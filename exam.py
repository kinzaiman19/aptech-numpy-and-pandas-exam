# /////////////////////////tasks/////////////////////////////////////............((((((((((TASKS)))))))))))........................?///////////////////////////////////////////


import numpy as np

# # create an 1d ,2d 3d array of given values....
# array1d=np.arange(1,16)
# print(array1d)
# # /////////// no 2////////
# array_2d=np.arange(1,17)
# array2=array_2d.reshape(2,8)
# print(array2)
# # //////////no 3/////
# array_3d=np.arange(1,25)
# array_3=array_3d.reshape(2,2,6)
# print(array_3)

# # ///////////create an  array and print its shape ,size and data type

# array_2d=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print("array 2d")
# print(array_2d)
# print("shape of array", array_2d .shape)
# print("datatype of array", array_2d .dtype)
# print(" dimension of array", array_2d .size)


# # //create an array of float and covert it to integers//

# array1d=np.array([1.2,3.4,4.5,2,8])
# array_1d=array1d.astype(int)
# print(array_1d)

# # /////////create 2 array of size 5 and perform multi add , sub////


# array2d_1 = np.array([[1,2,3],[4,5,6]])
# array2d_2 = np.array([[7,8,9],[10,11,12]])

# array_result = array2d_1 + array2d_2
# multi_array = array2d_1 * array2d_2
# sub_array = array2d_1 - array2d_2
# print(" add the array of",array_result)
# print("multiply the array of",multi_array)
# print("subtract the array of ",sub_array)


# # ///////// task no 6............../////////

# array_3d=np.ones((2,3,4))
# print(array_3d)

# array_3d=np.zeros((2,3,4))
# print(array_3d)

# array_3d=np.empty((2,3,4))
# print(array_3d)
# # ////////////////...............TASK NO 7............../////////////////

# array=np.arange(1,50)
# print(array)
# sort_array=np.sort(array[array>15])
# print(sort_array)

# # //////////..........TASK NO 4.....////////

# array_2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(array_2d[1,3])
# print("row",array_2d[1])
# print("column",array_2d[:,2])


# # //////////////.....TASK NO 8...///////////////

# original_array= ([1,2,3,4,5])
# deep_copy=original_array.copy()
# deep_copy[3]=15
# print(original_array)
# print(deep_copy)

# #////////........TASK NO 9.........////////////

# array=np.array([5,9,3,2,7])
# print(array)
# sort_array=np.sort(array)
# print(sort_array)
# sort_desc=sort_array[::-1]
# print(sort_desc)

# # ////////////.....TASK NO ...10........///////////////////
# array=np.arange(1,17,1)
# print(array)
# array2=array.reshape(4,4)
# print(array2)
# print(array2[0:2] ,array2[0:2,0:2])


# # /////////////.......TASK NO 11.......////////////////
# import random
# # Generate an array of 10 random integers between 1 and 20
# random_integers = [random.randint(1, 20) for _ in range(10)]

# # Filter out the even numbers
# Even_numbers = [num for num in random_integers if num % 2 != 1]

# print("Random integers:", random_integers)
# print("Even numbers:", Even_numbers)

# # ////////////////////////...TASK NO .12....////////////////////

# array = np.array([1, 4, 9, 16, 25])
# sqrt_array = np.sqrt(array)
# exp_array = np.exp(array)
# print("Original Array:", array)
# print("Square Root of Each Element:", sqrt_array)
# print("Exponentiation  of Each Element:", exp_array)

# # //////////......  ///  TASK NO 13  ///...........///////

# arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr1)
# arr2=np.array([[2,5,6],[7,9,0],[2,6,8]])
# print(arr2)
# print("multi",np.dot(arr2,arr1))
# multiarray=arr2*arr1

# # /////////////////////////// ..... TASK NO    14   .........////////////
# array1d =np.arange(1,100)
# array1=array1d[(array1d % 3 == 0)&(array1d % 5 == 0)]
# print(array1)

# # # ////////////////////// .....................PANDAS TEST...............///////////////

# import pandas as pd 


# # # /////////////........1st TASK...... ////////////////
# data={
#     'maths':95,
#     'english':74,
#     'science':89,
#     'history':75,
# }
# marks=pd.Series(data)
# print(marks['science'])
# marks['history'] = 80
# print(marks)


# ////////////////// 2nd TASK.....///////////

# data ={
#     'name':['alice','jason','david','max','stiphen','lord'],
#     'age':[22,34,12,45,21,20],
#     'city':['england','australia','UK','USA','canada','france'],
# }  
# employee=pd.DataFrame(data)
# print(employee)
# age=employee[employee['age']>25]
# print(age)
# df = pd.DataFrame(data)
# df['Profession']='Employee'
# print(df)

# ///////////////....... 3rd task..............

# student_details = {
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#     "Roll Number": [101, 102, 103, 104, 105],
#     "Class": ["10th", "9th", "10th", "8th", "9th"]
# }
# df_student = pd.DataFrame(student_details)
# marks_details = {
#     "Roll Number": [101, 102, 103, 104, 105],
#     "Marks": [85, 90, 78, 88, 92]
# }
# df_marks = pd.DataFrame(marks_details)
# final_df = pd.merge(df_student, df_marks, on="Roll Number")
# print(final_df)


