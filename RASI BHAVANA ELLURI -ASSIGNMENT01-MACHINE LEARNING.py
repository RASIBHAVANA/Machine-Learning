#!/usr/bin/env python
# coding: utf-8

# # Question01

# In[1]:


# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# • Sort the list and find the min and max age
# • Add the min age and the max age again to the list
# • Find the median age (one middle item or two middle items divided by two)
# • Find the average age (sum of all items divided by their number)
# • Find the range of the ages (max minus min)

#creating a list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


# In[2]:


ages.sort() #built-in sort
print(f" Given list: {ages}") #sorted list


# In[3]:


print(f"max age: {max(ages)}, min age: {min(ages)}") #min and max age


# In[4]:


ages.extend([min(ages),max(ages)]) #add the max and min ages back to the list
print(f"New list: {ages}") #print the list after new additions


# In[5]:


#median
middle = int(len(ages)/2) #find middle index in the list
print(middle)
if middle % 2 == 0:    #find if its even
    print(f"The median of ages: {int((ages[middle-1]  + ages[middle] )/ 2)}")


# In[6]:


#average age
print(f"The average of ages: {sum(ages)/len(ages)}")


# In[7]:


#range
print(f"Range of the ages: {max(ages) - min(ages)}")


# # Question2

# In[8]:


# program2
# (a)Create an empty dictionary called dog
# (b) Add name, color, breed, legs, age to the dog dictionary
# (c) Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
#     (d) Get the length of the student dictionary
# (e) Get the value of skills and check the data type, it should be a list
# (f) Modify the skills values by adding one or two skills
# (g)Get the dictionary keys as a list
# (h)Get the dictionary values as a list

#empty dictionary with name dog
dog = {}


# In[9]:


#adding key value pairs to the dog dictionary
dog = {'name':'Max', 'color':'white black', 'breed':'husky', 'legs':'4', 'age':'6'}


# In[11]:


#student dictionary
student = {'first_name':'Bhavya', 'last_name': 'Elluri', 'gender':'female', 'age': '25', 'marital_status':'single',
           'skills':['coding'], 'country': 'India', 'city':'Narasaraopet', 'address':'8217'}


# In[12]:


#length of student dictionary
print(f"length of the  student dictionary: {len(student)}")


# In[13]:


#getting value of skills and checking datatype
print(type(student['skills']))


# In[14]:


#modifying skills
student['skills'].extend(['Eating', 'reading','Sleeping'])
print(student['skills'])


# In[15]:


#printing keys and values
print(f"keys of student dictionary:{student.keys()}")
print(f"values of student dictionary: {student.values()}")


# # Question3

# In[30]:


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are
# fine)
# • Join brothers and sisters tuples and assign it to siblings
# • How many siblings do you have?
# • Modify the siblings tuple and add the name of your father and mother and assign it to
# family_members


#sister and brother tuple
sister = ('Ramya', 'Bhavya', 'Divya', 'Bhargavi', 'Namaratha')
brother = ('Hemal', 'Sai', 'Haryanth', 'Lucky', 'Pavan')
#join brothers and sisters tuples and assign it to siblings
siblings = sister + brother
#count of siblings
print("Number of siblings: ",len(siblings))
#modify tuple with father and mother
father_mother = ("Peddi","Padmavathi")
siblings =siblings + father_mother

family_members = siblings
print(family_members)


# # Question4

# In[34]:


# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# • Find the length of the set it_companies
# • Add 'Twitter' to it_companies
# • Insert multiple IT companies at once to the set it_companies
# • Remove one of the companies from the set it_companies
# • What is the difference between remove and discard
# • Join A and B
# • Find A intersection B
# • Is A subset of B
# • Are A and B disjoint sets
# • Join A with B and B with A
# • What is the symmetric difference between A and B
# • Delete the sets completely
# • Convert the ages to a set and compare the length of the list and the set.



it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(f"length of IT compaines: {len(it_companies)}")

#add twitter
it_companies.add('Twitter')
print(f"add Twitter: {it_companies}")

#multiple IT companies
it_companies.update(['TCS', 'accenture', 'Honeywell'])
print(f"updated IT companies:{it_companies}")

