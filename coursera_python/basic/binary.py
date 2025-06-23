arr = [1,2,3,4,5,8]
lp = arr[0]
up = arr[5]
num = int(input())
mid = int((up + lp)/2)
while(lp<=up):
    
    if mid == num:
        print(mid)
    elif mid < num:
        lp = mid + 1
    else:
        up = mid - 1
    
        





