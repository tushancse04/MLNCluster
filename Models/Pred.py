class Pred:
	def __init__(self, predstring):
		parts = predstring.split('(')
		self.name = parts[0].strip()
		values = parts[1].split(')')[0].split(',')
		for i,v in enumerate(values):
			values[i] = v.strip()
		self.values = values


