a=int(input())
print("It is "+str(a==sum([pow(int(i),3) for i in str(a)]))+" that "+str(a)+" is a Armstrong number!")