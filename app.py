# List:
# number = [5, 6, 7, 8, 3]
# friends = ["a", "b", "c", "d", "creed"]
# friends.insert(1, "kelly")
# friends.remove("a")
# friends.clear()
# friends.pop()  # exclude the final element
# friends.index("d")
# friends.count("a")  # how many "a" here?
# friends.sort()  # in letter order
# friend2 = friends.copy()

# Tuple: cannot change the element inside described in (), but list in []
"""
coordinates = (4, 5)
print(coordinates[0])

inates = [4, 5]
inates[1] = 10

coordinates = [(4, 5), (6, 7)]
"""

# function
"""
def say_hi(name, age):
    print("hello " + name + ", you are " + str(age))


print("top")
say_hi("lynn", 35)
print("bottom")
"""

# return
"""
def cube(num):
    return num * num * num

result = cube(4)
print(result)
"""

# if else elif
"""
is_male = True
is_tall = True
if is_male and is_tall:  # can also use "and" here
    print("you are a tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are a tall nonmale")
else:
    print("you are a short nonmale")
"""

"""
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# if "dog" == "dog"
print(max_num(3, 4, 5))
"""

# dictionaries
"""
monthconversions = {
    "Jan": "January",
    "Feb": "February"

}  # left: keys which need to be unique
print(monthconversions["Jan"])
print(monthconversions.get("Jan", "Not a valid key"))  # right: default value
"""

# while
"""
i = 1
while i <= 10:
    print(i)
    i += 1
print ("done with lp")
"""

# for
"""
friends = ["a", "b", "c"]
for friend in friends:  # friend here is a new name decided by user
    print(friend)
for letter in "alex":  # for every letter in the word "alex"
    print(letter)
for letter1 in range(3):  # range(3) means 0 1 2
    print(letter1)
"""

# print(2 ** 3)  # it means 2^3

"""
def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result
"""

# 2D lists
"""
number_grid = [1, 2, 3, 4]
number_gris = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8, 9]
]

print(number_gris[0][0])  # the location of 1

for row in number_gris:
    for col in row:
        print(col)
 """

# translator
"""
def translate(phrase):
    translation = ""
    for letter in phrase:  # "Out"
        if letter in "AEIOUaeiou":  # letter.lower(): lower all the letter in the string. here change Out to out
            # here i can also change it into: if letter.upper() in "AEIOU"
            # or i can also change it into: if letter in "AEIOUaeiou"

            if letter.isupper():  # if letter is uppercase
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase")))
"""

# except

"""
try:
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError as error:  # 10/0
    print(error)
except ValueError:  # input: abc
    print("invalid input")
"""

# file
"""
open("employees.txt", "r")  # just read the file
open("employees.txt", "w")  # you can modify the file
employ_file.write("\nlynn-swe")   # it will overwrite
employ_file.write("<p> this is html</p>")
employ_file=open("employees.txt", "a")  # append information onto the end of the file
employ_file.write("\nlynn-swe") # add some contents in the file
open("employees.txt", "r+")  # you can read and write

employ_file = open("employees.txt", "r+")  # create another file to store the change
print(employ_file.read())  # tell me all the content of the file
print(employ_file.readline())  # read a line every time
print(employ_file.readlines())  # read all lines
employ_file.close()
"""

# class
"""
from student import student

# from student file import student class

student1 = student("Jim", "Business", "3.1")
student2 = student("alex", "math", "3.5")
print(student1.name)
"""

"""
from question import question  # take the class question from the file question

question_prompts = [
    "\nwhat color is alexander?\n(a)red\n(b)brown\n(c)yellow\n",
    "\nalexander hen da de\n(a)true\n(b)even bigger\n(c)this galaxy is too small for it\n"
]  # set up 2 questions, question_prompts is a list including two strings

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "a")
]  # set up the question answer, questions is a list including two classes, each class contains question and answer


def run_test(questions):
    score = 0
    for question in questions: # for every class question in questions
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct!")


run_test(questions)
"""

"""
in a class file, you can inherit another class
from chef import chef
class chinesechef(chef):
# in this way chinesechef inherited all functions in chef
"""
