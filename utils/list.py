class ListUtil:
	def to_list_without_duplicated_entries(list_with_duplicated_entries):
		return sorted(set(list_with_duplicated_entries))
