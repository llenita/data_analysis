f1 = 1;
f2 = 1;
 
n = int(input())
 
if n < 1:
    quit()
elif n = 1 or n = 2:
    print("1")
    quit()
else:
    for i in range(2, n):
        fn = f1+f2
        f1=f2
        f2=fn
    print(fn)

