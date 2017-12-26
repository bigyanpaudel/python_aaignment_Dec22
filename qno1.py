
# Program to generate & print a dictionary that contains a number (between 1 and n) in the form (x, x*x).



num = input("Enter the number: ")

dict1 = dict()



for i in range(1, num+1):

    dict1[i] = i*i



print(dict1)