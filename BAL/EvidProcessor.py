from Models.Atom import Atom
from collections import defaultdict
import os
class EvidProcessor:
	def __init__(self):
		pass
	def GetAtoms(self,evidpath):
		files = os.listdir(evidpath)
		atoms = {}
		for fname in files:
			if not (fname.startswith('test') or fname.startswith('train')):
				continue
			efile = open(evidpath + "/" + fname)
			for atomString in efile:
				atom = Atom(atomString)
				if atom.name in atoms:
					atoms[atom.name] += [atom]
				else:
					atoms[atom.name] = [atom]
		return atoms