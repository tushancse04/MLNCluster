from Models.Formula import Formula
class MLNProcessor:
	def __init__(self):
		pass
	def GetPredPairs(self,mlnpath):
		PredPairs = []
		mfile = open(mlnpath)
		for formula in mfile:
			if formula.count(':') <= 1:
				f = Formula()
				PredPairs += f.GetPredPairs(formula)

		return PredPairs