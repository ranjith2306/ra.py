for raj in range(100,1000):
  temp=raj
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
      if sum==raj:
           print (raj)
