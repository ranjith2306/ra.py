s,r=map(int,input().split())
for i in range(s+1,r):
	for k in range(2,i):
		if(i%k==0):
			break
	else:
		print(i,end=" ")
