import numpy as np

# Resultados de NAIVE LCS
naiveHip1 = np.array([8.50706e37,1.26765e30,1.15792e77,1.36113e39,4.67681e49,1.20893e24,2.81475e14,4.39805e12,1.32923e36,3.24519e32,1.3938e42,9.5781e52,8.50706e37,2.02824e31,1.18059e21,1.80144e16,9.22337e18,3.02231e23,1.80144e16,1.15292e18,5.44452e39,268435456,3.77789e22,8.50706e37,3.24519e32,2.23007e43,1.15292e18,2.2836e46,1.15292e18,3435973836,3435973836,6.2771e57,4.05648e31,1.80144e16,1.36113e39,3.51844e13,4.72237e21,4.72237e21,1.80144e16,3.74144e50,1.93428e25,1.75922e13,1.23794e27,2.81475e14,1073741824,7.3787e19,1.3938e42,3.74144e50,2.65846e36,3.51844e13,3.77789e22,1.5325e54,7.20576e16,1.80144e16,6.12998e54,4.05648e31,4.39805e12,1.80144e16,6.12998e54,5.02168e58,1.75922e13,6871947673,1.09951e12,6.2771e57,2.41785e24,2.23007e43,1.76685e72,2.69599e67,1.29807e33,3.40282e38,1.15292e18,1.23794e27,1.11504e43,1.15292e18,33554432,3.24519e32,6871947673,1.20893e24,2.41785e24,9.22337e18,6.12998e54,2.23007e43,2.81475e14,2.02824e31,1.93428e25,1048576,3.24519e32,5.1923e33,1048576,5.1923e33,1.5325e54,3.68935e19,1.42725e45,6.12998e54,4.39805e12,1.09951e12,2.81475e14,1.15292e18,7.92282e28,1073741824])
naiveHip2 = np.array([8388608,1048576,4294967296,8388608,67108864,262144,16384,8192,8388608,2097152,16777216,134217728,8388608,2097152,524288,32768,65536,524288,32768,131072,8388608,2048,1048576,8388608,2097152,33554432,524288,33554432,131072,4096,4096,268435456,4194304,32768,8388608,16384,262144,262144,32768,67108864,524288,32768,524288,16384,2048,131072,16777216,67108864,4194304,16384,1048576,134217728,262144,32768,134217728,4194304,8192,32768,134217728,268435456,32768,4096,16384,268435456,262144,33554432,2147483648,1073741824,2097152,16777216,524288,2097152,16777216,65536,1024,2097152,4096,2097152,262144,65536,134217728,33554432,65536,2097152,1048576,512,2097152,4194304,512,4194304,134217728,262144,33554432,134217728,8192,16384,65536,65536,4194304,2048])
naivePasosEj = np.array([1259004,197703,320600341,1015597,5904225,51725,5519,3431,710944,292988,3038705,13899533,992481,189447,18291,6159,20989,33776,9919,8720,768918,659,29077,966241,559384,2112003,7163,6669959,12352,1443,1178,20060849,195708,5443,909806,2505,13418,27994,6392,10232879,87562,572,114443,2792,704,15009,1890944,10131255,833783,1477,3344,5407103,4945,7741,39665864,312202,2451,10009,24550172,25535154,1630,1847,997,7065454,48725,2410759,248184154,119618586,571191,666123,917,89223,2897512,8169,503,222163,1847,27845,62439,8439,11475704,892565,3114,334373,72564,251,84871,488325,173,438816,19243137,8393,4096618,22003792,1516,1096,3639,11899,24952,880])
naiveTiempos = np.array([692.38179,114.49520,215357.57265,806.33268,3310.29644,32.42427,3.08518,1.87516,424.34194,194.88988,1780.66980,8233.58425,516.59173,115.29314,13.93715,3.21456,20.64212,24.11601,6.40688,7.58157,422.69591,0.35508,18.83707,574.27477,296.96116,1226.06595,3.80218,4246.39289,6.88337,0.72442,0.72841,11694.40342,125.12774,3.36902,520.80371,1.25390,7.18203,15.22583,4.36017,6243.58186,70.73791,0.42063,69.27426,1.40437,0.37161,8.95345,1198.20304,5599.84588,455.44448,0.75063,1.60158,2999.95782,2.85719,3.98058,27226.58119,189.90276,1.59360,5.82610,13459.96367,16596.17308,0.89768,1.09375,0.90452,4047.99891,46.59625,1495.53182,155169.74339,75224.50541,324.85371,365.50758,0.46679,53.22142,2783.67177,6.03641,0.34653,285.96328,1.61697,24.99945,134.31602,11.11701,8350.80840,487.08563,1.52463,177.60480,46.61221,0.12881,67.85849,313.57654,0.09860,266.32542,10409.05741,4.65484,3597.09641,16528.44398,0.82359,0.66628,2.14988,11.85966, 23.20123, 0.52778])

# Resultados de EFFICIENT LCS
efficientHip1 = np.array([])
efficientHip2 = np.array([])
efficientAccesosMatriz = np.array([])
efficientTiempos = np.array([])

# Resultados de BOTTOM LCS
bottomHip1 = np.array([])
bottomHip2 = np.array([])
bottomAccesosMatriz = np.array([])
bottomTiempos = np.array([])