def pairSum(arr,s):
    i=0
    lst=[]
    while i <len(arr):
        j=0
        while j <len(arr):
            if arr[i]+arr[j]==s and (min(arr[i],arr[j]),max(arr[i],arr[j])) not in lst:
                lst.append((min(arr[i],arr[j]),max(arr[i],arr[j])))
            j+=1
        i+=1
    return lst
#Driver Code
n,s=input().split()
n,s=int(n),int(s)
arr=input().split()
arr=[int(arr[i]) for i in range(n)]
pairs=pairSum(arr,s)
print("\n")
[print(a,b,"\r") for (a,b) in pairs]