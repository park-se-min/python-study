a = [2, 4]
b = '123456789'
print(b[a[0]:a[1]])
print(b[2:4])


a = ['a', 'b', 1, 2]
a = [(1,2), (3,4), (5,6)]
for i in a:
	print(i)


for (first, last) in a:
	print(first + last)



a = [90, 25, 67, 45, 80]
i = 0
for j in a:
	i = i + 1

	if j > 60:
		print('%s 학생은 합격' % i)
	else:
		print('%s 학생은 불합격' % i)