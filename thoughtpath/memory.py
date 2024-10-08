import hashlib
import os
from os.path import exists

import random


class Memory:
	
	def __init__(self):
		self.result = ''

		
	def save_memories(self, prompt, previous_value):
		
		prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()
		previous_value_hash = hashlib.md5(previous_value.encode('utf-8')).hexdigest()
		
		#print(prompt_hash)
		
		memory_path = 'memory/' + str(previous_value_hash)
		
		if(not exists(memory_path)):
			os.mkdir(memory_path)
		
		#dir_list = os.listdir(memory_path)
		
		#print(len(dir_list))
		
		save_path = memory_path + '/' + str(prompt_hash) + '.txt'
	
		file = open(save_path,'w')
        
		file.write(prompt)
        
		file.close()
        
		self.result = prompt

		#if(len(dir_list) == 0):
		#	save_path = memory_path + '/' + str(prompt_hash) + '.txt'
			
		#	file = open(save_path,'w')
			
		#	file.write(prompt)
			
		#	file.close()
			
		#	self.result = prompt
		#else:
		#	for entry in dir_list:
		#		file = open(memory_path + '/' + entry,'r')
				
		#		self.result = file.read()
				
		#		file.close()
		
		
	
	def get_result(self):
		return self.result
	

	def get_response(self, starting_point):

		response = ['']

		for num in range(1, random.randint(2, 20)):

			starting_point_hash = hashlib.md5(starting_point.encode('utf-8')).hexdigest()

			memory_path = 'memory/' + str(starting_point_hash)

			if(exists(memory_path)):
				dir_list = os.listdir(memory_path)

				rand_value = random.randint(0, len(dir_list) - 1)

				print(rand_value)
				print(len(dir_list))

				entry = dir_list[rand_value]

				full_entry_path = memory_path + '/' + entry

				if exists(full_entry_path):
					file = open(full_entry_path,'r')

					next_value = file.read()
						
					response.append(next_value)
						
					file.close()

			starting_point = next_value

		s = " "

		return s.join(response)
