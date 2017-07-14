import numpy as np
from kmodes import kmodes
class KModes:
	def __init__(self):
		pass
	def Cluster(self,features):
		km = kmodes.KModes(n_clusters=100, init='Huang', n_init=1, verbose=1)
		clusters = km.fit_predict(features)
		print(clusters)
		#print(clusters)