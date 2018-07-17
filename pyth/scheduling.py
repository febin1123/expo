r=int(input('Enter the number of rooms: '))
R=[]
m=int(input('Enter the number of interviewers: '))
M=[]
n=int(input('Enter the number of Candidates: '))
N=[]
for i in range(1,r):
	for j in range(1,m):
		for k in range(1,n):
			if(R[i]==0):
				if(M[j]==0):
					R[i]=n
					M[j]=n
					print('room ',R[i],' allotted to interviewer ',M[j],' and candidate ',N[k])
