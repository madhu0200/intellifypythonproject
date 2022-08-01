#reading dividend,divisor and num of digits in precision
def getquotient(dividend,divisor,decimal):
    
    #getting the decimal values with leading zero
    quotient=dividend/divisor-dividend//divisor

    #taking the required decimal places in quotient
    quotient='%.{}f'.format(decimal)% quotient

    #converting the quotient to string
    quotient=str(quotient)

    #taking the required decimal values
    quotient=quotient[2:decimal+2]
    print('{} decimal places for {}/{}:'.format(decimal,dividend,divisor), quotient)

    #dclaring empty dictionary
    dict2={}

    #for searching the values from 0 to 9 values in decimal
    for i in range(10):
        #updating the dictionary with key as i value(0-9) and values as count of i value in decimal
        dict2.update({i:quotient.count(str(i))})
    print(dict2)


getquotient(22,7,10)
getquotient(27, 5, 25)
getquotient(1,3,33)
getquotient (100, 25, 4)
    