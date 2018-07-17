#factorial.py


def fact(a):
	if(a==1 or a==0):
		return a
	else:	
  		return (a*fact(a-1))

num1=int(input('Enter a number:'))
print('factorial is:',fact(num1))


 	
     	