import sys
from thoughtpath import ThoughtPath


args = sys.argv

del args[0]

prompt = " ".join(args)

path = ThoughtPath(prompt)

path.start()
