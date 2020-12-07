# ФУНКЦИИ. Локальность имен. 

# Dont Repeat Yourself (DRY). Антишаблон - WET - We Enjoy Typing.

# Функции - нужны для того, чтобы вызывать одни и тот же участок кода, как правило с разными аргументами. 

# Зачем нужен return? Указываем, куда нужно вернуть результат работы функции. В какой участок кода. 

# Каждый вызов функции порождает новое пространство имен



def foo(x, y):
	x[0] = y
	return 7



A = [1, 2, 3]

z = foo(A, 7)



print(A)
print(z)

# Duck Typing (Утиная типизация) - если некий объект выглядит как утка, плавает как утка и крякает как утка, значит это утка. 
# То есть Python не требует строгой типизации, как это делают языка Java, C, C++ и т.д. 

# Аннотации - НЕОбЯЗАТЕЛЬНЫЕ

def coo(x:str, y:int) -> str:
	result = x
	for i in range(y - 1):
		result += x
	return result

print(coo(2 , 5))
print(coo('MA', 2))




def voo(x, y=0, z=0):  #Значение по умолчанию z=0
	
	return 100*x + 10*y +1*z


print(voo(1, 2, 3))
print(voo(z=1, x=2, y=3)) # Named parameters.
print(voo(1, 2))
print(voo(7))


# Произвольное количество аргументов
def bar(*args, last_parameter = 'hleb'):
	for arg in args:
		print('bar arg =', arg)

bar([1,2,3])
bar(4, 5, 6)
bar('jelly', 'fish')









