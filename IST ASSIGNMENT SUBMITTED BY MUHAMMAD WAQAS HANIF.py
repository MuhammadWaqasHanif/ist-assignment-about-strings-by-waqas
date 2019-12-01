#!/usr/bin/env python
# coding: utf-8

# In[1]:


x= "Muhammad Waqas Hanif"
dir(x)


# In[6]:


x = "Muhammad Waqas Hanif"           # change ist character of string to uppercase
print(x.capitalize())


# In[7]:


x= "Muhammad Waqas Hanif"               # Here all characters of string are lowercased 
print(x.casefold())


# In[9]:


x ="Muhammad Waqas Hanif"              #it is used to give spaces of 60(number of spaces) half before string and half after string, if in "" something written than it print that character on those spaces 
print(x.center(60,"f"))


# In[10]:


x = "Muhammad Waqas Hanif"            #it is used to  print the number of m how many times in string and return integer value
print(x.count("m"))


# In[11]:


x= "Muhammad Waqas Hanif"            #this method returns an encoded version of the string
print(x.encode())


# In[12]:


x= "Muhammad Waqas Hanif"          #it will retuen true or false if the string ends with the charcter in "_"
print(x.endswith("m"))


# In[13]:


x='Muha\tmmad Waq\qas'
print(x.expandtabs(2))


# In[14]:


a='wa\qas'
b=a.expandtabs(5)                  #Sets the tab size of the string
print(b)


# In[15]:


x= "Muhammad Waqas Hanif"         # returns true if all characters of string are alphabets
print(x.isalpha())


# In[16]:


y="Muhammad Waqas Hanif"
z=y.isalpha()                #Returns True if all characters in the string are in the alphabet
print(z)


# In[17]:


x = "Muhammad Waqas Hanif"       #return false if the string is not lowercase
print(x.islower())


# In[18]:


x= "my name is Muhammad Waqas Hanif and i study in UET"  #it will search the string and return the specified position of the string to find 
print(x.find('and'))


# In[19]:


x= "Muhammad Waqas Hanif"  #return false if string is not alphanumeric. space is consider as false. if no space between string than it returns true
print(x.isalnum())


# In[20]:


x = "Muhammad Waqas Hanif"     # it will return true if string is alphanumeric 
print(x.isalnum())


# In[21]:


y="Muhammad Waqas Hanif"
z=y.isalpha()                #Returns True if all characters in the string are in the alphabet
print(z)


# In[22]:


x = "Muhammad Waqas Hanif"  
print(x.islower())


# In[48]:


x= "132453"             #return true if string has  numeric values
print(x.isnumeric())


# In[24]:


x= "122111" 
y= "muhammad"          #it will return true if string is digit 
print(x.isdigit())      # it willl return false if string is not digits
print(y.isdigit())


# In[25]:


x= "Muhammad Waqas Hanif"  #if some string without spaces than it will return false
print(x.isspace())


# In[42]:


x= "  "              # if spaces are given as string it will give true 
print(x.isspace())


# In[27]:


x= "Muhammad Waqas Hanif"         #it will return true if the string follows the title format
print(x.istitle())


# In[28]:


x= "Muhammad Waqas Hanif"            # it is used for converion to lowercase 
y=x.lower()
print(y)


# In[29]:


x= "welcome to piaic "          #  it converts string to uppercase
print(x.upper())


# In[30]:


x = "chair , pencil , card"         # it is used to split the strings with comma after each value
print(x.rsplit(',') )


# In[31]:


a = ("muhammad", "Waqas")            #it is used to join the strings
print(".".join(a))


# In[32]:


a = "we are pakistani"                              #partition example  
b = a.partition("are")
print(b)
('we ', 'are', ' pakistani')


# In[47]:


x= "Muhammad Waqas Hanif"      # it will change upper to lowercase and vice versa
y=x.swapcase()
print(y)


# In[34]:


x = "Welcome to PIAIC,\n where you can learn"      # it will splitlines
print(x.splitlines())
['Welcome to PIAIC,', ' where you can learn']


# In[35]:


x= "Muhammad Waqas Hanif"
print(x)                           # it removes the spaces at starting of the string if given when storing values
print(x.lstrip())


# In[36]:


w = "Muhammad Waqas Hanif"                          # it will give 30 character spaces for left justified
print(w.ljust(30),"my fist name")


# In[43]:


x= "i told to my friend to bring me some new books"
print(x.index("friend"))


# In[44]:


x= "i am student of UET"  # varibale[start:end:step] according to these values steps will print
print(x)
print(x[::])
print(x[8:12:])    #it will print +1 charactaer starting value and -1 from end value is S printed
print(x[::-1])


# In[39]:


x= "my name was Muhammad Waqas Hanif"         # it replaces the word.
print(x.replace('was','is'))


# In[45]:


x= "Muhammad Waqas Hanif"       # it will cover 25 characters from right side and add zeros to left of first string character
print (x.zfill(25))


# In[49]:


y = "this is a example of  string....really!!!"         # it will print the highest character in string
print ("Max character: " + max(y))


# In[ ]:





# In[ ]:




