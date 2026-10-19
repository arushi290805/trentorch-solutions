def summation(f, lo, hi):
    ans=0
    for i in range(lo,hi+1):
        ans=ans+f(i)
    return ans
