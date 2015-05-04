import os

class RessourceException(Exception):
	pass

class PathUtil:

	@staticmethod
	def get_content_from_file(path):
		PathUtil.ensure_path_exists(path)
		with open(path) as file:
			file_content = file.read()
		return file_content

	@staticmethod
	def ensure_path_exists(path):
		if not os.path.exists(path):
			raise FileNotFoundError('The "{0}" path dont exists.'.format(path))

class RessourceUtil:

	@staticmethod
	def get_ressource_path(ressource_name = None):
		ressource_folder = ['docs', 'ressources']

		if ressource_name is not None:
			ressource_folder.append(ressource_name)

		ressource_path = os.path.join(*ressource_folder)

		if os.path.isdir(ressource_path) and not ressource_path.endswith('/'):
			ressource_path+= '/'

		return ressource_path

	@staticmethod
	def get_content_from_ressource(ressource_name):
		try:
			ressource_path = RessourceUtil.get_ressource_path(ressource_name)
			return PathUtil.get_content_from_file(ressource_path)
		except FileNotFoundError:
			RessourceUtil.__handleFileNotFoundError(ressource_name)

	@staticmethod
	def ensure_ressource_exists(ressource_name):
		try:
			ressource_path = RessourceUtil.get_ressource_path(ressource_name)
			PathUtil.ensure_path_exists(ressource_path)
		except FileNotFoundError:
			RessourceUtil.__handleFileNotFoundError(ressource_name)

	@staticmethod
	def __handleFileNotFoundError(filename):
		raise RessourceException('The "{0}" ressource dont exists.'.format(filename))








