import turtle

# Python - интерпретируемый язык (построчное преобразование кода в машинный код - на лету).
# Типы данных Python - int, float, bool, string

# print(0.2 + 0.1)
# print(2 ** 1000)


# name = input("What's your name? ")
# lastname = input("What's your last name? ")

# print(f"Hello, {name} {lastname}!")


# x = 10

# while True:
# 	x -= 1
# 	if x < 0:
# 		break
# 	print(x)

# print("done")

# x = 0
# while x <= 10:
# 	print(x)
# 	x += 1

# for i in 1,2,3,4,5,6,7:
# 	if i == 4:
# 		break
# 	print(i, end='')



# x = 10

# if x == 3:
# 	print('x is 3')
# else:
# 	print('x is 10')


def myTurtle():
	for step in range(6):
		turtle.begin_fill()
		for i in range(3):
			turtle.forward(30)
			turtle.left(360 / 3)
		turtle.end_fill()
		
		turtle.forward(50)
		turtle.right(60)


	

turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('blue', 'darkblue')
turtle.forward(300)
turtle.pensize(3)
turtle.speed(10)



myTurtle()
turtle.backward(300)
myTurtle()


turtle.done()



# x = int(input())
# y = int(input())


# if x > 0 and y >0:
# 	print("ONE period")
# else:
# 	if x < 0 and y > 0:
# 		print('TWO period')
# 	else:
# 		if x < 0 and y < 0:
# 			print('THREE period')
# 		else:
# 			if x > 0 and y < 0:
# 				print('FOUR period')
# 			else:
# 				print("NEVER")

# # Более ПЛОСКАЯ СТРУКТУРА - BEST PRACTICE

# a = int(input())
# b = int(input())

# if x > 0 and y >0:
# 	print("ONE period")
# elif x < 0 and y > 0:
# 	print('TWO period')
# elif x < 0 and y < 0:
# 	print('THREE period')
# elif x > 0 and y < 0:
# 	print('FOUR period')
# else:
# 	print("NEVER")

