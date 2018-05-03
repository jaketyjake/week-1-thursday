#prime or not
number = int(input("Enter a number to see if it is prime: "))


    
if number < 4:
    print("It's prime!!!")
else:
    for divider in range(2, number):
        if number > 3 and number % divider != 0:
            print("It's prime!!!") 
            break
        else:   
            print("It's not...") 
            break    

        




        