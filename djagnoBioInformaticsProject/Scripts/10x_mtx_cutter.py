import sys
import random
#Uncomment when working on prod
#number_of_barcodes = int(sys.argv[1])
#number_of_genes = int(sys.argv[2])
#path_to_files = sys.argv[3]

number_of_barcodes = 8000
number_of_genes = 2000
path_to_files = '/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TrainData/liver'
path_to_output = '/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TestData/liver'

#Working with barcodes

print("Starting barcode reducing!")
barcodes = open(path_to_files + "/barcodes.tsv", "r")
barcodes_output = open(path_to_output + "/barcodes.tsv", "w")
barcodes_data = barcodes.readlines()
barcodes_output.writelines(barcodes_data[:number_of_barcodes])
barcodes_output.close()
#Test start
barcodes_500 = open(path_to_output + "/barcodes.tsv", "r")
barcodes_data_2 = barcodes_500.readlines()
print("Length of barcodes now = ", len(barcodes_data_2))
print("Length of barcodes was = ", len(barcodes_data))
barcodes_500.close()
barcodes.close()
#Test finished
print("Barcodes reducing completed!")

#Working with genes

print("Starting gene reducing!")
genes = open(path_to_files + "/genes.tsv", "r")
genes_output = open(path_to_output + "/genes.tsv", "w")
genes_data = genes.readlines()
genes_output.writelines(genes_data[1:number_of_genes + 1])
for i in range (11669 - number_of_genes):
    genes_output.write("ENSG00001111159	AAAAAA" + '\n')
genes_output.close()
#Starting test
genes_2000 = open(path_to_output + "/genes.tsv", "r")
genes_data_2 = genes_2000.readlines()
print("Length of genes now = ", len(genes_data_2))
print("Length of genes was = ", len(genes_data))
genes_2000.close()
genes.close()
print("Genes reducing completed!")

#Reducing_the_matrix

def cut_line(line):
    numbers = line.split()
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    if (first_number > number_of_genes or second_number > number_of_barcodes):
        return False
    return True


print("Starting matrix reducing!")
matrix = open(path_to_files + "/matrix.mtx", "r")
data1 = matrix.readline()
data2 = matrix.readline()
print(data2)
cnt = 0
data = []
next_line = matrix.readline()
while (next_line):
    if (cut_line(next_line)):
        cnt += 1
        data.append(next_line)
    next_line = matrix.readline()
print("End of data scanning.")
print("Starting to write data.")
matrix.close()
matrix = open(path_to_output + "/matrix.mtx", "w")
matrix.writelines(data1)
matrix.writelines(str(11669) + ' ' + str(number_of_barcodes) + ' ' + str(cnt) + '\n')
random.shuffle(data)
matrix.writelines(data)
matrix.close()
print("Total lines in matrix now = ", cnt)
print("End of reducing matrix")