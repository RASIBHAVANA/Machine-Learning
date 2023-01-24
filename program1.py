#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 1
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# (a) Sort the list and find the min and max age
# (b)Add the min age and the max age again to the list
# (c)Find the median age (one middle item or two middle items divided by two)
# (d)Find the average age (sum of all items divided by their number)
# (e)Find the range of the ages (max minus min)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #creation of  a list

# (a) Sort the list and find the min and max age
# sorting the list using sort and printing the sorted list.

ages.sort() #built-in sort
print(f" Given list: {ages}") #sorted list

print(f"maxage: {max(ages)}, minage: {min(ages)}") #min and max age

# (b)Add the min age and the max age again to the list

ages.extend([min(ages),max(ages)]) #add the max and min ages back to the list
print(f"Updated list: {ages}") #print the list after new additions

# (c)Find the median age (one middle item or two middle items divided by two)

middle = int(len(ages)/2) #find middle index in the list
print(middle)
if middle % 2 == 0:    #find if its even
    print(f"Median of ages: {int((ages[middle-1]  + ages[middle] )/ 2)}")
    
# (d)Find the average age (sum of all items divided by their number)

print(f"Average of ages: {sum(ages)/len(ages)}")

# (e)Find the range of the ages (max minus min)

print(f"Range of the ages: {max(ages) - min(ages)}")


    









