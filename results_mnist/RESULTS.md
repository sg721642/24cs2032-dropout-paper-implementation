# Actual measured results

Final fixed epoch; rates selected using mean validation error only.
SD is sample standard deviation across seeds; one seed has no SD.

| Dataset | Drop rate | Train error % | Val error % | Test error % | Test SD | Gap pp |
|---|---:|---:|---:|---:|---:|---:|
| mnist | 0.0 | 0.203 | 4.260 | 4.320 | 0.295 | 4.117 |
| mnist | 0.1 | 0.090 | 4.180 | 4.050 | 0.278 | 3.960 |
| mnist | 0.2 | 0.110 | 3.893 | 3.900 | 0.239 | 3.790 |
| mnist | 0.3 | 0.240 | 3.753 | 3.820 | 0.118 | 3.580 |
| mnist | 0.4 | 0.323 | 3.747 | 3.843 | 0.282 | 3.520 |
| mnist | 0.5 | 0.700 | 3.840 | 3.883 | 0.087 | 3.183 |
| mnist | 0.6 | 1.273 | 4.407 | 4.380 | 0.104 | 3.107 |
| mnist | 0.7 | 2.513 | 5.133 | 5.110 | 0.147 | 2.597 |

mnist: validation-selected drop rate = 0.4.
Test-error change vs no dropout = 0.477 percentage points (positive means lower error with the selected model).
