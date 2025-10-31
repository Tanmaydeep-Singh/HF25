N = int(input())
c = 0
# if N==2 or N==3 or N==5 or N==7:
#         c = 1 
# else:        
    for i in range(2,N+1):
        
        prime=1
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=0
                break
        if prime==1 and N%i==0:
            c += 1
print(c)
