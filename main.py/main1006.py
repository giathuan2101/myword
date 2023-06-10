#a

#b
# agest = ages

# #c
# ls_a= [1,2,3]
# # print("max of the list: ", max(ls_a))
# max_age = num

# #d
# len_name = len(name[0]) #set flag: maximum lengthof name
# for name in names:
#     check = len(name)
#     if check>longest_name:
#         len_name=check
#         longest_name = name
# for i in range(len(name )):
#     print(i)
#     check = len(name[i]) #check length of each 
#     check = len(name)
#     if check>longest_name:
#         len_name=check
#         longest_name = name[i]
    
        
# print("The longest naem is: ", longest_name)
# print(names)




# Numpy 2D array
# Exercise 1
# nested_ls= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(nested_ls[0][2])
# arr_a = np.array(nested_ls)
# print("array a: \n", arr_a)
# print("1st row: ",arr_a[:, 0])

#Ex 1:
# a)Created an 8x8 array with ones on all the edges and zeros everywhere  else
# b) Created an 8x8 array of integers with a checkerboard pattern of ones and zeros
# c) Created an 8x8 array of random integers (0,99),
# make all the numbers not divisible by 3.
# d) split the matrix above into 4 solu

# a)Created an 8x8 array with ones on all the edges and zeros everywhere  else
import numpy as np
# from main3105 import check_a
# from itertools import chain

# Create an 8x8 array filled with zeros
arr = np.zeros((8, 8))

# Set ones on the edges
arr[0, :] = 1  # First row
arr[-1, :] = 1  # Last row
arr[:, 0] = 1  # First column
arr[:, -1] = 1  # Last column
# Print the resulting array
# print(arr)

# b)
import numpy as np

# Create an 8x8 array filled with zeros
arr = np.zeros((8, 8), dtype=int)

# Set the checkerboard pattern of ones and zeros
arr[1::2, ::2] = 1  # Odd rows, even columns
arr[::2, 1::2] = 1  # Even rows, odd columns

# Print the resulting array
# print(arr)

# c)
# C= np.random.randint()
c= np.random.randint(0, 100, (8, 8))
# print("1st C: ",C)
c[c%3==0]+=1
# print ("2nd c: \n", c)

# d)
D1 = c[:4,:4]
D2 = c[:4,4:]
D3 = c[4:,:4]
D4 = c[4:,4:]
# print(D4)
D = np.split(c, 2, axis=0)
E = [np.split(x, 2, axis=1) for x in D]
# F = [i for sub_list in E fpr i in subl_ist]

# Exercise 2
# a) Enter some new items (key, value) to the dictionary
# b) Print all items of the dictionary
# c) Find student who has max GPA
# d) Find student who has min GPA
# e) Find mean GPA of students
# Write a function to check the method=("get", "update", "deleete") user want to do with the student's name:
# f) Enter a student name, print his/her GPA (method="get")
# g) Enter a student name, a new GPA and update it (method="update")
# h) Enter a student name, remove him/her from the dictionary (method="delete")

# a) b)
dict_students = {}
    
dict_students["Bob"] = 7.5
dict_students["Bobb"] = 5.5
dict_students["Bobbb"] = 6.5
dict_students["Bobbbbb"] = 7.0
dict_students["Bobcccc"] = 8.5

# print(dict_students.values())
# for name, age in dict_students.items():
    # print(name)
    # print(age)

# c)
max_gpa = max(dict_students, key=dict_students.get)
# print("student with max gpa: ", max_gpa, " and gpa is: ", dict_students[max_gpa])


# d)
# Find the student with the minimum GPA
min_gpa = min(dict_students, key=dict_students.get)
min_gpa = dict_students[min_gpa]


# Print the student with the minimum GPA
# print(f"The student with the lowest GPA is {min_gpa} with a GPA of {min_gpa}.")


# Exercise 1
# Create a list of 20 random integers less than 100
# a) Find elements that are greater than 50
# b) Find elements that are greater than mean of list
# c) Create a list of even numbers from that list
# d) Re-arrange the list so that 1st half contains only even numbers and 2nd half contains only odd numbers
# e) Create a list of even index numbers from that list, a list of odd index numbers from that list
import random
ls_a = [random.randint(0,100) for _ in range(20)]
print(" list of 20 random integers: \n", ls_a)


# a)
ls_a_50 = [a for a in ls_a if a>50]
print("a) elements that are greater than 50: \n", ls_a_50)

# b)
mean_value = sum(ls_a)/len(ls_a)
print("mean value: ", mean_value)
ls_a_mean = [a for a in ls_a if a>mean_value]
print("b) elements that are greater than mean: \n ", ls_a_mean)

# c)
ls_a_even = [a for a in ls_a if a%2==0]
print("c) even numbers: \n", ls_a_even)

# d)
ls_a_arrange = ls_a_even + [a for a in ls_a if a%2!=0 ]
print("d) Re-arrange list: \n", ls_a_arrange)

# e)
ls_a_even_index = [ls_a[i] for i in range(len(ls_a)) if i%2==0]
print("e) even index number: \n", ls_a_even_index)
# add index Number

# Exercise 2
# Reuse the dictionary of (student, GPA) from previous exercise
# a) Print Distinction students who have GPA > 8.0
# b) Print Merit students who have GPA > 6.5 but <= 8.0
# c) Print Pass students who have GPA >= 4.0 but <= 6.5
# d) Print Failed student who have GPA < 4.0
# e) Print numbers of Distinction students, Merit students, Pass students and Failed students
# f) Print pass rate and check if it is greater than 70% then print successful semester

students = {
    'John': 9.2,
    'Alice': 7.8,
    'Bob': 5.5,
    'Emily': 8.9,
    'Tom': 3.2,
    'Sarah': 6.7,
    'Michael': 9.8,
    'Olivia': 4.1
}

# a) Print Distinction students who have GPA > 8.0
print("Distinction students:")
for student, gpa in students.items():
    if gpa > 8.0:
        print(student)

# b) Print Merit students who have GPA > 6.5 but <= 8.0
print("\nMerit students:")
for student, gpa in students.items():
    if 6.5 < gpa <= 8.0:
        print(student)

# c) Print Pass students who have GPA >= 4.0 but <= 6.5
print("\nPass students:")
for student, gpa in students.items():
    if 4.0 <= gpa <= 6.5:
        print(student)

# d) Print Failed students who have GPA < 4.0
print("\nFailed students:")
for student, gpa in students.items():
    if gpa < 4.0:
        print(student)

# e) Print the number of Distinction, Merit, Pass, and Failed students
distinction_count = 0
merit_count = 0
pass_count = 0
failed_count = 0

for gpa in students.values():
    if gpa > 8.0:
        distinction_count += 1
    elif 6.5 < gpa <= 8.0:
        merit_count += 1
    elif 4.0 <= gpa <= 6.5:
        pass_count += 1
    else:
        failed_count += 1

print("\nNumber of Distinction students:", distinction_count)
print("Number of Merit students:", merit_count)
print("Number of Pass students:", pass_count)
print("Number of Failed students:", failed_count)

# f) Calculate pass rate and check if it is greater than 70% then print successful semester
total_students = len(students)
pass_rate = (merit_count + pass_count + distinction_count) / total_students * 100

print("\nPass rate:", pass_rate, "%")
if pass_rate > 70:
    print("Successful semester!")
