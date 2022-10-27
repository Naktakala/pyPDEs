#========== Problem Description ==========
# Isotope: Be9
# Problem type: Neutron only
# Neutron group structure: 3 groups

# Output
NUM_GROUPS 3
NUM_MOMENTS 8
NUM_PRECURSORS 0

NEUTRON_GS_BEGIN
0    5        1000    
1    1000     1e+06   
2    1e+06    2e+07   
NEUTRON_GS_END

SIGMA_T_BEGIN
0    2.31929
1    5.37674
2    6.15252
SIGMA_T_END

SIGMA_A_BEGIN
0    0.23091
1    3e-05
2    0.00025
SIGMA_A_END

SIGMA_S_BEGIN
0    2.44974
1    5.37671
2    6.15227
SIGMA_S_END

SIGMA_HEAT_BEGIN
0    1.0304e+06
1    102439
2    209.561
SIGMA_HEAT_END

INV_VELOCITY_BEGIN
0    4.82077e-08
1    6.40039e-07
2    1.13247e-05
INV_VELOCITY_END

TRANSFER_MOMENTS_BEGIN
# l = 0
M_GPRIME_G_VAL 0   0    0    1.90886
M_GPRIME_G_VAL 0   0    1    0.540851
M_GPRIME_G_VAL 0   0    2    2.56802e-05
M_GPRIME_G_VAL 0   1    1    5.19177
M_GPRIME_G_VAL 0   1    2    0.184941
M_GPRIME_G_VAL 0   2    2    6.15227
# l = 1
M_GPRIME_G_VAL 1   0    0    0.734422
M_GPRIME_G_VAL 1   0    1    0.0183397
M_GPRIME_G_VAL 1   0    2    1.57249e-05
M_GPRIME_G_VAL 1   1    1    0.508905
M_GPRIME_G_VAL 1   1    2    -0.05209
M_GPRIME_G_VAL 1   2    2    0.459051
# l = 2
M_GPRIME_G_VAL 2   0    0    0.449243
M_GPRIME_G_VAL 2   0    1    -0.0195827
M_GPRIME_G_VAL 2   0    2    8.9588e-06
M_GPRIME_G_VAL 2   1    1    0.0369711
M_GPRIME_G_VAL 2   1    2    -0.00547063
M_GPRIME_G_VAL 2   2    2    0.015441
# l = 3
M_GPRIME_G_VAL 3   0    0    0.189342
M_GPRIME_G_VAL 3   0    1    -0.0059203
M_GPRIME_G_VAL 3   0    2    4.53805e-06
M_GPRIME_G_VAL 3   1    1    0.000969831
M_GPRIME_G_VAL 3   1    2    -0.000191121
# l = 4
M_GPRIME_G_VAL 4   0    0    0.0519815
M_GPRIME_G_VAL 4   0    1    0.000467378
M_GPRIME_G_VAL 4   0    2    2.51422e-06
M_GPRIME_G_VAL 4   1    1    -0.000241489
M_GPRIME_G_VAL 4   1    2    1.87619e-06
M_GPRIME_G_VAL 4   2    2    -1.53807e-05
# l = 5
M_GPRIME_G_VAL 5   0    0    0.0107519
M_GPRIME_G_VAL 5   0    1    0.000985541
M_GPRIME_G_VAL 5   0    2    3.56523e-06
M_GPRIME_G_VAL 5   1    1    -4.27064e-05
M_GPRIME_G_VAL 5   1    2    3.81841e-07
# l = 6
M_GPRIME_G_VAL 6   0    0    0.00265384
M_GPRIME_G_VAL 6   0    1    0.000112783
M_GPRIME_G_VAL 6   0    2    4.60313e-06
M_GPRIME_G_VAL 6   1    1    -3.69913e-06
M_GPRIME_G_VAL 6   1    2    -8.65758e-07
# l = 7
M_GPRIME_G_VAL 7   0    0    0.000622115
M_GPRIME_G_VAL 7   0    1    0.000104345
M_GPRIME_G_VAL 7   0    2    2.83288e-06
M_GPRIME_G_VAL 7   1    1    8.79622e-08
M_GPRIME_G_VAL 7   1    2    6.37494e-06
M_GPRIME_G_VAL 7   2    2    6.15227e-07
TRANSFER_MOMENTS_END
