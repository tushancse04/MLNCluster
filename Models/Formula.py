class Formula:
	def __init__(self):
		pass
	def GetPredPairs(self,formulaString):
		formula = formulaString.split(':')[1]
		preds = formula.split('v')
		for i,pred in enumerate(preds):
			preds[i] = pred.strip().replace("!","")
		predpairs = []
		for i in range(0,len(preds) -1):
			for j in range(1,len(preds)):
				pred1 = Pred(preds[i])
				pred2 = Pred(preds[j])
				predpairs += [[pred1,pred2]]
		return predpairs