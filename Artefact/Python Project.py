import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("lc-2025-computer-science-firebase-adminsdk-5i2lh-9ab47d6f17.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://lc-2025-computer-science-default-rtdb.europe-west1.firebasedatabase.app/"})


df = pd.read_csv("POKEMON_DATASET.csv")
df = df.rename(columns={"#": "Pokedex Number", "Sp. Atk": "special attack", "Sp. Def": "special defence", "Type 1": "type1", "Type 2": "type2"})   #renaming to make it simpler to identify each column
df.columns = df.columns.str.upper() # setting all columns uppercase for less error


df["NAME"] = df["NAME"].str.replace("Mime Jr.", "Mime Jr")  #Contained an illegal character "." 
df = df.fillna("Pure")                                      #Filling all blank cells with Pure as only blank cells were secondary pokemon types, also makes it easy to identify pokemon with only one type as a pure pokemon

df = df.drop_duplicates(subset=['POKEDEX NUMBER'], keep="first") # <-- Drops duplicates , duplicates contained mega evolutions of Pokemon with the same Pokedex no. , megas were unnecessary for this investigation 

# print(df.info())  <--- to check that all columns contained the same amount of cells and also to identify their data type

df_json = df.to_json(orient="records") # convert dataframe to json
#dictionary = df.to_dict() # <-- csv as dictionary
#root_ref = db.reference("") 
#root_ref.child("POKEMON_DATASET_cleaned").set(dictionary)   # sets a new cleaned dataframe from the modified/cleaned dictionary 
df.to_csv("POKEMON_DATASET_cleaned.csv", index=False) # converts dataframe to a csv file

df2 = pd.read_csv("POKEMON_DATASET_cleaned.csv")
dictionary2 = df2.to_dict()
root_ref = db.reference("")
root_ref.child("POKEMON_DATASET_cleaned").set(dictionary2)




