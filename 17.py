c=int(input())
ab=c
sum=0
while c>0:
	b=c%10
	sum=sum+b*b*b
	c=c/10
	if ab==sum:
		print("yes")
else:
	print("no")
