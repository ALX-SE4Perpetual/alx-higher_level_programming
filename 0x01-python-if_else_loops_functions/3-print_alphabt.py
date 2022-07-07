#!/usr/bin/python3

# print ASCII alphabets in lowercase
# except letters q and e
# Only use one print function
# Only use one loop in your code
# Do not store char in a variable and do not import module

for letters in range(97, 123):
    if chr(letters) != q and chr(letters) != e:
	print ("{}".format(chr(letters)), end="")
