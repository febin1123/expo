res=0
trig=1
def add():
	num1=float(input('Enter the 1st number: '))
	num2=float(input('Enter the 2st number: '))
	return(num1+num2)
def sub():
	num1=float(input('Enter the 1st number: '))
	num2=float(input('Enter the 2st number: '))
	return(num1-num2)
def mul():
	num1=float(input('Enter the 1st number: '))
	num2=float(input('Enter the 2st number: '))
	return(num1*num2)
def div():
	num1=float(input('Enter the 1st number: '))
	num2=float(input('Enter the 2st number: '))
	if(num2==0):
		print('Undefined')
	else:
		return(num1*num2)
def sqr():
	num1=float(input('Enter the a number: '))
	return(num1**2)
def menu():
	print('Calculater Menu:')
	print('1.Adddition\t2.Subtraction\n3.Multiplication\t4.Division\n5.Squaring of a number')
	key=int(input('Enter Your Choice(1-5): '))
	if(key==1):
		res=add()
		print(res)
		calc()
	elif(key==2):
		res=sub()
		print(res)
		calc()
	elif(key==3):
		res=mul()
		print(res)
		calc()
	elif(key==4):
		res=div()
		print(res)
		calc()
	elif(key==5):
		res=sqr()
		print(res)
		calc()
	else:
		print('Invalid Entry!!!')
		menu()
def calc():
	print('1.Back to menu\t2.Exit')
	trig=int(input('Enter your choice: '))
	if(trig==2):
		exit()
	elif(trig==1):
		menu()	
	else:
		('Invalid Entry!!')
menu()	