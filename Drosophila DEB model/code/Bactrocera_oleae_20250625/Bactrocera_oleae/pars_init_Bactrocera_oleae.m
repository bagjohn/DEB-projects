function [par, metaPar, txtPar] = pars_init_Bactrocera_oleae(metaData)

metaPar.model = 'abp'; 

%% reference parameter (not to be changed) 
par.T_ref = 293.15;   free.T_ref = 0;   units.T_ref = 'K';        label.T_ref = 'Reference temperature'; 

%% core primary parameters 
par.T_A = 8822.1635;  free.T_A   = 1;   units.T_A = 'K';          label.T_A = 'Arrhenius temperature'; 
par.z = 0.1081;       free.z     = 1;   units.z = '-';            label.z = 'zoom factor'; 
par.F_m = 6.5;        free.F_m   = 0;   units.F_m = 'l/d.cm^2';   label.F_m = '{F_m}, max spec searching rate'; 
par.kap_X = 0.8;      free.kap_X = 0;   units.kap_X = '-';        label.kap_X = 'digestion efficiency of food to reserve'; 
par.kap_P = 0.1;      free.kap_P = 0;   units.kap_P = '-';        label.kap_P = 'faecation efficiency of food to faeces'; 
par.v = 0.0061786;    free.v     = 1;   units.v = 'cm/d';         label.v = 'energy conductance'; 
par.kap = 0.90044;    free.kap   = 1;   units.kap = '-';          label.kap = 'allocation fraction to soma'; 
par.kap_R = 0.95;     free.kap_R = 0;   units.kap_R = '-';        label.kap_R = 'reproduction efficiency'; 
par.p_M = 3641.4108;  free.p_M   = 1;   units.p_M = 'J/d.cm^3';   label.p_M = '[p_M], vol-spec somatic maint'; 
par.p_T = 0;          free.p_T   = 0;   units.p_T = 'J/d.cm^2';   label.p_T = '{p_T}, surf-spec somatic maint'; 
par.k_J = 0.002;      free.k_J   = 0;   units.k_J = '1/d';        label.k_J = 'maturity maint rate coefficient'; 
par.E_G = 4455.3757;  free.E_G   = 1;   units.E_G = 'J/cm^3';     label.E_G = '[E_G], spec cost for structure'; 
par.E_Hb = 3.012e-03; free.E_Hb  = 1;   units.E_Hb = 'J';         label.E_Hb = 'maturity at birth'; 
par.E_Hp = 6.375e-01; free.E_Hp  = 1;   units.E_Hp = 'J';         label.E_Hp = 'maturity at puberty'; 
par.h_a = 2.504e-06;  free.h_a   = 1;   units.h_a = '1/d^2';      label.h_a = 'Weibull aging acceleration'; 
par.s_G = 0.0001;     free.s_G   = 0;   units.s_G = '-';          label.s_G = 'Gompertz stress coefficient'; 

%% other parameters 
par.E_He = 2.462e+00; free.E_He  = 1;   units.E_He = 'J';         label.E_He = 'maturity at emergence'; 
par.Lb_tL_T = 0.0071064;  free.Lb_tL_T = 1;   units.Lb_tL_T = 'cm';     label.Lb_tL_T = 'structural length at birth for f_tL_T data'; 
par.T_AH = 2417.1786;  free.T_AH  = 1;   units.T_AH = 'K';         label.T_AH = 'Arrhenius temperature for upper boundary'; 
par.T_AL = 716.4401;  free.T_AL  = 1;   units.T_AL = 'K';         label.T_AL = 'Arrhenius temperature for lower boundary'; 
par.T_H = 311.5243;   free.T_H   = 1;   units.T_H = 'K';          label.T_H = 'upper boundary'; 
par.T_L = 292.0274;   free.T_L   = 1;   units.T_L = 'K';          label.T_L = 'lower boundary'; 
par.del_M = 0.13599;  free.del_M = 1;   units.del_M = '-';        label.del_M = 'shape coefficient'; 
par.f = 1;            free.f     = 0;   units.f = '-';            label.f = 'scaled functional response for 0-var data'; 
par.f_3 = 0.77783;    free.f_3   = 1;   units.f_3 = '-';          label.f_3 = 'scaled functional response for tWw data'; 
par.f_4 = 0.73417;    free.f_4   = 1;   units.f_4 = '-';          label.f_4 = 'scaled functional response for tWw data'; 
par.h_Tb = 65.5295;   free.h_Tb  = 1;   units.h_Tb = '1/d';       label.h_Tb = 'heat stress for egg'; 
par.h_Ti = 7.5675;    free.h_Ti  = 1;   units.h_Ti = '1/d';       label.h_Ti = 'heat stress for imago'; 
par.h_Tp = 418.0979;  free.h_Tp  = 1;   units.h_Tp = '1/d';       label.h_Tp = 'heat stress for pupa'; 
par.h_i = 0.015555;   free.h_i   = 1;   units.h_i = '1/d';        label.h_i = 'imago hazard rate'; 
par.kap_V = 0.53905;  free.kap_V = 1;   units.kap_V = '-';        label.kap_V = 'conversion efficiency E -> V -> E'; 
par.s_1 = 15.6479;    free.s_1   = 1;   units.s_1 = '-';          label.s_1 = 'stress at instar 1: L_1^2/ L_b^2'; 
par.s_2 = 1.7975;     free.s_2   = 1;   units.s_2 = '-';          label.s_2 = 'stress at instar 2: L_2^2/ L_1^2'; 

%% set chemical parameters from Kooy2010 
[par, units, label, free] = addchem(par, units, label, free, metaData.phylum, metaData.class); 

%% Pack output: 
txtPar.units = units; txtPar.label = label; par.free = free; 
