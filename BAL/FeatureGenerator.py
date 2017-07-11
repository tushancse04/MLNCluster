from Models.Formula import Formula
from Models.Atom import Atom
class FeatureGenerator:
	feature_matrix = {}
	predshortnames = {}
	def __init__(self):
		pass
	def GenerateFeatureMatrix(self,atoms,predpairs):
		for predpair in predpairs:
			pred1 = predpair[0]
			pred2 = predpair[1]
			for i,p1v in enumerate(pred1.values):
				for j,p2v in enumerate(pred2.values):
					if p1v == p2v:
						AddFeature(pred1.name)

	def AddFeature(self, pred_name,pos, coupling_pred_name):
