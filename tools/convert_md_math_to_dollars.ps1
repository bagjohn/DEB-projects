param(
    [Parameter(Mandatory = $false)]
    [string]$Root = (Get-Location).Path,

    [Parameter(Mandatory = $false)]
    [switch]$WhatIf
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Convert-LineOutsideCode([string]$line) {
    if ([string]::IsNullOrEmpty($line)) { return $line }

    $matches = [regex]::Matches($line, '`+')
    if ($matches.Count -eq 0) {
        return (Convert-TextOutsideInlineCode $line)
    }

    $sb = New-Object System.Text.StringBuilder
    $cursor = 0
    $inInlineCode = $false

    foreach ($m in $matches) {
        $segment = $line.Substring($cursor, $m.Index - $cursor)
        if (-not $inInlineCode) {
            $segment = Convert-TextOutsideInlineCode $segment
        }
        [void]$sb.Append($segment)
        [void]$sb.Append($m.Value)
        $inInlineCode = -not $inInlineCode
        $cursor = $m.Index + $m.Length
    }

    $tail = $line.Substring($cursor)
    if (-not $inInlineCode) {
        $tail = Convert-TextOutsideInlineCode $tail
    }
    [void]$sb.Append($tail)

    return $sb.ToString()
}

function Convert-TextOutsideInlineCode([string]$text) {
    if ([string]::IsNullOrEmpty($text)) { return $text }

    # Block math delimiters
    $text = $text -replace '\\\[', '$$'
    $text = $text -replace '\\\]', '$$'

    # Inline math delimiters
    $text = $text -replace '\\\(', '$'
    $text = $text -replace '\\\)', '$'

    return $text
}

$rootPath = (Resolve-Path -LiteralPath $Root).Path
$files = Get-ChildItem -LiteralPath $rootPath -Recurse -File -Filter '*.md'

$changedFiles = 0

foreach ($file in $files) {
    $lines = Get-Content -LiteralPath $file.FullName -Encoding UTF8

    $inFence = $false
    $fenceMarker = ''
    $out = New-Object System.Collections.Generic.List[string]

    foreach ($line in $lines) {
        $trim = $line.TrimStart()
        $fenceMatch = [regex]::Match($trim, '^(?<fence>`{3,}|~{3,})')
        if ($fenceMatch.Success) {
            $marker = $fenceMatch.Groups['fence'].Value.Substring(0,3)
            if (-not $inFence) {
                $inFence = $true
                $fenceMarker = $marker
            } elseif ($trim.StartsWith($fenceMarker)) {
                $inFence = $false
                $fenceMarker = ''
            }
            $out.Add($line)
            continue
        }

        if ($inFence) {
            $out.Add($line)
            continue
        }

        $out.Add((Convert-LineOutsideCode $line))
    }

    $newText = ($out -join "`r`n")
    $oldText = ($lines -join "`r`n")

    if ($newText -ne $oldText) {
        $changedFiles++
        if (-not $WhatIf) {
            Set-Content -LiteralPath $file.FullName -Encoding UTF8 -Value $out
        }
    }
}

if ($WhatIf) {
    Write-Host "Would change $changedFiles markdown file(s) under: $rootPath"
} else {
    Write-Host "Updated $changedFiles markdown file(s) under: $rootPath"
}
