import sys
import random
#Uncomment when working on prod
path_to_files = sys.argv[1]
path_to_data = sys.argv[2]

file = open(path_to_data + "/matrix.mtx")
input_str = file.readline()
input_str = file.readline()
arr = input_str.split(" ")
file.close()

number_of_barcodes = int(arr[1])
number_of_genes = int(arr[0])

#Working with barcodes

print("Starting barcode reducing!")
barcodes = open(path_to_files + "/barcodes.tsv", "r")
number_of_barcodes = len(barcodes.readlines())
barcodes.close()


#Working with genes

genes = open(path_to_files + "/genes.tsv", "r")
genes_data = genes.readlines()
number_of_genes_in_file = len(genes_data) - 1
genes.close()
genes = open(path_to_files + "/genes.tsv", "w")
if (number_of_genes_in_file >= number_of_genes):
    genes.writelines(genes_data[1:number_of_genes + 1])
else:
    genes.writelines(genes_data[1:number_of_genes_in_file + 1])
    for i in range (number_of_genes - number_of_genes_in_file):
        genes.write("ENSG00001111159	AAAAAA" + '\n')
genes.close()

#Reducing_the_matrix

def cut_line(line):
    numbers = line.split()
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    if (first_number > number_of_genes or second_number > number_of_barcodes):
        return False
    return True

matrix = open(path_to_files + "/matrix.mtx", "r")
data1 = matrix.readline()
data2 = matrix.readline()
cnt = 0
data = []
next_line = matrix.readline()
while (next_line):
    if (cut_line(next_line)):
        cnt += 1
        data.append(next_line)
    next_line = matrix.readline()
matrix.close()
matrix = open(path_to_files + "/matrix.mtx", "w")
matrix.writelines(data1)
matrix.writelines(str(number_of_genes) + ' ' + str(number_of_barcodes) + ' ' + str(cnt) + '\n')
matrix.writelines(data)
matrix.close()