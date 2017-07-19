from BAL.EvidProcessor import EvidProcessor
from BAL.MLNProcessor import MLNProcessor
from BAL.FeatureGenerator import FeatureGenerator
from BAL.KModes import KModes
import numpy as np
from kmodes import kmodes
import numpy as np

print('processing evid file...')
ep = EvidProcessor()
atoms = ep.GetAtoms("/home/localadmin/mominul/Cluster/Data/webkb")

print('processing mln file...')
mp = MLNProcessor()
predpairs = mp.GetPredPairs("/home/localadmin/mominul/Cluster/Data/webkb/mln.txt") 

print('Generating features...')
fg = FeatureGenerator()
feature_matrix = fg.GenerateFeatureMatrix(atoms,predpairs)
CR = .5
print('Generating cluster...')
km = KModes()
km.Cluster(feature_matrix,CR)

