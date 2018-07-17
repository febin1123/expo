R[r]=0
r=int(input('Enter the number of rooms'))
M[m]=0
m=int(input('Enter the number of interviewers'))
N[n]=0
n=int(input('Enter the number of Candidates'))
for i in range(1,r):
	for j in range(1,m):
		for k in range(1,n):
			if(R[i]==0):
				if(M[j]==0):
					R[i]=n
					M[j]=n
					print('room ',R[i],' allotted to interviewer ',M[j],' and candidate ',N[k])






