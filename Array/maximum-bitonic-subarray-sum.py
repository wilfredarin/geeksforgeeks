#https://practice.geeksforgeeks.org/problems/maximum-bitonic-subarray-sum/0
test = int(input())
for t in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    inc = [a[0]]
    prev = a[0]
    for i in range(1,n):
        if a[i]>prev:
            inc.append(inc[-1]+a[i])
        else:
            inc.append(a[i])
        prev = a[i]
    dec = [a[-1]]
    prev = a[-1]
    for i in range(n-2,-1,-1):
        if a[i]>prev:
            dec.append(dec[-1]+a[i])
        else:
            dec.append(a[i])
        prev = a[i]
    dec = dec[::-1]
    ans = 0
    for i in range(n):
        ans = max(ans,inc[i]+dec[i]-a[i])
    print(ans)
            
