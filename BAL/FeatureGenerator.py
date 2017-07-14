from Models.Formula import Formula
from Models.Atom import Atom
class FeatureGenerator:
	feature_matrix = {}
	def __init__(self):
		pass
	def GenerateFeatureMatrix(self,atoms,predpairs):
		for predpair in predpairs:
			pred1 = predpair[0]
			pred2 = predpair[1]
			for i,p1v in enumerate(pred1.values):
				for j,p2v in enumerate(pred2.values):
					if p1v == p2v:
						self.AddFeature(atoms,pred1.name,i,pred2.name)
						self.AddFeature(atoms,pred2.name,j,pred1.name)
		return self.feature_matrix


	def AddFeature(self, atoms, pred_name,pos, coupling_pred_name):
		SN = self.GetPredShortName(coupling_pred_name)
		for atom in atoms[pred_name]:
			if atom.name not in self.feature_matrix:
				self.feature_matrix[atom.name] = {}

			if len(atom.values) == 1:
				if atom.values[0] not in self.feature_matrix[atom.name]:
					self.feature_matrix[atom.name][atom.values[0]] = []
				self.feature_matrix[atom.name][atom.values[0]] += [SN + atom.values[pos]]
			else:
				if (atom.values[0],atom.values[1]) not in self.feature_matrix[atom.name]:
					self.feature_matrix[atom.name][(atom.values[0],atom.values[1])] = []
				self.feature_matrix[atom.name][(atom.values[0],atom.values[1])] += [SN + atom.values[pos]]



	def GetPredShortName(self,pred_name):
		SN = ''
		for a in pred_name:
			if a.isupper():
				SN += str(a)
		return SN