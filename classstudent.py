class student():
        __marks = []
        def set_data(self,Name,Rollno,m1,m2,m3,m4,m5):
                student.__name = Name
                student.__rollno = Rollno
                student.__marks.append(m1)
                student.__marks.append(m2)
                student.__marks.append(m3)
                student.__marks.append(m4)
                student.__marks.append(m5)
        def display(self):
                print("*** STUDENT DETAILS ***")
                print("NAME:", student.__name)
                print("ROLL NO.", student.__rollno)
                print("PERCENTAGE:", self.total())
                
        def total(self):
                m = student.__marks
                n = m[0]+m[1]+m[2]+m[3]+m[4]
                s =n/5
                return s
        

Name = input("Enter the name of student",)
Roll_no = int(input("Enter the roll no."))
m1 = int(input("Enter the marks"))
m2 = int(input("Enter the marks"))
m3 = int(input("Enter the marks"))
m4 = int(input("Enter the marks"))
m5 = int(input("Enter the marks"))
s1 = student()
s1.set_data(Name,Roll_no,m1,m2,m3,m4,m5)
s1.display()
