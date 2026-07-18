#Write a program to identify if the character is a vowel or consonant
'''l1=['a','e','i','o','u']
value=input()
if value in l1:
    print("vowel")
else:    
    print("consonant") '''       
    
#Write a program to identify if the character is an alphabet or not
'''isalpha() is a built-in string method in Python that checks whether all characters
 in a string are alphabets (letters).'''
 
'''print(ord('a'))# gives ASCII values of given character 
ch= input('enter an alphabet:')
if len(ch)==1 and (('a'<=ch<='z') or ('A'<=ch<='Z')):
    print("alphabet")
else:
    print("not alphabet")'''
#Write a program to find number of digits in an integer
'''num =int(input("enter number "))
num=[*f'{num}']
count=0
for i in num:
    count+=1
print(count)'''    

#pascal's triangle of n rows
'''n=int(input("number:"))
for i in range(0,n):
    for k in range(i,n):
        print("",end=" ")
        c=1
    for j in range(0,i):
        print(c,end=" ")
        c=int(c*(i-j)/(j+1))
    print(c)'''
''''     
    or
n=int(input("enter number"))
cpr=n*2
for i in range(1,n+1):
    print(" "*cpr,*range(1,i+1),*range(i-1,0,-1))
    cpr-=2
'''
            
#factorial of number
'''
num= int(input("enter a number:"))
m=1
while(num>0):
    m=m*num
    num-=1
print(m)

'''
'''
m=1
for i in range(1,num+1):
    m=m*i
print(m)'''

#fibonacci series

'''
num= int(input("enter a number:"))
m=0
n=1
p=0
for i in range(1,num-1):
    p=m+n
    m=n
    n=p
print(p)'''

#sum of digits
'''
num= int(input("enter a number:"))
sum=0
while num!=0:
    digit=num%10
    num=num//10
    sum+=digit
print(sum)    
    '''
#sum of natural number
'''
num=int(input("enter the range:"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)   
      
      or


sum=(num*(num+1))//2
print(sum)

'''   
 #sum of numbers in the given range
''' 
first_num=int(input("enter first number:"))
last_num=int(input("enter last number:"))
sum=0  
for i in range(first_num,last_num+1):
    sum+=i
print(sum)'''


#program to reverse a number
'''
num=int(input("enter a number:"))
temp=0
while num!=0:
    digit=num%10
    temp=(temp*10)+digit
    num=num//10
print(temp,end="")'''

#finding lcm of two numbers
'''
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if num1>num2:
        min_num=num2
else:
        min_num=num1
while (1):
    if min_num%num1==0 and min_num%num2==0:
        print("lcm is ",min_num)
        break
    min_num+=1
'''


# finding a strong number

'''
num=int(input("enter a number:"))
sum=0
p=num
while num!=0:
    digit=num%10
    n=1
    for i in range(1,digit+1):
        n=n*i  
    sum+=n   
    num=num//10
if sum==p:
        print("strong number")
else:
        print("not strong number")
   ''' 

# finding a perfect number
'''
num=int(input("enter a number:"))
sum=0
for i in range(1,num+1):
    if num%i==0 and i!=num:
        sum+=i
if sum==num:
    print("perfect number")
else:
    print("not perfect number")
'''

#addition of two fractions
'''
num1=int(input("enter the first fracton numerator:"))
deno1=int(input("enter the first fracton denominator:"))
num2=int(input("enter the second fracton numerator:"))
deno2=int(input("enter the second fracton denominator:"))

fraction_num=(num1*deno2+num2*deno1)
fraction_deno=(deno1*deno2)
print("fraction_num/fraction_deno",fraction_num/fraction_deno)
print("fraction is: {}/{}".format(fraction_num,fraction_deno))'''


#find gcd of two numbers
'''
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
gcd=1
if num1>num2:
    max_num=num1
else:
    max_num=num2
for i in range(1,max_num):
    if num1%i==0 and num2%i==0:
     gcd=gcd*i
     max_num-=1
print(gcd)    
 '''       
#checking armstrong number or not
'''
num=int(input("enter a number:"))
p=[*f'{num}']
count=0
sum=0
n=num
for i in p:
    count+=1
while num!=0:
    digit=num%10
    sum+=digit**count
    num=num//10
if sum==n:
    print("Armstrong Number")
else:
    print("not armstrong number")

'''
#check number is leap year or not
'''  
year=int(input("enter year:"))
if year%100==0 and year%400==0:
    print("leap year")
elif year%4==0:
    print("leap year")
else:
    print("normal year")
        '''
#check prime number or not
'''
num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
   print("prime number ") 
else:
   print("not prime number")     
 '''   
#palindrome or not
'''
num=int(input("enter number:"))
p=num
reverse_num=0
while num!=0:
    digit=num%10
    reverse_num=(reverse_num*10)+digit
    num=num//10
if p==reverse_num:
    print("palindrome")
else:
    print("not palinddrome")'''
    
#prime numbers in given range
''' 
num1=int(input("enter start number:"))
num2=int(input("enter last range:"))
k=0
for i in range(num1,num2+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
           count+=1
    if count==2:
        print(i)
        k+=1
print("total number of primenumbers",k)
        '''
#armstring number between two numbers
'''
num1 =int(input("enter firts number:"))
num2=int(input("enter second number"))
for i in range(num1,num2+1):
    p=i
    l=[*f"{i}"]
    x=len(l)
    sum=0
    while i!=0:
         digit=i%10
         sum+=digit**x
         i=i//10
    if sum==p:
        print(p)
         '''
         
#express a number as sum of two prime numbers
'''
num=int(input("enter a number:"))

for i in range(1,num+1):
    count=0
    n=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2 and i!=1:
        for k in range(1,num-i+1):
            if (num-i)%k==0:
                    n+=1
        if n==2:
                  print(i,num-i)'''
                  
#replace 0's with 1's in given integer
'''
num=int(input("enter a number:"))
n=0
i=0
while num!=0:
    digit=num%10
    if digit==0:
        n=n+1*10**i
        num=num//10
        i+=1
    else:
        n=n+digit*10**i
        num=num//10
        i+=1
print(n)'''

# pyramid pattern using stars
'''
rows=int(input("enter number of rows:"))
cpr=rows*2
for rownum in range(1,rows+1):
    print(" "*cpr,end=" ")
    for i in range(1,rownum+1):
       print("*",end=" ")
    for i in range(rownum-1,0,-1):
       print("*",end=" ")
    print()
    cpr-=2'''
# pyramid pattern using numbers 
'''
rows= int(input("enter a number:"))
cpr=rows*2
for rownum in range(1,rows+1):
    print(" "*cpr,*range(1,rownum+1),*range(rownum-1,0,-1))
    cpr-=2'''
    
# total number of handshakes
#formula (n*(n-1))/2

#in which quadrant coordinates lies
'''
num1=int(input("enter first quadrant:"))
num2=int(input("enter second quadrant:"))
if num1>0 and num2>0:
    print(" firts quadrant")
if num1<0 and num2>0:
    print("quadrant2")
if num1<0 and num2<0:
    print("quadrant3")
if num1>0 and num2<0:
    print("quadrant4")'''
    
    

