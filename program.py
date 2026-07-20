#1Write a program to identify if the character is a vowel or consonant
'''
l1=['a','e','i','o','u']
value=input()
if value in l1:
    print("vowel")
else:    
    print("consonant")
    '''       
    
#2Write a program to identify if the character is an alphabet or not
'''
isalpha() is a built-in string method in Python that checks whether all characters
 in a string are alphabets (letters).

print(ord('a'))# gives ASCII values of given character 
'''

'''
ch= input('enter an alphabet:')#takes input as string
if len(ch)==1 and (('a'<=ch<='z') or ('A'<=ch<='Z')):
    print("alphabet")
else:
    print("not alphabet")
    '''
#3Write a program to find number of digits in an integer
'''
num =int(input("enter number "))
num=[*f'{num}']
count=0
for i in num:
    count+=1
print(count)
'''    

#4pascal's triangle of n rows
'''
n=int(input("number:"))
for i in range(0,n):
    for k in range(i,n):
        print("",end=" ")
        c=1
    for j in range(0,i):
        print(c,end=" ")
        c=int(c*(i-j)/(j+1))
    print(c)
'''
  

'''
n=int(input("enter number:"))
cpr=n*2
for i in range(1,n+1):
    print(" "*cpr,*range(1,i+1),*range(i-1,0,-1))
    cpr-=2
'''
            
#5factorial of number
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


#6sum of digits factorial in a given number
'''
num=int(input("enter a number"))
if num<0:
    num=-num
sum=0
while num!=0:
    digit=num%10
    fact=1
    while digit!=0:
        fact=fact*digit
        digit-=1
    sum=sum+fact
    num=num//10
print(sum)
        
'''
#7strong number :-if sum of digits factorial is original number it is called strong number
'''
num=int(input("enter a number"))
n=num
if num<0:
    num=-num
sum=0
while num!=0:
    digit=num%10
    fact=1
    while digit!=0:
        fact=fact*digit
        digit-=1
    sum=sum+fact
    num=num//10
if n==sum:
    print("strong number")
else:
    print("not strong number")
'''

#8strong numbers in given range

'''
num1 =int(input("enter firts number:"))
num2=int(input("enter second number"))
for num in range(num1,num2+1):
    n=num
    sum=0
    while num!=0:
        digit=num%10
        fact=1
        while digit!=0:
            fact=fact*digit
            digit-=1
        sum=sum+fact
        num=num//10
    if n==sum:
        print(n)
'''    




#9fibonacci series

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

#10sum of digits
'''
num= int(input("enter a number:"))
sum=0
while num!=0:
    digit=num%10
    num=num//10
    sum+=digit
print(sum)    
    '''
#11sum of natural number
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
 #12 sum of numbers in the given range
''' 
first_num=int(input("enter first number:"))
last_num=int(input("enter last number:"))
sum=0  
for i in range(first_num,last_num+1):
    sum+=i
print(sum)

'''


#13 program to reverse a number
'''
num=int(input("enter a number:"))
temp=0
while num!=0:
    digit=num%10
    temp=(temp*10)+digit
    num=num//10
print(temp,end="")'''

#14 finding lcm of two numbers
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

#15 find gcd of two numbers
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
print(gcd)    
''' 

#16  finding a perfect number
#if a number sum of factors is equals to number then number is called perfect number
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
#17 perfect numbers between given range
'''
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
for num in range(num1,num2):
    sum=0
    for i in range(1,num+1):
        if num%i==0 and i!=num:
            sum+=i
    if sum==num:
        print(num)
'''    


#18 addition of two fractions
'''
num1=int(input("enter the first fracton numerator:"))
deno1=int(input("enter the first fracton denominator:"))
num2=int(input("enter the second fracton numerator:"))
deno2=int(input("enter the second fracton denominator:"))

fraction_num=(num1*deno2+num2*deno1)
fraction_deno=(deno1*deno2)
print("fraction_num/fraction_deno",fraction_num/fraction_deno)
print("fraction is: {}/{}".format(fraction_num,fraction_deno))'''

     
#19 checking armstrong number or not
#if a number digits power of len(number)==original number 

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


#20 armstrong number between two numbers
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
         
         
#21 check number is leap year or not
'''  
year=int(input("enter year:"))
if year%100==0 and year%400==0:
    print("leap year")
elif year%4==0:
    print("leap year")
else:
    print("normal year")
        '''
#22 check prime number or not
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
#23 palindrome or not
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
    
#24 prime numbers in given range
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

         
#25 express a number as sum of two prime numbers
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
                  print(i,num-i)
  '''                
#26 replace 0's with 1's in given integer
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

#27 pyramid pattern using stars
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
#28 pyramid pattern using numbers 
'''
rows= int(input("enter a number:"))
cpr=rows*2
for rownum in range(1,rows+1):
    print(" "*cpr,*range(1,rownum+1),*range(rownum-1,0,-1))
    cpr-=2'''
    
#29 total number of handshakes
#formula (n*(n-1))/2

#30in which quadrant coordinates lies
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
    
#31 no of times digit occured
'''
num=int(input("enter a number"))
if num<0:
    num=-num
l1=[*f'{num}']
l2=[]
while num!=0:
    digit=num%10
    num=num//10
    count=0
    if digit in l2:
        continue
    else:
        l2=l2+[digit]
        for i in l1:
           if i==f'{digit}':
               count+=1
        print("{0} occured {1} times".format(digit,count))
'''       
        
#write a python program to  print the all combinations of n-digit number

'''
num=int(input("enter a number:"))
if num<0:
    num=-num
max=0
min=9
l1=0
p=num
for _ in [*f"{num}"]:
    l1+=1
while num!=0:
    digit=num%10
    if max<digit:
        max=digit
    if min>digit:
        min=digit
    num=num//10
start=min*10**(l1-1)
end=max*10**(l1-1)
for i in range(start,end):
    if {*f'{i}'} == {*f'{p}'}:
        print(i)
 '''       

    

