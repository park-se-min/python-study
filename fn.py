# print(divmod(5, 20))

# a = ['a', 'b', 'c']

# for i, name in enumerate(a):
#     print(name)
#     # print(i)
#     # print(':')


# print(eval('1'+'2'))

# a = input()
# b = input("Enter: ")
# print(b)

def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)


def two_times(x):
	return x*2

print(list(map(two_times, [1, 2, 3, 4])))