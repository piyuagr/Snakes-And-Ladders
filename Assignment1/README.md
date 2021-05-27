Using python library hashlib.
I used sha256 constructor of this hashlib library of python to calculate sha256 of a string.
Then I compared hexadecimal representation of sha256 of input string appended with x( a positive integer) with "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff".
We will start loop with x = 1 and will continue incrementing x untill we find a x such that when it is appended to the input string will generate a sha256 string of it's own such that it is less than "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
time library is used to get current time at that start and end of the program.
