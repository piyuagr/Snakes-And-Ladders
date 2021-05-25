Using python library hashlib.
We used sha256 constructor of this hashlib library of python to calculate sha256 of a string.
Then we compare hexadecimal representation of sha256 of input string appended with x( a positive integer) with "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff".
We will start loop with x = 1 and will continue incrementing x untill we find a x satisfying above condition. 