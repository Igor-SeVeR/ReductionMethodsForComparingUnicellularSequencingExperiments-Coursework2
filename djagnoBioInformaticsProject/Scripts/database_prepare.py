import sys

#Library to save LDA model
import joblib

#Library to read files format
import scanpy as sc

# Path to database
path_to_database = '/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/djagnoBioInformaticsProject/media/DataBase/Human_cell_markers.txt'

# Path to lda model
path_to_lda_model = '/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/djagnoBioInformaticsProject/media/models/blood_lda_model.jl'

# Path to data, on which lda model was learnt
path_to_data = '/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/djagnoBioInformaticsProject/media/TrainData/blood'

# Numer of genes, to get from each model topic
number_of_genes_in_topics = 200

# Opening database
data_base = open(path_to_database, "r")

# Reading database and parsing it into dictionary
lines_in_database = data_base.readline()
lines_in_database = data_base.readline()
base_dict = {}
data = []
while (lines_in_database):
    data.append(lines_in_database.split('\t'))
    lines_in_database = data_base.readline()

for i in range (len(data)):
    cell_type = data[i][4]
    cell_name = data[i][5]
    base_dict[cell_name, cell_type] = []

for i in range (len(data)):
    genes_array = data[i][8].replace(" ", "").split(',')
    for j in range (len(genes_array)):
        genes_array[j] = genes_array[j].replace("[", "")
        genes_array[j] = genes_array[j].replace("]", "")
    cell_type = data[i][4]
    cell_name = data[i][5]
    for j in range (len(genes_array)):
        base_dict[cell_name, cell_type].append(genes_array[j])

# End of reading database

# Readind lda model
lda_model = joblib.load(path_to_lda_model)
model_data = sc.read_10x_mtx(path_to_data + '/')

# Getting top-genes for each theme

genes_names = []
for row in sc.get.var_df(model_data).index:
    genes_names.append(row)

genes_by_theme = []
for topic_idx, topic in enumerate(lda_model.components_):
        topic_genes_names = ""
        topic_genes_names += " ".join([genes_names[i]
                             for i in topic.argsort()[:-number_of_genes_in_topics - 1:-1]])
        genes_by_theme.append(topic_genes_names.split(" "))

#Genes per topic are now in genes_by_theme array

answer = []
for i in range (lda_model.n_components):
    genes_intersection = {}
    step_answer = []
    for elem in (base_dict):
        cnt = 0
        for k in range (len(base_dict[elem])):
            for j in range (len(genes_by_theme[i])):
                if (base_dict[elem][k] == genes_by_theme[i][j]):
                    cnt += 1
        name_and_type = []
        name_and_type.append(elem[0])
        name_and_type.append(elem[1])
        genes_intersection[float(cnt) / float(len(base_dict[elem]))] = name_and_type
    sorted_values = sorted(genes_intersection, reverse=True)
    number = 0
    for j in range(5):
        step_answer.append(genes_intersection[sorted_values[j]])
    answer.append(step_answer)

file = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/djagnoBioInformaticsProject/media/OutputData/prediction.txt", "w")
file.writelines("Here are predicted cells by genes significance in each topic.")
for i in range (len(answer)):
    file.write("Topic " + str(i) + '\n')
    for j in range(len(answer[i])):
        file.write("Cell name: " + answer[i][j][0] + "; Cell type: " + answer[i][j][1] + '\n')