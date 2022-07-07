#!/usr/bin/python3
# print ASCII alphabets in lowercase except letters q and e
for letters in range(97, 123):
    if chr(letters) != 'q' and chr(letters) != 'e':
	print("{}".format(chr(letters)), end="")