#remove
it_companies.remove('accenture')
print(f"remove a company:{it_companies}")

#discard
it_companies.discard('TCS')
print(f"discard a company:{it_companies}")

#remove() raises key error if element is not found whereas
#discard doesn't raise an error


#join A and B
print(f"join A AND B:{A | B}")

#intersection of A and B
print(f"intersection A AND B:{A & B}")

#subset
print(f"if A is subset of B:{A.issubset(B)}")

#Are A and B disjoint sets
print(f"if disjoint set:{A.isdisjoint(B)}") #disjoint means no elements in common

# • Join A with B and B with A
A.update(B)
print(A)

B.update(A)
print(B)

#symmetric difference
print(f"symmetric difference:{A.symmetric_difference(B)}")

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f"symmetric difference of initial set: a  {A.symmetric_difference(B)}")


#delete set
A.clear()
B.clear()

#Convert the ages to a set and compare the length of the list and the set.
print(f"The length of the list age:{len(age)}")

age = set(age)
print(f"The length of the set age:{len(age)}")


# # Question5

# In[35]:


# The radius of a circle is 30 meters.
# • Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
# • Calculate the circumference of a circle and assign the value to a variable name of
# _circum_of_circle_
# • Take radius as user input and calculate the area

import math

#declaring radius
radius = 30

#calculate area
_area_of_circle = math.pi * radius * radius
print(f"The area of circle with radius 30 is {round(_area_of_circle,2)}")

#circumference of a circle
_circum_of_circle_ = 2 * math.pi * radius
print(f"The circumference of circle with radius 30 is {round(_circum_of_circle_,2)}")

#taking radius as user input
r = float(input("enter radius of your choice:"))
print(f"The area of circle with radius {r} is {round(math.pi * r * r,2)}")


# # Question6

# In[36]:



# “I am a teacher and I love to inspire and teach people”
# • How many unique words have been used in the sentence? Use the split methods and set
# to get the unique words.

string = "I am a teacher and I love to inspire and teach people"
list = string.split(' ')
print(list)

unique_count = len(set(list))
print(f"number of unique words in the given string is:{unique_count}")


# # Question7

# In[42]:


# Use a tab escape sequence to get the following lines.
# Name Age Country City
# Asabeneh 250 Finland Helsinki

print("Name \t\t Age \t Country \t City")
print("Asabeneh \t 250 \t Finland \t Helsinki")


# # Question8

# In[38]:


# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# “The area of a circle with radius 10 is 314 meters square.”

radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")


# # Question9

# In[39]:


# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
# Ex: L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]

#list of students weights
in_lbs =  [150, 155, 145, 148, 120, 130, 100]

in_kgs = []
#converting weight to kgs
for x in in_lbs:
    in_kgs.append(round(x * 0.45359237,2))

print(f"weight in kgs: {in_kgs}")


# # Question10

# In[44]:


feature = [1,2,3,6,6,7,10,11]
classes = [0,0,1,1,1,0,0,0]


# In[45]:


mid = len(feature)//2
train_feature, train_label = feature[0:mid],classes[0:mid]
test_feature, test_label = feature[mid:],classes[mid:]


# In[46]:


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


# In[47]:


model = KNeighborsClassifier(n_neighbors=3)

train_feature = np.array(train_feature).reshape((-1,1))
model.fit(train_feature,train_label)

test_feature = np.array(test_feature).reshape((-1,1))
predicted = model.predict(test_feature)


# In[48]:


print("Confusion Matrix : \n",confusion_matrix(predicted,test_label))
cnf_matrix = confusion_matrix(predicted,test_label)

TP = cnf_matrix[0][0]
TN = cnf_matrix[1][1]

FP = cnf_matrix[0][1]
FN = cnf_matrix[1][0]


# In[49]:


accuracy = (TP + TN)/(TP+TN+FP+FN)
print("Accuray : ",accuracy) 

sensitivity = TP/(TP + FN)
print("Sensitivity : ",sensitivity) 

Specificity = TN/(TN+FP)
print("Specificity : ",Specificity) 

