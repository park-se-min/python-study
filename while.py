a = 0
while a < 10:
	a = a + 1
	print('나무 %s 찍었습니다' % a)
	if a >= 10:
		print('나무 쓰러짐')


prompt = """
1. Add
2. Del
3. List
4. Quit
5. Enter number:
ㄴㅇ"""

# number = 0
# while number != 4:
# 	print(prompt)
# 	number = int(input())

z = input("dddd : ")
if z == '':
	print(11)
else:
	print(22)

print('입력값 : '+ z)

coffee = 10
while True:
    money = input("돈을 넣어 주세요: ")

    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
