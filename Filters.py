from CSVHandler import CSVFile, Field

class Filter(object):
	"""
	An abstract object that is able to produce a filtered version of a CSVFile based
	on some filtering criterias.
	"""
	def __init__(self, csvin):
		self._input = csvin
		
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
	def __init__(self, field, csvin):
		super(FieldSelector, self).__init__(csvin=csvin)
		self._field = field
	
	def output(self):
		"""
		Returns a Field object out of a bigger CSVFile.
		"""
		return Field(header=self._field, values=self._input.data[self._field])
	


class Updater(Filter):
	pass
	
	
	
class Remover(Filter):
	pass
	
	
	
class Inserter(Filter):
	pass
	
	
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
