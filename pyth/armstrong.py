num=int(input('Enter a number: '))
s=len(num)
print(s)
temp=num
sum=0
for i in range(1,s):
	sum+=((temp%10)*s)
	temp//=10
if(num==sum):
	print('The give number is an Armgstrong number')
else:
	print('The give number is not an Armgstrong number')	