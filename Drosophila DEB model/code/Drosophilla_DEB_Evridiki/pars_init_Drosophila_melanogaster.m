function [par, metaPar, txtPar] = pars_init_Drosophila_melanogaster(metaData)

metaPar.model = 'abp'; 

%% reference parameter (not to be changed) 
par.T_ref = 293.15;   free.T_ref = 0;   units.T_ref = 'K';        label.T_ref = 'Reference temperature'; 

%% core primary parameters 
par.T_A = 25597.2574;  free.T_A   = 1;   units.T_A = 'K';          label.T_A = 'Arrhenius temperature'; 
par.z = 0.049897;     free.z     = 1;   units.z = '-';            label.z = 'zoom factor'; 
par.F_m = 6.5;        free.F_m   = 0;   units.F_m = 'l/d.cm^2';   label.F_m = '{F_m}, max spec searching rate'; 
par.kap_X = 0.8;      free.kap_X = 0;   units.kap_X = '-';        label.kap_X = 'digestion efficiency of food to reserve'; 
par.kap_P = 0.1;      free.kap_P = 0;   units.kap_P = '-';        label.kap_P = 'faecation efficiency of food to faeces'; 
par.v = 0.04503;      free.v     = 1;   units.v = 'cm/d';         label.v = 'energy conductance'; 
par.kap = 0.76205;    free.kap   = 1;   units.kap = '-';          label.kap = 'allocation fraction to soma'; 
par.kap_R = 0.95;     free.kap_R = 0;   units.kap_R = '-';        label.kap_R = 'reproduction efficiency'; 
par.p_M = 11832.9085;  free.p_M   = 1;   units.p_M = 'J/d.cm^3';   label.p_M = '[p_M], vol-spec somatic maint'; 
par.p_T = 0;          free.p_T   = 0;   units.p_T = 'J/d.cm^2';   label.p_T = '{p_T}, surf-spec somatic maint'; 
par.k_J = 0.002;      free.k_J   = 0;   units.k_J = '1/d';        label.k_J = 'maturity maint rate coefficient'; 
par.E_G = 4419.5703;  free.E_G   = 1;   units.E_G = 'J/cm^3';     label.E_G = '[E_G], spec cost for structure'; 
par.E_Hb = 2.806e-01; free.E_Hb  = 1;   units.E_Hb = 'J';         label.E_Hb = 'maturity at birth'; 
par.E_Hp = 3.489e+02; free.E_Hp  = 1;   units.E_Hp = 'J';         label.E_Hp = 'maturity at puberty'; 
par.h_a = 4.021e-08;  free.h_a   = 1;   units.h_a = '1/d^2';      label.h_a = 'Weibull aging acceleration'; 
par.s_G = 0.0001;     free.s_G   = 0;   units.s_G = '-';          label.s_G = 'Gompertz stress coefficient'; 

%% other parameters 
par.E_He = 7.665e-01; free.E_He  = 1;   units.E_He = 'J';         label.E_He = 'maturity at emergence'; 
par.del_M = 0.60521;  free.del_M = 1;   units.del_M = '-';        label.del_M = 'shape coefficient for head capsule of larva'; 
par.del_Mw = 0.36848;  free.del_Mw = 1;   units.del_Mw = '-';       label.del_Mw = 'shape coefficient for wing length of imago'; 
par.f = 1;            free.f     = 0;   units.f = '-';            label.f = 'scaled functional response for 0-var data'; 
par.f_DR = 0.98936;   free.f_DR  = 1;   units.f_DR = '-';         label.f_DR = 'scaled functional response for DR diet'; 
par.f_F424 = 1.3563;  free.f_F424 = 1;   units.f_F424 = '-';       label.f_F424 = 'scaled functional response for F424 diet'; 
par.f_HS = 0.89751;   free.f_HS  = 1;   units.f_HS = '-';         label.f_HS = 'scaled functional response for HS diet'; 
par.f_JAZZ = 1.5645;  free.f_JAZZ = 1;   units.f_JAZZ = '-';       label.f_JAZZ = 'scaled functional response for JAZZ diet'; 
par.kap_V = 0.00088239;  free.kap_V = 1;   units.kap_V = '-';        label.kap_V = 'conversion efficient E -> V -> E'; 
par.s_1 = 3.9772;     free.s_1   = 1;   units.s_1 = '-';          label.s_1 = 'stress at instar 1: L_1^2/ L_b^2'; 
par.s_2 = 3.0775;     free.s_2   = 1;   units.s_2 = '-';          label.s_2 = 'stress at instar 2: L_2^2/ L_1^2'; 

%% set chemical parameters from Kooy2010 
[par, units, label, free] = addchem(par, units, label, free, metaData.phylum, metaData.class); 

%% Pack output: 
txtPar.units = units; txtPar.label = label; par.free = free; 
