
af = input("выберите (+ или -): ")
a = float(  input("введите первое число: ") )
b = float( input("введите воторое число: ") )
if af == "+":
	c = a + b
	print("Результат " + str(c) )
elif af == "-":
	c = a - b
	print("Результат " + str(c) ) 

else:
	print("выберите + или - ")

input()	