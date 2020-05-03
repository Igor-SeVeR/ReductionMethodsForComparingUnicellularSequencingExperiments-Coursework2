import sys

#Library to save LDA model
import joblib

#Library to read files format
import scanpy as sc

#Library, which contains LDA model trainer
from sklearn.decomposition import LatentDirichletAllocation as LDA

#Libary for plotting
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

#Reading data
path_to_model = sys.argv[1]
path_to_model_data = sys.argv[2]
path_to_users_data = sys.argv[3]
path_to_images = sys.argv[4]

#Reading LDA model
lda_model = joblib.load(path_to_model)
model_data = sc.read_10x_mtx(path_to_model_data + '/')
data_out = model_data.X
lda_output = lda_model.transform(data_out)

#Creating a bar plot of percentage of cell divisions by topic in trained model
df_cell_topic = pd.DataFrame(np.round(lda_output, 2))
df_cell_dominant_topic = np.argmax(df_cell_topic.values, axis=1)
df_cell_topic['dominant_topic'] = df_cell_dominant_topic
number_of_dominant_topics = df_cell_topic['dominant_topic'].value_counts()
topics = []
for i in range (lda_model.n_components):
    topics.append(i)
values = []
for i in range (lda_model.n_components):
    values.append(number_of_dominant_topics[i] / float(data_out.shape[0]) * 100)

# Dictionary loaded into a DataFrame
dataFrame = pd.DataFrame(data={"Topic":topics, "Percentage":values })

# Draw a vertical bar chart
dataFrame.plot.bar(x="Topic", y="Percentage", rot=70, title="")
plot.savefig(path_to_images + "/plot1.png", dpi = 300)

#Reading data
data = sc.read_10x_mtx(path_to_users_data + '/')

#Applying data on a trained model to get cells by topics
data_test = data.X
topic_probability_scores = lda_model.transform(data_test)
df_cell_topic_user = pd.DataFrame(np.round(topic_probability_scores, 2))
df_cell_dominant_topic_user = np.argmax(df_cell_topic_user.values, axis=1)
df_cell_topic_user['dominant_topic'] = df_cell_dominant_topic_user
number_of_dominant_topics_user = df_cell_topic_user['dominant_topic'].value_counts()
topics = []
for i in range (lda_model.n_components):
    topics.append(i)
values = []
for i in range (lda_model.n_components):
    values.append(number_of_dominant_topics_user[i] / float(data_test.shape[0]) * 100)

# Dictionary loaded into a DataFrame
dataFrame = pd.DataFrame(data={"Topic":topics, "Percentage":values })

# Draw a vertical bar chart
dataFrame.plot.bar(x="Topic", y="Percentage", rot=70, title="")
plot.savefig(path_to_images + "/plot2.png", dpi = 300)