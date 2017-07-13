from Models.Atom import Atom
from collections import defaultdict
class EvidProcessor:
	def __init__(self):
		pass
	def GetAtoms(self,evidpath):
		efile = open(evidpath)
		atoms = {}
		for atomString in efile:
			atom = Atom(atomString)
			if atom.name in atoms:
				atoms[atom.name] += [atom]
			else:
				atoms[atom.name] = [atom]
		return atoms