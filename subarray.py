def index(l,s):
    i = 0
    while i < len(l):
        x = l[i]
        j = i+1
        if x == s:
            j = len(l)
            return [i+1,0]
            break
        while j < len(l):
            x += l[j]
            if x == s:
                return [i+1,j+1]
                break
            else:
                j += 1
        i += 1
    if i == len(l):
        return [-1,0]
            
tc = int(input())
for i in range(tc):
    n , s = list(map(int,input().split()))
    l = list(map(int,input().split()))
    a,b = index(l,s)
    if b == 0:
        print(a)
    else:
        print('{} {}'.format(str(a),str(b)))
    
