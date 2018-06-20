#FUNCTIONS AND RECURSION IN PYTHON

#1.Create a function to calculate the area of a circle by taking radius from user.
rad = float(input("enter the radius:"))

def area_circle (r):
    res = (3.14*pow(r,2))
    print("the area of the circle is %0.2f"%(res) )
area_circle(rad)
print("\n")

#Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

#function to determine number is a perfect number
def perf_num (n):
    sum = 0
    for i in range (1,n):
        rem = n % i
        if( rem == 0 ):
            sum = sum +i
           
    if(sum == n):
        print("%d"%(n))

    else :
        return()
print("in the given range i.e between 1 to 1000 are:")
#loop to make use of function perf_num in given range
for j in range(1,1000) :
    
    perf_num(j)
print("\n")

#3.Print multiplication table of 12 using recursion

def multi_twelve( multiplicand, multiplier=1):
    if(multiplier <= 10):
        print(multiplicand ,"x", multiplier,"=", multiplicand * multiplier)
        multi_twelve(multiplicand,multiplier+1)
    else:
        return()
m = int(input("enter the multiplicand:"))
print("the multiplication table of %d is:"%(m))
(multi_twelve(m))  
print("\n")

#4. Write a function to calculate power of a number raised to other ( a^b ) using recursion.

a = int(input("enter a number:"))
b = int(input("enter the power:"))

def pwr ( num1 , num2):
    if(num2 !=0):
       return(num1*pow(num1,num2-1))

    else :
        return(1)
print("%d^%d is:"%(a,b))
print(pwr(a,b))
print("\n")

#5. Write a function to find factorial of a number but also store the factorials calculated in a dictionary

numx = int(input("enter a number:"))
f=0
def fact ( numbr ):
    if (numbr == 0):
        return(1)
    else :
        return(numbr*fact(numbr-1))
print("the factorial of the number %d is :"%(numx))
print(fact(numx))
          
