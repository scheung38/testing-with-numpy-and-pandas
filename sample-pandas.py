import pandas as pd
import pandas.util.testing as pdt

s1 = pd.Series([1, 2, 3], dtype='int')

s2 = pd.Series([1, 2, 3], dtype='float')

print(pdt.assert_series_equal(s1, s2))