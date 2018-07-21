import time
key=1
while(key!=0):
	tstamp[key]=time.time()
	head[key]=[key,key-1,count[key]]
	body[key]
	if(n>1):
		n+=1
	name[[key],[n]]=input('Enter the Name of transaction :')
	amount[[key],[n]]=float(input('Enter the Amount of transaction '))
	block[key]=[head[key],body[key],tstamp[key],tail[key]]
	count+=1
	trig=input('If you want to enter more transaction(y/n)')
	
	if(trig==y or trig==Y):
		key+=1
	elif(trig==n or trig==N):
		key=0
	else:
		print('Invalid Entry!!')	



	
		