import hashlib
import os
from os.path import exists


class Transformation:
	
	def __init__(self, prompt):
		self.prompt = prompt
		self.result = ''
		
		self.load_existing(prompt)

		
	def load_existing(self, prompt):
		
		prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()
		
		print(prompt_hash)
		
		memory_path = 'memory/' + str(prompt_hash)
		
		if(not exists(memory_path)):
			os.mkdir(memory_path)
		
		dir_list = os.listdir(memory_path)
		
		print(len(dir_list))
		
		if(len(dir_list) == 0):
			save_path = memory_path + '/' + str(prompt_hash) + '.txt'
			
			file = open(save_path,'w')
			
			file.write(prompt)
			
			file.close()
			
			self.result = prompt
		else:
			for entry in dir_list:
				file = open(memory_path + '/' + entry,'r')
				
				self.result = file.read()
				
				file.close()
		
		
	
	def get_result(self):
		return self.result
		