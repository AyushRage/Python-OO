# Python-OO
Object Oriented Python 

## Assignment 1 : Identify OO Concepts

Objective: Read the above given business scenario to understand and identify OO concepts

Problem Description: Identify the OO concepts applicable for these scenarios:
1. More than 100 faculty members are working in the college to teach various engineering subjects. Every faculty has some attributes and perform some activities. How can these attributes and activities be represented using OO concepts?
2. Student can choose either to be a Day Scholar or a hosteller. If he is a Day Scholar, Transportation fees is applicable according to the travel distance. If he is staying hostel, hostel fee and mess fee are applicable. Identify the OO Concepts used here and write the appropriate class names to implement this scenario.
3. Accountant collects the fees to be paid from all the students irrespective of type of student. But, the formula used to calculate the fees depends on the student type. Which OO concept is used here?
4. Certain attributes of the student need to be accessed by the accountant and some attributes need not be. How can bring this feature into the system and what is the OO concept used for that?

Summary of this assignment: In this assignment, you have learnt object oriented concepts using scenarios


## Assignment 2 : Create class and objects in Python

Objective: Read the above given business scenario to create student class and to create objects for that class

Problem Description: Write a Python program for the class diagram given below:

|Student|
|---|
-studentid : int
-qualifyingexammarks : float
-residentialstatus : char
-yearofengg : int
+setstudentid(int) : void
+setqualifyingexammarks(float) : void
+setresidentialstatus(char) : void
+setyearofengg(int) : void
+getstudentid() : int
+getqualifyingexammarks() : float
+getresidentialstatus(): char
+getyearofengg() : int

Step 1: Create Student.py as per the class diagram
Step 2: Define all setter and getter methods
Step 3: Create a reference for student class with the name of objstu
Step 4: Invoke the corresponding setter methods using objstu and set following values to object
Step 5: Invoke the corresponding getter method to display the student details as given below:
  Student Id :
  Qualifying Marks :
  Residential Status :
  Current Year of Engineering :
  
Summary of this assignment: In this assignment, you have learnt
1. How to create a class, instantiate object
2. Invoking methods using object
3. Execute a Python program


## Assignment 3 : Debugging – self reference

Objective: Understand the importance of self reference to access the object members.

Problem Description:  Debug the below given Python code to give the output, shown after the code.

#### Code
```
class Registration:
    def setregistrationid (self, rid):
        __registrationid = rid
    
    def getregistrationid (self):
        return __registrationid

objreg = Registration()
objreg.setregistrationid(1001)
print("Registration Id : ", objreg.getregistrationid())
```

Output Expected:
  Registration Id : 1001
  
Summary of this assignment: In this assignment, you have learnt
  Importance of self
  Usage of self for accessing class members
  
  
## Assignment 4: Using default parameters in Method

Objective: For one of the above given business scenario to use default parameters in __init__() method

Problem Description: To initialize the members of the class during object instantiation __init__() method is needed. By using default parameters in __init__() method we can initialize the members as per the requirement. Write a Python program for the class diagram given below:

|Student|
|---|
+displayheader(char c) : void
+displayheader(char c, int n) : void
+displayheader(string s) : void
