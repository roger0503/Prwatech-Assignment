import statistics

print("SCIENTIFIC CALCULATOR\n")

#Asking user for choice of operation
while True:
    choice = int(input('''Which operation are you willing to do? Press:
    1 for Addition
    2 for Subraction
    3 for Multiplication.
    4 for Division
    5 for And operation
    6 for Or operation
    7 for Nor operation.
    8 for Factorial
    9 for Fibonacci
    10 for Permutation
    11 for Integer reverse
    12 for Combination
    13 for Mean, median and mode
    14 for Dictionary, variance and standard deviation\n'''))

    #Function for Addition
    def addition(a,b):
        return a+b

    #Function for Subtraction
    def subtract(a,b):
        return a-b

    #Function for Multiplication
    def multiplication(a,b):
        return a*b

    #Function for Division
    def division(a,b):
        return a/b

    #Function for AND operation
    def and_oper(a,b):
        return a and b

    #Function for OR operation
    def or_oper(a,b):
        return a or b

    #Function for NOR operation
    def nor_oper(a,b):
        return int(not(a or b))

    #Function for factorial
    def factorial(n):
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

    #Function for Fibonacci
    def fibonacci(n):
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    #Function for Permutation
    def permutation(n,r):
        fact_n = 1
        fact_r = 1
        for i in range(1,n+1):
            fact_n *= i
        for j in range(1,(n-r)+1):
            fact_r *= j
        return fact_n/fact_r

    #Function for Integer Reverse
    def int_reverse(n):
        n1 = str(n)
        ans = n1[::-1]
        return int(ans)

    #Function for combination
    def combination(n,r):
        fact_n = 1
        fact_r = 1
        fact_of_r = 1
        for i in range(1,n+1):
            fact_n *= i
        for j in range(1,(n-r)+1):
            fact_r *= j
        for k in range(1,r+1):
            fact_of_r *= k
        return fact_n/(fact_of_r*fact_r)

    if(choice == 1):
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The addition of {a} and {b} is: {addition(a,b)}\n")

    elif(choice == 2):
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The subtraction of {a} from {b} is: {subtract(a,b)}\n")

    elif(choice == 3):
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The multiplication of {a} and {b} is: {multiplication(a,b)}\n")

    elif(choice == 4):
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The division of {a} from {b} is: {division(a,b)}\n")

    elif(choice == 5):
        a = int(input("Enter 0 or 1:"))
        b = int(input("Enter 0 or 1:"))
        print(f"{a} AND {b} = {and_oper(a,b)}\n")

    elif(choice == 6):
        a = int(input("Enter 0 or 1:"))
        b = int(input("Enter 0 or 1:"))
        print(f"{a} OR {b} = {or_oper(a,b)}")

    elif(choice == 7):
        a = int(input("Enter 0 or 1:"))
        b = int(input("Enter 0 or 1:"))
        print(f"{a} NOR {b} = {nor_oper(a,b)}\n")

    elif(choice == 8):
        a = int(input("Enter number: "))
        print(f"The Factorial of {a} is: {factorial(a)}\n")

    elif(choice == 9):
        a = int(input("Enter which number of fibonacci series you want:"))
        print(f"The {a}th number in fibonacci series is: {fibonacci(a)}\n")

    elif(choice == 10):
        a = int(input("Enter value of n: "))
        b = int(input("Enter value of r: "))
        print(f"{a}P{b} = {permutation(a,b)}\n")

    elif(choice == 11):
        a = int(input("Enter the number:"))
        print(f"The reverse of {a} is : {int_reverse(a)}\n")

    elif(choice == 12):
        a = int(input("Enter the value of n: "))
        b = int(input("Enter the value of r: "))
        print(f"{a}C{b} = {combination(a,b)}")
    
    elif(choice == 13):
        n = input("Enter elements of a list separated by space\n")
        l1 = n.split()
        for i in range(len(l1)):
            l1[i] = int(l1[i])
        print(f"The mean of numbers is : {statistics.mean(l1)}")
        print(f"The median of numbers is : {statistics.median(l1)}")
        print(f"The mode of numbers is : {statistics.mode(l1)}")
    
    elif(choice == 14):
        n = input("Enter elements of a list separated by space\n")
        l1 = n.split()
        for i in range(len(l1)):
            l1[i] = int(l1[i])
        print(f"The variance of entered numbers is : {statistics.variance(l1)}")
        print(f"The standard deviation of entered numbers is : {statistics.stdev(l1)}")
    
    else:
        print("Invalid choice")
    
    cont = str(input("Do you want to do more operations?(y/n)\n"))
    if(cont == 'y'):
        continue
    elif(cont == 'n'):
        break
    else:
        print("Invalid command")
        break