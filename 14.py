ran1,ran2=map(int,input().split())
for ran3 in range(ran1+1,ran2):
	if(ran3%2!=0):
		print(ran3,end=" ")
