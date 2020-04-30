import sys
import zipfile
import numpy as np
import matplotlib.pyplot as plt
import os, shutil

#Кароч надо создать две папки рядом с кодом LoadedData и OutputData
file_path = sys.path[0]
zip_file_path = file_path + '/OutputData/gr.zip' #Тут прописать путь до zip
z = zipfile.ZipFile(zip_file_path, 'r')
z.extractall(path=sys.path[0] + '/LoadedData')
#here must be something to work with
#here it must end
folder = file_path + '/LoadedData'
for the_file in os.listdir(folder):
    next_file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(next_file_path):
            os.unlink(next_file_path)
    except Exception as e:
        print()
rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng
fig, ax = plt.subplots(figsize=(5, 3))
ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()
file_path_for_first_image = file_path + '/OutputData/gr'
file_path_for_second_image = file_path + '/OutputData/gr1'
plt.savefig(file_path_for_first_image, dpi=300)
plt.savefig(file_path_for_second_image, dpi=300)
images = []
#Creating_list_with_images
images.append(file_path_for_first_image)
images.append(file_path_for_second_image)