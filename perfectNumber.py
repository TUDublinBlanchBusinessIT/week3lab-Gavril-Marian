# Gavril Marian
#17/02/2025
# A program that checks if number is a perfect number
from divisors import divisors
def perfectNumber(number):

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
#The function should return True if the number is perfect and False if it is not

#from divisors import divisors


#define the function header called perfectNumber expecting one argument


    #set a result variable to False by default
    perfectNumber=False

    #if the sum of all the divisors of the number is equal to the test number
    my_list=[]
    my_list=divisors(number)
    sum=0
    for i in range(len(my_list)):
        sum=sum+my_list[i]
    if (sum == number):
        perfectNumber = True
    return perfectNumber
    


def main():
    if (perfectNumber(8128)):
        print("8128 is a perfect number")
main()

