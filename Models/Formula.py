from Models.Pred import Pred
class Formula:
	def __init__(self):
		pass
	def GetPredPairs(self,formulaString):
		print(formulaString)
		formula = formulaString.split(':')
		if len(formula) < 2:
			return []
		formula = formula[1]
		preds = formula.split('v')
		for i,pred in enumerate(preds):
			preds[i] = pred.strip().replace("!","")
		predpairs = []
		#print(formulaString)
		for i in range(0,len(preds) -1):
			for j in range(i+1,len(preds)):
				pred1 = Pred(preds[i])
				pred2 = Pred(preds[j])
				#print(pred1.name,pred2.name)
				predpairs += [[pred1,pred2]]
		return predpairs