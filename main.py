# head recursion

def headrec(n,num):
  if n < num:
   return
  headrec(n-1,num) 
  print(n)  
#headrec(20,1)


def tailrec(n,num):
  if n > num:
    return
  print(n)
  tailrec(n+1,num)
#tailrec(20,50)  

def incdec(n,num):
  if (n < 1 or n > num):
     return 
  print(n)
  incdec(n-1,num)
  print(n)
incdec(5,5)

