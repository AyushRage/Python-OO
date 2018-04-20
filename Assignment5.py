class Student:
    def __init__(self=1,studentid=1001,studentname="Addy",qualifyingexammarks=56.09, residentialstatus="H", yearofengg=3, branchname="CSE"):
        self.__studentid = studentid
        self.__studentname = studentname
        self.__qualifyingexammarks = qualifyingexammarks
        self.__residentialstatus = residentialstatus
        self.__yearofengg = yearofengg
        self.__branchname = branchname
        
        print("Student Id: ",self.__studentid)
        print("Student Name: ", self.__studentname)
        print("Qualifying Exam Marks: ", self.__qualifyingexammarks)
        print("Residential Status: ", self.__residentialstatus)
        print("Current Year of Engineering: ",self.__yearofengg)
        print("Branch Name: ",branchname)


'For Default - CASE 1'
#deets = Student() 

'CASE - 2'
deets=Student(15001,"Jack",125.5,"H",1,"Civil") 

