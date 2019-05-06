
# coding: utf-8

# In[31]:


x=int(input("Enter a number: "))   #Find all primes till number entered by user
c=1
i=1
p=0
print("All the primes till",x,"are")
while (c<=x):
    for i in range(1,c):
        if (c%i==0):
            p=p+1
    
    if (p==1):
        print(c)
        
    p=0
    c=c+1


# In[32]:


x=int(input("Enter a number: "))   #Find nth fibonacci number where n is entered by user
c=2
n=0
a=0
b=1

if (x==1):
    print("Fibonacci #",x,"= 0")

if (x==2):
    print("Fibonacci #",x,"= 1")

while (1>0):
    n=a+b
    a=b
    b=n
    c=c+1
    if (c==x):
        print("Fibonacci #",x,"=",n)
        break
    
    


# In[39]:


def func(x): 
    return x*x*x - 27

a=-100
b=200
bisection(a,b)

# Prints root of func(x) 
# with error of EPSILON 
def bisection(a,b): 
  
    if (func(a) * func(b) >= 0): 
        print("You have not assumed right a and b\n") 
        return
   
    c = a 
    while ((b-a) >= 0.01): 
  
        # Find middle point 
        c = (a+b)/2
   
        # Check if middle point is root 
        if (func(c) == 0.0): 
            break
   
        # Decide the side to repeat the steps 
        if (func(c)*func(a) < 0): 
            b = c 
        else: 
            a = c 
              
    print("The value of root is : ","%.4f"%c) 

