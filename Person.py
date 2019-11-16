#########################################################################
# Person.py								
# Version: 1.0														
# Date: 11/16/2019													
# Description: This is an object module which contains the atributes
#	describing the faimly member.
#########################################################################

class Person:
	'''
	This class contains all the information necessary about the individual
	and also the methods required to access and change certain info.
	'''

	def __init__(self, name, gender=0, age=0):
		'''
		Constructor method. Initialize all of the atributes
		'''
		self.name = name
		self.gender = gender
		self.age = age

	def get_name(self):
		'''
		The get_name function is used to acess the individuals name.
		Returns: string name
		'''
		return self.name