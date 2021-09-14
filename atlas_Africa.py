from arcpy import *
from arcpy.mapping import *
import os

mxd=GetParameterAsText(0)
date_debut=GetParameter(1)
date_fin=GetParameter(2)
output_pdf=GetParameterAsText(3)

file_name="ATLASCOVID.pdf"                    #le nom du pdf Atlas
full_path= os.path.join(output_pdf, file_name) #le chemin vers le pdf atlas
Atlas=PDFDocumentCreate (full_path)         #creation d'un fichier pdf

Atlas.appendPages(r"C:\Users\M\Desktop\pagepremeire.pdf") #ajout de la premiere page de garde


mxd=MapDocument(mxd)


df1Time = ListDataFrames(mxd)[0].time  #on a 2 data frames
df2Time = ListDataFrames(mxd)[1].time
df1Time.currentTime = date_debut       #ajustation de la date a la date debut entré par ml'utilisateur
df2Time.currentTime = date_debut



while df1Time.currentTime <= date_fin:  #on travaille sur un atlas de la date debut a la date fin
    name="temporaire.pdf"          
    df1Time.currentTime = df1Time.currentTime 
    df2Time.currentTime = df1Time.currentTime
    
    ExportToPDF(mxd,os.path.join(output_pdf,name)) #des pdfs temporaires (1 page correspondant au statistiques d'une date) sont crees
    Atlas.appendPages(os.path.join(output_pdf,name)) #dans le pdf deja crée on ajoute le pdf temporaire
    df1Time.currentTime = df1Time.currentTime + df1Time.timeStepInterval #l'intervalle de temps est  un jour (defini sur le time slider)
    
 
    
Atlas.appendPages(r"C:\Users\M\Desktop\logo.pdf")  #ajout de la derniere page de garde 
Atlas.saveAndClose () #enregistrement  de l'atlas














