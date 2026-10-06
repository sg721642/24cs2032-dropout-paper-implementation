# Actual measured results

Final fixed epoch; rates selected using mean validation error only.
SD is sample standard deviation across seeds; one seed has no SD.

| Dataset | Drop rate | Train error % | Val error % | Test error % | Test SD | Gap pp |
|---|---:|---:|---:|---:|---:|---:|
| fashion | 0.0 | 7.130 | 13.127 | 14.663 | 0.175 | 7.533 |
| fashion | 0.1 | 7.587 | 13.113 | 14.220 | 0.105 | 6.633 |
| fashion | 0.2 | 8.583 | 13.087 | 14.347 | 0.253 | 5.763 |
| fashion | 0.3 | 9.393 | 13.267 | 14.567 | 0.396 | 5.173 |
| fashion | 0.4 | 10.060 | 13.573 | 14.647 | 0.330 | 4.587 |
| fashion | 0.5 | 10.990 | 13.747 | 15.133 | 0.325 | 4.143 |
| fashion | 0.6 | 12.273 | 14.380 | 15.730 | 0.373 | 3.457 |
| fashion | 0.7 | 14.543 | 15.673 | 17.453 | 0.376 | 2.910 |

fashion: validation-selected drop rate = 0.2.
Test-error change vs no dropout = 0.317 percentage points (positive means lower error with the selected model).
