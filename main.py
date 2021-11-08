def pal(n):
    if(n[::-1]==n):
          return 1
    else:
          return 0
n=input()
print(pal(n))
   