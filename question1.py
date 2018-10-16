'''
Take in users age and multiply the users age by 5 before and after user input
'''

userAge = input("Please enter your age")

print(userAge)

def ageMultiplier(userAge):
   print(int(userAge)*5)


ageMultiplier(userAge)


# User can only enter an age of 10 so that the age multiplier can return back a value of 50
def test_answer(userAge):
    assert ageMultiplier(userAge) == 50

y =int(input("Enter the value of y"))
c =int(input("Enter the value of c"))


def equation(y,c):
   x =(2*y)+c
   print(x)

equation(y,c)


Summary 
#Runtime Error
#Logic Error
#Syntax Error

Varible types