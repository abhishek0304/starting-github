class Employee:
	 
	def __init__(self,Name,Desig,Sal):
		self.name = Name
		self.desig = Desig
		self.sal = Sal
		
	def display(self):
		print("NAME:",self.name,"  ","DESIGNATION:",self.desig,"   ","SALARY:",self.sal)
	
str1 = str(input("ENTER NAME:"))
str2 = str(input("ENTER DESIGNATION:"))
str3 = int(input("ENTER SALARY"))
obj1 = Employee(str1,str2,str3)
obj2 = Employee("Kandwal","Salesman2",5000)
obj3 = Employee("Yadav","Manager",15000)
obj1.display()
obj2.display()
obj3.display()

