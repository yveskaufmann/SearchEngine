class ListUtil:
	""" 
		Handy methods for url handling 
	"""
	def to_list_without_duplicated_entries(list_with_duplicated_entries):
		"""
			Returns a given list with removed duplications.
		"""
		return sorted(set(list_with_duplicated_entries))
