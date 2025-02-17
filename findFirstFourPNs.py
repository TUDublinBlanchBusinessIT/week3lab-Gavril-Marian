#Gavril Marian
#17/02/2025
# A program that tests first four perfect numbers

from perfectNumber import perfectNumber
totalPfs=0
testNumber=1
while(totalPfs<=4):
    if (totalPfs == 4):
        break
    if(perfectNumber(testNumber) == True):
        print (f"{testNumber} is a perfect number")
        totalPfs+=1
    testNumber+=1
            



