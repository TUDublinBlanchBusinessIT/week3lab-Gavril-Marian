#Gavril Marian
#17/02/25
#A program that test the divisors

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder
def divisors(num):
    my_list=[]

    for i in range(1,num):
        if num % i == 0:
            my_list.append(i)

    return my_list

def main():
    print(divisors(30))
main()
    

    


#define the funciton header called divisors expecting one argument

    #set up an empty list to hold your result
 
    
    #loop i from 1 to the number you are checking (take care not to include the number itself)

        #if the remainder when dividing the number by i is equal to zero then i is a divisor so...

            #apend i to the list you set up

 
    #return the list


#to test the divisors function uncomment the following line it should give [1,2,3,5,6,10,15]
#print(divisors(30))
