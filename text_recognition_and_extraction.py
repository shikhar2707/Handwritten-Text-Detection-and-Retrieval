#!/usr/bin/env python
# coding: utf-8
#Handwritten Text Detection & Extraction using Google Cloud Vision API
# In[2]:


#Installing required libraries
get_ipython().system('pip install google-cloud')


# In[3]:


get_ipython().system('pip install google-cloud-vision')


# In[1]:


#importing the required libraries.
import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd


# In[2]:


#This is an important step. It authenticates your id to use the Google API services.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"ServiceAccountToken.json"
client = vision.ImageAnnotatorClient()


# In[5]:


Folder = "Downloads/Buffalo_Dataset-20200406T093405Z-001/Buffalo_Dataset"#Includes the path where the dataset or the files are.
for file in os.listdir(Folder):
    folder_name = file.split(".")
    output_folder = Folder + "/" + str(folder_name[0])
    if not os._exists(output_folder):
        os.makedirs(output_folder)
        File_Path = os.path.join(Folder,file)
        with open(File_Path, 'rb') as file: #opening binary readable file.
            content = file.read()
            image = vision.types.Image(content=content)
            response = client.document_text_detection(image = image)
            docText = response.full_text_annotation.text
            #Storing the output to a .txt file as required.
            f = open(output_folder+ '/' + str(folder_name[0]) + ".txt" , 'w', encoding="utf-8")
            f.write(docText)
            f.close()


# In[12]:


#Below is a sample output.


# In[14]:





# In[ ]:




