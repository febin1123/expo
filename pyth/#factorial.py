#factorial.py

num1=int(input('Enter a number:'))
print('factorial is:',fact(num1))

def fact(a):
	if(a==1 or a==0):
		return a
	else:	
  		return (a*fact(a-1))

 	
     	