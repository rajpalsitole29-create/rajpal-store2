#pyhton program to create a simple calculater
#3 steps to build calculater program
#1. function for operation 
#2.user input
#3.print result


#step-1:create function:
#funcction to sum number
def addition(num1,num2):
    return(num1+num2)

#function to subtract number
def substraction(num1,num2):
    return(num1-num2)

#function to multiply number
def multiplication(num1,num2):
    return(num1*num2)

#function to divide number
def division(num1,num2):
    return(num1/num2)


#function to avg number
def average(num1,num2):
    return(num1+num2)/2


#step2: user input
print("please select a operation :\n" \
    "1. addition\n"\
    "2. subtraction\n"\
    "3. multiplication\n"\
    "4. division\n"\
    "5.average\n" )

select = int(input("select a operation from 1,2,3,4,5: "))

number1 = int(input("inter first inter number:"))
number2 = int(input("enter second inter number:"))

#step3 print the result

if select == 1:
    print(number1,"+",number2, "=",\
          addition(number1,number2))

elif select == 2:
    print(number1,"-",number2,"=",\
          substraction(number1,number2))

elif select == 3:
    print(number1,"*",number2, "=",\
          multiplication(number1,number2))

elif select == 4:
    print(number1,"/",number2, "=",\
          division(number1,number2))

elif select == 5:
    print((number1,"+",number2),"/","2" "=",\
          average(number1,number2))

else :
    ("invalid number! please try again")





    


