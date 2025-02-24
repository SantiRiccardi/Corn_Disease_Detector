## FUNCIONES PERSONALIZADAS ###

## Librerias ##
# Python
import os, sys
import pickle

# Data Analysis
import numpy as np
import pandas as pd

# Data Preproccesing
import tensorflow as tf 
from matplotlib.image import imread
from PIL import Image
import cv2
from skimage.transform import resize
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import label_binarize

# Data Visualization
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns

# Deep Learning

# Metricas
from sklearn.metrics import (confusion_matrix, classification_report, precision_recall_curve,
                            precision_score, recall_score,
                            f1_score, accuracy_score, roc_curve, auc)


# Clases
clases = os.listdir("/content/drive/MyDrive/Colab Notebooks/MAIZ/src/data/data_splitted/train")
clases

# Diccionarios de Mapeos para las etiquetas:
# para train (a numericas):
clases_a_cat = {0:'Blight',
                        1:'Common_Rust',
                        2:'Gray_Leaf_Spot',
                        3:'Healthy'}

# y para los resultados/predicciones (a categóricas):
clases_a_num = {'Blight':0,
                'Common_Rust':1,
                'Gray_Leaf_Spot':2,
                'Healthy':3}




#----------------------------------------------#
## Guardado y Carga de Datasets ##

def cargar_dataset(ruta):
  # Ruta donde se encuentra el dataset
  # Cargamos el dataset con pickle:
  with open(ruta, 'rb') as archivo:
    dataset_cargado = pickle.load(archivo)

  return dataset_cargado
  
def guardar_dataset(dataset, ruta):
  # Ruta donde queremos guardar el dataset
  # Guardamos el dataset con pickle:
  with open(ruta, 'wb') as archivo:
    pickle.dump(dataset, archivo)

#----------------------------------------------#
## EDA ##

def dimensiones_imagenes(dataset):
  # Creamos una lista con todas las dimensiones que hay
  l_shapes = []
  for i in range(0,len(dataset)):
    shape = dataset[i].shape
    l_shapes.append(shape)
  # Creamos un diccionario donde las keys son las dimensiones, los values el n° de veces que esta esa dimension
  d = {}
  for shape in l_shapes:
    if shape in d: # si la dimension esta en el d, le sumanos 1 a su value
      d[shape]+=1

    else:
      d[shape] = 1 # si no esta en el d, introducimos esa dimension y su value es 1
  # Iteramos en el diccionario creado
  for key in d:
    print("{} --> {} imagenes".format(key, d[key]))

  return d

def distribución_x_clase(train_path):
  # Creamos un diccionario con {clase: n° de imagenes de esa clase}
  name_clases = os.listdir(train_path)
  d = {}
  for name_clase in name_clases:
    clase = os.listdir(train_path + '/' + name_clase)
    d[name_clase] = len(clase)

  # Creamos el df
  df = pd.DataFrame(columns = ["Class_Name", "N° of Images"])
  # Insertamos los valores en cada columna del df
  df['Class_Name'] = d.keys()
  df["N° of Images"] = d.values()

  return df



#----------------------------------------------#
## Data Preprocessing ##

def transformacion_datos_X(X_train, X_test, X_val):

  # Convertimos las listas en arrays:
  X_train = np.array(X_train)
  X_test = np.array(X_test)
  X_val = np.array(X_val)

  # Creamos una lista con las X:
  data_X = [X_train, X_test, X_val]
  for X in data_X:
    # Normalizamos las imagenes a a valores entre [0, 1]
    for i in range(0, len(X)):
      X[i] /= 255

  return X_train, X_test, X_val


def transformacion_datos_y_OneHotEncoding(y_train, y_test, y_val):
  # 1°) Lista con los nombres de las clases:
  class_names = clases
  
  # 2°) Creamos diccionario: {clase1:0,...., claseN:n}
  clases_a_num = {class_name : index for index, class_name in enumerate(class_names)}

  # 3°) Mapeo
  y_train = list(map(lambda etiqueta: clases_a_num[etiqueta], y_train)) # etiqueta=label=numero [0,1,2,3] 
  y_test = list(map(lambda etiqueta: clases_a_num[etiqueta], y_test))
  y_val = list(map(lambda etiqueta: clases_a_num[etiqueta], y_val))
  '''                                                                   
  Argumentos de la funcion lambda :
  qué es lo que queremos que nos devuelva : condición/lo que buscamos
  
  Argumentos de la funcion Map(funcion, iterable)
  * Funcion: Es una función que se aplicará a cada elemento del iterable, en nuestro caso usamos lambda
  * iterable: Es la secuencia de elementos a la que se aplicará la función. Ej:lista, tupla 

  list(): map() devuelve un objeto iterable, no puedes acceder a sus elementos directamente o inspeccionarlo fácilmente
          Por eso convertimos el resultado de map en una lista iterable
  '''
  
  # 4°) Conversion de v targets a numéricas:
  y_train = to_categorical(y_train, 
                           num_classes=4)

  y_test = to_categorical(y_test, 
                          num_classes=4)

  y_val = to_categorical(y_val, 
                         num_classes=4)

  return  y_train, y_test, y_val

