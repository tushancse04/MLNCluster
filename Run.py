from BAL.EvidProcessor import EvidProcessor
from BAL.MLNProcessor import MLNProcessor
from BAL.FeatureGenerator import FeatureGenerator
ep = EvidProcessor()
atoms = ep.GetAtoms("/home/localadmin/mominul/Cluster/Data/er/test-0.txt")
mp = MLNProcessor()
predpairs = mp.GetPredPairs("/home/localadmin/mominul/Cluster/Data/er/mln.txt") 
fg = FeatureGenerator()
fg.GenerateFeatureMatrix(atoms,predpairs)