import numpy as np
import numpy.testing as npt
a = np.arange(10)
b = np.arange(10)

# assert a == b
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
print((a == b).all())
# True

# print(np.version.version)

# print(pd.__version__)

# print(npt.assert_array_equal([1, 2, 3], [1, 2, 3]))

# print(npt.assert_array_equal([1, 2, 3], [1, 2, 3, 4, 5]))

# print(npt.assert_array_equal([99, 2, 3], [99, 2, 3]))


# print(npt.assert_array_equal([np.pi], [np.sqrt(np.pi) ** 2]))

# For floating points
print(npt.assert_allclose([np.pi], [np.sqrt(np.pi) ** 2]))

