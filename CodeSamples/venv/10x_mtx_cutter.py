number_of_barcodes = 20
number_of_genes = 100

#Reducing the number of barcodes to 500

print("Starting barcode reducing!")
barcodes = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TrainData/blood/barcodes.tsv", "r")
barcodes_500 = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TestData/blood/barcodes.tsv", "w")
barcodes_data = barcodes.readlines()
barcodes_500.writelines(barcodes_data[:number_of_barcodes])
barcodes_500.close()
barcodes_500 = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TestData/blood/barcodes.tsv", "r")
barcodes_data_2 = barcodes_500.readlines()
print("Length of barcodes now = ", len(barcodes_data_2))
print("Length of barcodes was = ", len(barcodes_data))
barcodes_500.close()
barcodes.close()
print("Barcodes reducing completed!")

#Reducing the number of genes to 2000

print("Starting gene reducing!")
genes = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TrainData/blood/genes.tsv", "r")
genes_2000 = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TestData/blood/genes.tsv", "w")
genes_data = genes.readlines()
genes_2000.writelines(genes_data[1:number_of_genes + 1])
genes_2000.close()
genes_2000 = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TestData/blood/genes.tsv", "r")
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
matrix = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TrainData/blood/matrix.mtx", "r")
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
matrix = open("/home/igor-server/courseWork/ReductionMethodsForComparingUnicellularSequencingExperiments-Coursework2/TestData/blood/matrix.mtx", "w")
matrix.writelines(data1)
matrix.writelines(str(number_of_genes) + ' ' + str(number_of_barcodes) + ' ' + str(cnt) + '\n')
matrix.writelines(data)
matrix.close()
print("Total lines in matrix now = ", cnt)
print("End of reducing matrix")