import os
import zipfile
import subprocess

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.response import Response
from rest_framework.views import APIView
from bio_settings.settings import SERVER_URL

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
import pyLDAvis
import random

def clearData(filePath):
    folder = filePath
    for the_file in os.listdir(folder):
        next_file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(next_file_path):
                os.unlink(next_file_path)
        except Exception as e:
            print()

def useBloodModel(file):
    clearData("media/plots")
    clearData("media/OutputData")
    z = zipfile.ZipFile("media/" + file, 'r')
    z.extractall(path="media/archives")
    data = sc.read_10x_mtx("media/archives/")
    input_number = open("media/systemFiles/number_of_questions.txt", "r")
    number = int(input_number.readline()) + 1
    input_number.close()
    input_number = open("media/systemFiles/number_of_questions.txt", "w")
    input_number.write(str(number))
    input_number.close()
    file_name = "model_data" + str(number)
    p = subprocess.Popen("python Scripts/10x_mtx_cutter.py media/archives media/TrainData/blood", stdout=subprocess.PIPE, shell=True)
    p.wait()
    p = subprocess.Popen("python Scripts/lda_theme_proportion.py media/models/blood_lda_model.jl media/TrainData/blood media/archives media/plots " + file_name, stdout=subprocess.PIPE, shell=True)
    p.wait()
    p = subprocess.Popen("python Scripts/database_prepare.py media/DataBase/Human_cell_markers.txt media/models/blood_lda_model.jl media/TrainData/blood media/OutputData " + file_name,
        stdout=subprocess.PIPE, shell=True)
    p.wait()
    return {"Predicted cells by clusters:": 'media/OutputData/' + file_name + '.txt', "Interactive pyLDAvis graph:": 'media/OutputData/' + file_name + '.html', "The distribution of barcodes in model.": 'media/plots/' + file_name +'1.png', "The distribution of barcodes in users data due to model.": 'media/plots/' + file_name + '2.png'}

def buildModelAndUseIt(file):
    clearData("media/plots")
    clearData("media/OutputData")
    z = zipfile.ZipFile("media/" + file, 'r')
    z.extractall(path="media/archives")
    data = sc.read_10x_mtx("media/archives/")
    input_number = open("media/systemFiles/number_of_questions.txt", "r")
    number = int(input_number.readline()) + 1
    input_number.close()
    input_number = open("media/systemFiles/number_of_questions.txt", "w")
    input_number.write(str(number))
    input_number.close()
    file_name = "users_data" + str(number)
    p = subprocess.Popen("python Scripts/learn_new_model.py users_lda_model media/archives 10 media/models", stdout=subprocess.PIPE, shell=True)
    p.wait()
    p = subprocess.Popen("python Scripts/lda_theme_proportion.py media/models/users_lda_model.jl media/archives media/archives media/plots " + file_name, stdout=subprocess.PIPE, shell=True)
    p.wait()
    p = subprocess.Popen("python Scripts/database_prepare.py media/DataBase/Human_cell_markers.txt media/models/users_lda_model.jl media/archives media/OutputData " + file_name, stdout=subprocess.PIPE, shell=True)
    p.wait()
    return {"Predicted cells by clusters:": 'media/OutputData/' + file_name + '.txt', "Interactive pyLDAvis graph:": 'media/OutputData/' + file_name + '.html', "The distribution of barcodes in model.": 'media/plots/' + file_name + '1.png'}


def saveFile(file, pathToSave):
    data = file.read()
    path = default_storage.save(pathToSave, ContentFile(data))
    return path


def formUrlOnServer(pathes):
    for key in pathes:
        pathes[key] = SERVER_URL + pathes[key]
    return pathes


class UseBuiltModel(APIView):
    def post(self, request):
        clearData("media/archives")
        file = request.FILES['photo']
        pathToArch = saveFile(file, 'archives/arch.zip')
        pathes = useBloodModel(pathToArch)
        pathes = formUrlOnServer(pathes)
        print(pathToArch)
        return Response(pathes)

class BuildModel(APIView):
    def post(self, request):
        clearData("media/archives")
        file = request.FILES['photo']
        pathToArch = saveFile(file, 'archives/arch.zip')
        pathes = buildModelAndUseIt(pathToArch)
        pathes = formUrlOnServer(pathes)
        print(pathToArch)
        return Response(pathes)
