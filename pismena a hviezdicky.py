s = 'Python'
j='.......'
g= 5
for i in range(0,len(s)):
    ns = j[:g+1]+s[:i+1]
    g-=1
    
    
    print(ns)
