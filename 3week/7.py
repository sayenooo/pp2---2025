def Filter(n):
    if (n<=1):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        break
    return True
    
a=[]
while True:
   i = int(input())
   a.append(i)
   if i==0:
       break
  
new_list = list(filter(lambda aa: Filter(aa) , a))
print(new_list, end = " ")
        
    
