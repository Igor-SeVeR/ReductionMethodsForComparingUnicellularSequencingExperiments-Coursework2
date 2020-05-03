import sys

#Library to save LDA model
import joblib

#Library to read files format
import scanpy as sc

#Library, which contains LDA model trainer
from sklearn.decomposition import LatentDirichletAllocation as LDA

#Reading data
lda_model_name = sys.argv[1]
path_to_files = sys.argv[2]
number_of_themes = int(sys.argv[3])
a_Data = sc.read_10x_mtx(path_to_files + '/')
path_to_model = sys.argv[0] + '/'

#Learning new model
data = a_Data.X
lda_model = LDA(n_components=number_of_themes, learning_method='online')
lda_output = lda_model.fit_transform(data)

#Saving new model
joblib.dump(lda_model, lda_model_name + '.jl')