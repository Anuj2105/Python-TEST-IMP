#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# # ** What is 7 to the power of 4?**

# In[1]:


7**4


# # ** Split this string:**
# 
#     s = "Hi there Yogesh!"
#     
# **into a list. **

# In[3]:


s = "Hi there Yogesh!"


# In[4]:


s.split()


# # ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[5]:


planet = "Earth"
diameter = 12742


# In[6]:


'The diameter of {} is {} km'.format(planet,diameter)


# ** Given this nested list, use indexing to grab the word "hello" **

# In[5]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst [3][1][2][0]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[7]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',
                            {'target':[1,2,3,'hello']}]}]}


# In[9]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# #Tuple is immutable objects the lists are mutable.

# ###### * Create a function that grabs the email website domain from a string in the form: **
# 
# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com

# In[19]:


def fun1(email):
    return email.split('@')[1]


fun1('anujdubey1370@gmail.com')


# ##### ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[17]:


def findDog(input):
    return 'dog' in input.lower().split()

findDog('Is there a dog here?')


# #### ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[37]:


def count_dog(input):
    c=0
    for w in  input.lower().split():
        if w=='dog':
            c=c+1
    return c

count_dog('This dog runs faster than the other dog dude!')


# #### ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# 
# ['soup','salad']

# In[44]:


seq = ['soup','dog','salad','cat','great']

list (filter(lambda x:x[0]=='s',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases. **

# In[45]:


def abc(speed, birthday):
    if birthday:
        speed -= 5
    if speed <= 60:
        return "No Ticket"
    elif 61 <= speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"


# In[48]:


abc(81,True)


# In[49]:


abc(81,False)


# In[51]:


abc(65,True)


# ### Question
# Given a string print number num by extracting all the
# digits from the string as in string
# Print negative number if the first character in 
# string is '-'
# eg.
# -123abcd should return -123,abcd456-->456,fdhfh78dsd89--->7889,-56dssd78-->-5678

# In[52]:


def a(input):
    for b in input:
        if b =="-":
            print(b,end="")
        if (b.isnumeric()):
            print(b,end="")


# In[53]:


a('-123abcd ')


# In[54]:


a('abcd456 ')


# In[55]:


a('fdhfh78dsd89 ')


# In[56]:


a('-56dssd78')


# ### Que 2.
# WAP to check whether a number is palindrome or not on following 
# conditions.
# 1. take input number
# 2. add number and its reverse
# 3. check that number is palindrome or not,if not then sum and its reverse

# In[65]:


a=input("Enter number - ")
b=int(a[::-1])
c=str(int(a)+b)
while c!=c[::-1]:
    c=str(int(c)+int(c[::-1]))
    print("# number is ",c)
    print("Reverse number is",c[::-1])
    
    print("Palindrome is", )


# #### Write a python function to find and display the five 
# digit number in which the first digit is two more than 
# the second,the second digit is two more than the third,
# the fourth digit is two less than the third, and the 
# last digit is two more than
# the fourth.The sum of the third,fourth and fifth digits
# equals the first.The sum of all the digits is 19

# In[66]:


def find_digit():
    for x in range(9,0,-1):
        a=x
        b=x-2
        c=x-4
        d=x-6
        e=x-4
        if c+d+e==a:
            if a+b+c+d+e==19:
                return (str(a)+str(b)+str(c)+str(d)+str(e))
            print(find_five_digit())
    


# In[67]:


find_digit()


# In[ ]:




