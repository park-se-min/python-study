a = range(2, 10)
b = range(2, 10)

# for x in a:
# 	for y in b:
# 		print("%s X %s = %s" % (x, y, x*y))


a = range(2, 10)
b = range(2, 10)

# for x in a:
# 	for y in b:
# 		print("%s X %s = %s" % (x, y, x*y))

c = [
		"%s X %s = %s" % (x, y, x*y)
			for x in a
				for y in b
	]

for d in c:
	print(d)