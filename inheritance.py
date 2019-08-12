#Inheritance

#parent class
class Parent():
	#class variables will go here
	def __init__(self,last_name,eye_color):
		#instance variables,those are inside the constructor ,__init__() function
		self.last_name =  last_name
		self.eye_color = eye_color
		print('Contructor of class Parent is initialized')

	def show(self):
		return self.eye_color

#Child class
class Child(Parent):
	def __init__(self,last_name,eye_color,age):
		print('Constructor of Child initialized')
		Parent.__init__(self,last_name,eye_color)
		self.age = age

bob = Parent('Marley','blue')
print(bob.last_name)
billy = Child('cyrus','brown',20)
print('my eye color is ',billy.show())
print(billy.age)


