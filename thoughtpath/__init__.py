from thoughtpath.memory import Memory

class ThoughtPath:
	
	def __init__(self, prompt):
		self.prompt = prompt
	
	
	def start(self):
		self.get_result(self.prompt)
		
		#print(result)
	
	
	def get_result(self, prompt):
		
		self.make_memories(prompt)

		#self.get_memory()


	
	
	def make_memories(self, prompt):

		#self.remember(prompt, 'Talk About Something')
		#self.remember(prompt, prompt)

		previous_letter = ' '

		for letter in prompt:
			self.remember(letter, previous_letter)

			#print(letter)

			previous_letter = letter
			previous_value = letter

			first_item = True

			for item in prompt.split(letter):

				#print(item)

				if first_item:
					remember_item = item
				else:
					remember_item = letter + item

				self.remember(remember_item, previous_value)
				previous_value = remember_item
		
		return item


	def get_memory(self):
		
		memory = Memory()
		
		return memory
	
	
	def remember(self, current_value, previous_value):
		
		memory = self.get_memory()

		memory.save_memories(current_value, previous_value)
		
	def get_response(self, prompt):
		memory = self.get_memory()

		response = memory.get_response(prompt)

		return response




	#def find_patterns(self, prompt):
	#	memory = self.get_memory(prompt, '')

	#	response = memory.get_response(prompt)

	#	return response
	