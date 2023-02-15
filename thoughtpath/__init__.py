from thoughtpath.transformation import Transformation

class ThoughtPath:
	
	def __init__(self, prompt):
		self.prompt = prompt
	
	
	def start(self):
		result = self.get_result(self.prompt)
		
		print(result)
	
	
	def get_result(self, prompt):
		
		result = self.transform(prompt)
		
		return result
	
	
	def get_transformation(self, prompt):
		
		transformation = Transformation(prompt)
		
		return transformation
	
	
	def transform(self, prompt):
		
		transformation = self.get_transformation(prompt)
		
		return transformation.get_result()
	