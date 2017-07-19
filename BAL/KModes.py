import numpy as np
from kmodes import kmodes
import math

class KModes:
	def __init__(self):
		pass
	def Cluster(self,feature_matrix,CR):
		for pred in feature_matrix:
			features = []
			for atom_value in feature_matrix[pred]:
				features += [feature_matrix[pred][atom_value]]
			print(pred,len(features[0]))

			n_of_clusters = math.floor(len(features)*CR)
			km = kmodes.KModes(n_clusters=n_of_clusters, init='Huang', n_init=1, verbose=1)
			clusters = km.fit_predict(features)
			print(clusters)