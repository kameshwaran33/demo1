'''Data = [25, 32, 28, 34, 24, 31, 36, 27, 29, 30]
mean = sum(Data) / len(Data)
print("The mean is:", mean)


#output
#The mean is :27.6'''


#median 
Data = [2,3,4,5,6,7,8,9,3]
Data.sort()
N=len(Data)
if(N%2==0):
    median=Data[N//2-1]+Data[N//2]/2
    print("median",median)
else:
    median=Data[N//2]
    print("median",median)

