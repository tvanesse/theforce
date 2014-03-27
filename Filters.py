from CSVHandler import CSVFile, Field

class Filter(object):
	"""
	An abstract object that is able to produce a filtered version of a CSVFile based
	on some filtering criterias.
	"""
	def __init__(self, csvin=CSVFile()):
		self._input = csvin
		
	def job(self):
		"""
		This method is abstract. It should be overriden by all the classes extending
		Filter.
		"""
		raise NotImplementedError
		

class FieldSelector(Filter):
	"""
	A Filter object that selects a field within a given CSVFile.
	"""
	def __init__(self, csvin=CSVFile(), field):
		super(FieldSelector, self).__init__(csvin)
		self._field = field
	
	def job(self):
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
