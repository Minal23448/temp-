print ("hello")
H = int(input("ENTER THE HEIGHT: "))
W = int(input("ENTER THE WIDTH: "))
A = H*W

if H >= 0 and W >=0:
    print("Area of the rectangle is ",A)
else:
    print("INVALID INOUT")



 2. Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# a. Find out how many students are in the list
# b. Change Lisa’s favourite colour
# c. Remove 'Jenny' and her favourite colour

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
name=len(people)
print("all member in list num :",name)
people["Lisa"]="pink"
print("lisa new colour",people)
del people['Jenny']
print("all list ",people)

