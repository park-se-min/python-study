def add(arr):
	return arr[0] + arr[1]

print(add([1, 2]))


add2 = lambda arr: arr[0] + arr[1]

print(add2([1, 2]))

# def add(a, b):
# 	return a+b

# print(add(1,2))


# def add(arr):
# 	return arr['a'] + arr['b']

# print(add({'a':2, 'b':4}))


# def add_many(str, *args):
# 	if str=='a':
# 		result = 0
# 		for i in args:
# 			result = result + i
# 	elif str=='m':
# 		result = 1
# 		for i in args:
# 			result = result * i

# 	return result

# result = add_many('m', 1,2,3,4,5)
# print(result)

# result = add_many('a', 1,2,3,4,5)
# print(result)



# def re(str, *num):
# 	if str == 'a':
# 		result = 0
# 		for i in num:
# 			result = result + i
# 	elif str == 'm':
# 		result = 1
# 		for i in num:
# 			result = result * i

# 	return result


# result = re('a', 1,2,3,4,5)
# print(result)