def transformacion_datos_y_LabelEncoding(y_train, y_test, y_val):
  # Conversion de v targets a numéricas
  targets = [y_train, y_test, y_val]
  # Crear diccionario con los nombres de las clases y sus valores numericos
  d = {'Blight':0, 'Common_Rust':1, 'Gray_Leaf_Spot':2, 'Healthy':3}

  # Iteramos en train-test-val:
  for y in targets:
    # Itermaos en y
    for i, clase in enumerate(y): #enumerate() devuelve una tupla que contiene el índice de la clase en la lista y la clase en sí misma
      y[i] = d[clase]

  # Transformamos: en numpy arrays, tipo float y redimensionamos:
  y_train = np.asarray(y_train).astype('float32').reshape((len(y_train),1))
  y_test = np.asarray(y_test).astype('float32').reshape((len(y_test),1))
  y_val = np.asarray(y_val).astype('float32').reshape((len(y_val),1))

  # Como tenemos un array 2D, lo aplanamos para que tenga la siguiente dimension: `(n_samples,)`
  y_train = y_train.ravel()
  y_test = y_test.ravel()
  y_val = y_val.ravel()

  return  y_train, y_test, y_val
  
def transformacion_datos_y(y_train, y_test, y_val):
  # Conversion de v targets a numéricas
  targets = [y_train, y_test, y_val]
  # Crear diccionario con los nombres de las clases y sus valores numericos
  d = {'Blight':0, 'Common_Rust':1, 'Gray_Leaf_Spot':2, 'Healthy':3}

  # Iteramos en train-test-val:
  for y in targets:
    # Itermaos en y
    for i, clase in enumerate(y): #enumerate() devuelve una tupla que contiene el índice de la clase en la lista y la clase en sí misma
      y[i] = d[clase]

  # Transformamos: en numpy arrays, tipo float y redimensionamos:
  y_train = np.asarray(y_train).astype('float32').reshape((len(y_train),1))
  y_test = np.asarray(y_test).astype('float32').reshape((len(y_test),1))
  y_val = np.asarray(y_val).astype('float32').reshape((len(y_val),1))

  return  y_train, y_test, y_val




#----------------------------------------------#
## Modelado ##

def plot_confusion_matrix(y_test, y_pred, title='Matriz de Confusión'):
    # Clases:
    clases = ['Blight','Common_Rust','Gray_Leaf_Spot','Healthy']
    # Calcular la matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    
    # Calcular los porcentajes
    # cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100 

    # Configurar el gráfico
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt="d", cmap='BuGn', xticklabels=clases, yticklabels=clases)
    plt.title(title)
    plt.xlabel('Predicted label')
    plt.xticks(rotation=45)
    plt.ylabel('True label')
    plt.yticks(rotation=0)
    plt.show()

#----------------------------------------------#
## Metricas ##

# Classification Report

def classification_report(y_pred,y_test):
  
  # Diccionarios de Mapeos para las etiquetas:
  clases_a_cat = {0:'Blight',
                        1:'Common_Rust',
                        2:'Gray_Leaf_Spot',
                        3:'Healthy'}
  '''
  y_pred: Transformamos las predicciones de las imagenes en 
          formato categorico (nombres de las clases)
  
  y_test: Transformamos de numerico a categorica 
          los valores de y_test
  
  '''
  # Mapeamos y_pred e y_test a variables categoricas:
  y_pred = [clases_a_cat[prediccion] for prediccion in y_pred] 
  y_test = [clases_a_cat[y_num] for y_num in y_test] 

  return print(classification_report(y_test, y_pred))


# Matriz de Confusión 

def plot_confusion_matrix(y_test, y_pred, title='Matriz de Confusión'):
    # Clases:
    clases = ['Blight','Common_Rust','Gray_Leaf_Spot','Healthy']
    # Calcular la matriz de confusión
    cm = confusion_matrix(y_test, y_pred)

    # Calcular los porcentajes
    # cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100

    # Configurar el gráfico
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt="d", cmap='BuGn', xticklabels=clases, yticklabels=clases)
    plt.title(title)
    plt.xlabel('Predicted label')
    plt.xticks(rotation=45)
    plt.ylabel('True label')
    plt.yticks(rotation=0)
    plt.show()

# ROC Curve

def plot_ROC_Curve(y_pred, y_test):

  y_pred = [clases_a_num[prediccion] for prediccion in y_pred] 
  y_test = [clases_a_num[y_num] for y_num in y_test] 


  # Etiquetas para las clases
  class_labels = ['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy']

  # Binarizamos las etiquetas de y_test e y_pred:
  y_test_binarized = label_binarize(y_test, classes=[0, 1, 2, 3])
  y_pred_binarized = label_binarize(y_pred, classes=[0, 1, 2, 3])

  # Calcular la ROC y el AUC para cada clase
  fpr = dict()
  tpr = dict()
  roc_auc = dict()
  n_classes = y_test_binarized.shape[1]

  for i in range(n_classes):
      fpr[i], tpr[i],_ = roc_curve(y_test_binarized[:, i], y_pred_binarized[:, i])
      roc_auc[i] = auc(fpr[i], tpr[i])

  # Calcular la ROC promedio y el AUC
  fpr["micro"], tpr["micro"], thresholds = roc_curve(y_test_binarized.ravel(), y_pred_binarized.ravel())
  roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

  # Graficar todas las curvas ROC
  plt.figure()
  plt.plot(fpr["micro"], tpr["micro"], color='deeppink', linestyle=':', linewidth=4, label='Curva ROC promedio (area = {0:0.2f})'.format(roc_auc["micro"]))

  colors = ['aqua', 'darkorange', 'cornflowerblue', 'darkred']
  for i, color in zip(range(n_classes), colors):
      plt.plot(fpr[i], tpr[i], color=color, lw=2, label='ROC clase {0} (area = {1:0.2f})'.format(class_labels[i], roc_auc[i]))

  plt.plot([0, 1], [0, 1], 'k--', lw=2)
  plt.xlim([0.0, 1.0])
  plt.ylim([0.0, 1.05])
  plt.xlabel('Tasa de Falsos Positivos')
  plt.ylabel('Tasa de Verdaderos Positivos')
  plt.title('Curva ROC Multiclase')
  plt.legend(loc="lower right")
  plt.show()











    