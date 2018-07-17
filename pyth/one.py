import sys
print(sys.version)
print('Random String!')
obj=10
print(obj)
#if else statement:
if obj>20:
	print('Greater')
elif obj>15:
	print('Middle')
else:
    print('Smaller')
print('Outside ifelse')    
obj2=280
while obj2<=300:
	print(obj2)
	obj2+=1
l=['aa','bb','cc']	
for iteration in l:	
	print('iteration')
for iteration in range(1,7):	
	print('iteration',iteration)	