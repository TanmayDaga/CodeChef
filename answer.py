# cook your dish here
def ans(n):
    if n < 2048 :
        return(bin(n).count('1'))
    else :
        n = n - 2048
        return (1+ans(n))
    
for t in range(int(input())):
    n = int(input())
    print(ans(n))
    