import sys

print(sys.argv)

a = sys.argv[1:]

for i in a:
	print(i.upper())