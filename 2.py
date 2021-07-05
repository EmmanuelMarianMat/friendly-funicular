def solution(n,k):
    if k<=1: #for cases 0 and 1
        return n*k

    multiples = dict()
    for i in range(1,n+1):
        multiples[i] = tuple(range(i,n+1,i))
    
    def rec(x,l):
        if l==k:
            return len(multiples[x])
        ret = sum(rec(num,l+1) for num in multiples[x])
        return ret
        
    return sum(rec(num,2) for num in range(1,n+1))


def main():
    n = int(input().rstrip())
    k = int(input().rstrip())
    print(solution(n,k))

main()


"""
input 1:
2
1
answer=2

input 2:
2
2
answer=3

input 3:
3
2
answer=5

input 4: (extra)
5
3
answer=16 (I think?)
"""