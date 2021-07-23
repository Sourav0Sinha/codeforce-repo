'''Let's define S(x) to be the sum of digits of number x written in decimal system. For example, S(5)=5, S(10)=1, S(322)=7.

We will call an integer x interesting if S(x+1)<S(x). In each test you will be given one integer n. Your task is to calculate the number of integers x such that 1≤x≤n and x is interesting.

Input
The first line contains one integer t (1≤t≤1000)  — number of test cases.

Then t lines follow, the i-th line contains one integer n (1≤n≤109) for the i-th test case.

Output
Print t integers, the i-th should be the answer for the i-th test case.

Example
inputCopy
5
1
9
10
34
880055535
outputCopy
0
1
1
3
88005553
Note
The first interesting number is equal to 9.


'''
n = int(input())


data = []
for l in range(n):
    a = input()
    data.append(a)
  


def S(x):
    str1 = str(x)
    res = 0
    for j in str1:
        res += int(j)
        
    return res

def check(x,c):
    q = int(x)
    if x[0]=='8':
        q %= 8*(10**(len(x)-1))
        c += 8*(10**(len(x)-2))
        q = str(q)
        return check(q,c)
    else:
        return x,c
    
for i in data:
    count = 0
    i,c = check(i,count)
    
    q = int(i)
    count += c

    for j in range(1,q+1):
        cmp1 = S(j)
        cmp2 = S(j+1)
        if cmp1 > cmp2:
            count += 1
            
    print(count)