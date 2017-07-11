from Models.Formula import Formula
class MLNProcessor:
	PredPairs = []
	def __init__(self):
		pass
	def ProcessMLN(self,mlnpath):
		mfile = open(mlnpath)
		for formula in mfile:
			if formula.count(':') <= 1:
				f = Formula()
				self.PredPairs += f.GetPredPairs(formula)
