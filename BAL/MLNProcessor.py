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
		for p in PredPairs:
			print(p[0].name,p[0].values,p[1].name,p[1].values)
		return PredPairs