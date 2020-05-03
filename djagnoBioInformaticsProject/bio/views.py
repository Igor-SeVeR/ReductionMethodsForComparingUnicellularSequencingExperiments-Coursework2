import os
import zipfile
import subprocess

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.response import Response
from rest_framework.views import APIView
from igor.settings import SERVER_URL

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

def IGORMAGIC(file):
    z = zipfile.ZipFile("media/" + file, 'r')
    z.extractall(path="media/archives")
    p = subprocess.Popen("python Scripts/lda_theme_proportion.py media/models/blood_lda_model.jl media/TrainData/blood media/archives media/plots", stdout=subprocess.PIPE, shell=True)
    p.wait()
    return {"Plot by trained model": 'media/plots/plot1.png', "Plot by user data on train model": 'media/plots/plot2.png'}


def saveFile(file, pathToSave):
    data = file.read()
    path = default_storage.save(pathToSave, ContentFile(data))

    return path


def formUrlOnServer(pathes):
    for key in pathes:
        pathes[key] = SERVER_URL + pathes[key]
    return pathes


class MainView(APIView):
    def post(self, request):
        file = request.FILES['photo']
        pathToArch = saveFile(file, 'archives/arch.zip')
        pathes = IGORMAGIC(pathToArch)
        pathes = formUrlOnServer(pathes)
        print(pathToArch)
        return Response(pathes)
