import random


class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None
	# getters
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	# setters
	def set_age(self, newage):
		self.age = newage
	def set_name(self, newname=""):
		self.name = newname
	def __str__(self):
		return "animal:" + str(self.name) + ":" + str(self.age)

# a = Animal(3)

# a.set_name()
# print(a.get_name())

# a.set_name("fluffy")
# print(a.get_name())

class Cat(Animal):
	def speak(self):
		print("meow")
	def __str__(self):
		return "cat:" + str(self.name) + ":" + str(self.age)
		
class Person(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, age)
		self.set_name(name)
		self.friemds = []
	def get_friends(self):
		return self.friends
	def add_friend(self, fname):
		if fname not in self.friemds:
			self.friends.append(fname)
	def speak(self):
		print("hello")
	def age_diff(self, other):
		diff = self.age - other.age
		print(abs(diff), "year difference")
	def __str__(self):
		return "person" + str(self.name)+ ":" + str(self.age)
		

# print("\n---- person tests ----")
# p1 = Person("jack", 30)
# p2 = Person("jill", 25)

# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)		


class Student(Person):
	def __init__(self, name, age, major=None):
		Person.__init__(self, name, age)
		self.major = major
	def change_major(self, major):
		self.major = major
	def speak(self):
		r = random.random()
		if r < 0.25:
			print("i have homework")
		elif 0.25 <= r < 0.5:
			print("i need to sleep")
		elif 0.5 <= r < 0.75:
			print("i should eat")
		else:
			print("i am watching tv")
	def __str__(self):
		return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
		

		
# print("\n--- student tests ----")
# s1 = Student("alice", 20, "cs")
# s2 = Student("beth", 18)
# print(s1)
# print(s2)
# print(s1.get_name(), "says:", end=" ")
# s1.speak()
# print(s2.get_name(),"says:", end=" ")
# s2.speak()



class Rabbit(Animal):
	tag = 1 #class variable

	def __init__(self, age, parent1=None, parent2=None):
		Animal.__init__(self, age)
		self.parent1 = parent1
		self.parent2 = parent2
		self.rid = Rabbit.tag #instance variable
		Rabbit.tag += 1
	def get_rid(self):
		return str(self.rid).zfill(3)
	def get_parent1	(self):
		return self.parent1
	def get_parent2(self):
		return self.parent2
	def __add__(self, other):
		return Rabbit(0, self, other)
	def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
		parents_same = self.parent1.rid == other.parent1.rid \
		and self.parent2.rid == other.parent2.rid
		parents_opposite = self.parent2.rid == other.parent1.rid \
		and self.parent1.rid == other.parent2.rid
		return parents_same or parents_opposite

	def __str__(self):
		return "rabbit:"+ self.get_rid()


	
		
print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)















