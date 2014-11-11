class Animal():

	def __init__ (self,name,age):
		self.name = name
		self.age = age
		
	def sleep(self):
		print self.name + " of " + str(self.age) + " is sleeping"

	def eat(self,food):
		print self.name + " is eating: " + food

x = Animal("batata",1)
x.sleep()
x.eat("pizza")

