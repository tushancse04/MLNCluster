class Atom:
	def __init__(self, atomString):

		parts = atomString.split('(')
		self.name = parts[0].strip()
		values = parts[1].split(')')[0].split(',')
		for i,v in enumerate(values):
			values[i] = v.strip()
		self.values = values
