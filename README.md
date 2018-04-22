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
1. Importance of self
2. Usage of self for accessing class members
  
  
## Assignment 4: Using default parameters in Method

Objective: For one of the above given business scenario to use default parameters in __init__() method

Problem Description: To initialize the members of the class during object instantiation __init__() method is needed. By using default parameters in __init__() method we can initialize the members as per the requirement. Write a Python program for the class diagram given below:

|Student|
|---|
||
+displayheader(char c) : void
+displayheader(char c, int n) : void
+displayheader(string s) : void

Default parameters need to be assigned properly in such a way to get following output on the screen:

```
Annual Report – FY16
====================

****************************************************************
                    Rict Engineering College
****************************************************************
```

Summary of this assignment: In this assignment, you have learnt
1. Creating the method with default arguments
2. Invoking method which is having default arguments


## Assignment 8: Debugging using Python

Objective: To do a self-review on python programming level

Problem Description: What would be the output for the following programs? If there is an error in the program, analyze it, fix it and execute it. Also write the inference drawn from each code snippet.

#### Code 1
```
class Parent:
    
    def setnum(self, val):
        self.__num = val
        
    def getnum(self):
        return self.__num

    def display(self):
        print("Number : ", self.__num)

class Child(Parent):
    
    def setval(self, num):
        self.__val = num

    def getval(self):
        return self.__val

    def display(self,num,val):
        print("Value : ", self.__val)
        print("Number : ", self.__num)

child = Child()
child.setnum(10)
child.setval(20)
child.display()
```

#### Code 2
```
class Parent:

    def setnum(self, val):
        self.__num = val

    def getnum(self):
        return self.__num

    def display(self):
        print("Number : ", self.__num)

class Child(Parent):
    
    def setval(self, num):
        self.__val = num

    def getval(self):
        return self.__val

    def display(self):
        print("Value : ", self.__val)
        super().display()

child = Child()
child.setnum(10)
child.setval(20)
child.display()
```

#### Code 3
```
class StaticDemo:
    count = 10
    
    def __init__(self):
        StaticDemo.count = StaticDemo.count + 1

    @staticmethod
    def display():
        print(count)

s1 = StaticDemo()
s2 = StaticDemo()
s1.display()
```

#### Code 4
```
class Animal:
    
    @classmethod
    def testclassmethod(cls):
        print("Class Method in Animal class is invoked")

    def testinstancemethod(self):
        print("Instance Method in Animal class is invoked")

class Cat(Animal):
    
    @classmethod
    def testclassmethod(cls):
        print("Class Method in Cat class is invoked")
        
    def testinstancemethod(self):
        print("Instance Method in Cat class is invoked")
        
mycat = Cat()
myanimal = Animal()
myanimal = mycat
Animal.testclassmethod()
myanimal.testinstancemethod()
```

#### Code 5
```
class ClassA:
    def methodone(self):
        print("First method in Class A")

    def methodtwo(self):
        print("Second method in Class A")

    @staticmethod
    def methodthree():
        print("Third static method in Class A")

    @staticmethod
    def methodfour():
        print("Fourth static method in Class A")

class ClassB(ClassA):
    @staticmethod
    def methodone():
        print("First static method in Class B")

    def methodtwo(self):
        print("Second method in Class B")
        super().methodtwo()

        def methodthree(self):
            print("Third method in Class B")

        @staticmethod
        def methodfour():
            print("Fourth static method in Class B")
            super().methodfour()

b = ClassB()
b.methodone()
b.methodtwo()
b.methodthree()
b.methodfour()
```

