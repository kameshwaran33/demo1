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

#OUTPUT:
#median:5


