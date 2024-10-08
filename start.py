import sys
from thoughtpath import ThoughtPath


args = sys.argv

del args[0]

prompt = " ".join(args)

#print(prompt[1])

path = ThoughtPath(prompt)

last_item = path.make_memories(prompt)

print(last_item)

response = path.get_response(last_item)

print(response)




#print(path.find_patterns(prompt))
