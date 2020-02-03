#printing the value A and B which do not contain 4 in it from given number
keyin = int(input("Enter amount to pay, N = ")) #taking value from the user

key = str(keyin)    #converting integer into string for iteration perpose, because integer value can not be iterated
#initialisation of some variables
count = 1
co = 1
A = 0

#iteration to find the value of A
for i in key:
    if i == '4':    #checking the condition whether given number contains 4
        i = 3
    for  a in range(len(key)-count):    #calculating exponantial powers of numbers
        co = co * 10
    A = int(i)*co + A   #calculation of A which do not contain number 4
    count = count + 1   #incrementing counter
    co =  1     #reseting co to it's initial value 1
B = keyin - A   #calculation of B

#printing the value of A and b which do not contain number 4
print("The value of A = ", A)
print("The value of B = ", B)
