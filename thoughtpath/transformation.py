import hashlib
from os.path import exists

class Transformation:
	
	def __init__(self, prompt):
		self.prompt = prompt
		self.result = ''
		
		self.load_existing(prompt)

		
	def load_existing(self, prompt):
		
		prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()
		
		print(prompt_hash)
		
		memory_path = 'memory/' + str(prompt_hash) + '.txt'
		
		if(exists(memory_path)):
			file = open(memory_path,'r')
			
			self.result = file.read()
			
		else:
			file = open(memory_path,'w')
			
			file.write(prompt)
			
			self.result = prompt
		
	
	def get_result(self):
		return self.result
		