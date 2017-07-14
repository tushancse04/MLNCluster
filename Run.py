from BAL.EvidProcessor import EvidProcessor
from BAL.MLNProcessor import MLNProcessor
from BAL.FeatureGenerator import FeatureGenerator
from BAL.KModes import KModes
import numpy as np
from kmodes import kmodes
import numpy as np

ep = EvidProcessor()
atoms = ep.GetAtoms("/home/localadmin/mominul/Cluster/Data/er/test-0.txt")
mp = MLNProcessor()
predpairs = mp.GetPredPairs("/home/localadmin/mominul/Cluster/Data/er/mln.txt") 
fg = FeatureGenerator()
feature_matrix = fg.GenerateFeatureMatrix(atoms,predpairs)
#for x in feature_matrix:
#	print(x)

for pred in feature_matrix:
	features = []
	for atom_value in feature_matrix[pred]:
		features += [feature_matrix[pred][atom_value]]
	features = features[0:10]
	km = KModes()
	km.Cluster(features)