class Filter(object):
	"""
	An object that is able to produce a filtered version of a CSVFile based
	on some filtering criterias.
	"""
	def __init__(self, csvin=None):
		self._input = csvin
		
	#TODO : find out how to get an interface-like behaviour in Python
	# Say "I want all subclasses to implement this method"
	def job(self):
		pass
		
		

class FieldSelector(Filter):
	"""
	A Filter object that selects a field within a given CSVFile.
	"""
	def __init__(self, csvin=None, field):
		super()
		self._field = field
	
	def job(self):
		return self._input.data[self._field]
	


class Updater(Filter):
	pass
	
	
	
class Remover(Filter):
	pass
	
	
	
class Inserter(Filter):
	pass
