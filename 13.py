c=int(input())
if c>1:
	for d in range(2,c):
		if(c%d==0):
			print("no")
			break
	else:
		print("yes")
else:
	print("no")
