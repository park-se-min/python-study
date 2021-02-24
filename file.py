# f = open("./새파일.txt", 'w')
# a = input("제목")
# f.write(a)
# f.write("\n")
# for i in range(1, 11):
#     data = "%d 번째 ddd 줄입니다.\n" % i
#     f.write(data)
# f.close()


# f = open("새파일.txt",'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()


f = open("새파일.txt", 'r')
# line = f.readline()

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
# print(line)

f = open("새파일.txt", 'r')
d = f.read()
print(d)
f.close()