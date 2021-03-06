# -*- coding: utf-8 -*-
from CSVHandler import CSVFile, Field

class Filter(object):
	"""
	An abstract object that is able to produce a filtered version of a CSVFile based
	on some filtering criterias.
	"""
	def __init__(self, csvin):
		self._input = csvin
		
	def __str__(self):
		raise NotImplementedError
		
	@property
	def inputCSV(self):		# damn it ! input is already used by Python
		return self._input
		
	def output(self):
		"""
		This method is abstract. It should be overriden by all the classes extending
		Filter.
		"""
		raise NotImplementedError
		

class FieldSelector(Filter):
	"""
	A Filter object that selects a field within a given CSVFile.
	"""
	def __init__(self, field=None, csvin=None):
		super(FieldSelector, self).__init__(csvin)
		self._field = field
		
	def __str__(self):
		return "Field selector"
		
	@property
	def field(self):
		return self._field
		
	@field.setter
	def field(self, value):
		self._field = value
	
	def output(self):
		"""
		Returns a Field object out of a bigger CSVFile. The selected
		field is stored in self._field.
		"""
		return Field(header=self._field, values=self._input.data[self._field])
	

class FindAndReplace(Filter):
	def __str__(self):
		return "Find and Replace"
	
	
	
class Remover(Filter):
	def __str__(self):
		return "Remover"
	
	
	
class Inserter(Filter):
	def __str__(self):
		return "Inserter"
	
	
# ----- TESTING ----- #
if __name__ == "__main__" :
	import sys
	import os
	if os.path.isfile(os.path.abspath(sys.argv[1])):
		csv_file    = CSVFile(os.path.abspath(sys.argv[1]))
		filter_test = FieldSelector(csvin=csv_file, field="X_CURRENT_TARGET_SP")
		print(csv_file)
		print(filter_test.output())
	else:
		print("Error, the file does not exist")
