import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cred = credentials.Certificate("lc-2025-computer-science-firebase-adminsdk-5i2lh-9ab47d6f17.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://lc-2025-computer-science-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/POKEMON_DATASET_cleaned") 
dictionary = ref.get() #Grabbing Cleaned Dataset from firebase

def TypeGen(dictionary,generation):
	total_pure = {}
	for i,j in enumerate(dictionary['GENERATION']): #adds a counter to every item in the list
		if j == generation:
			if dictionary['TYPE1'][i] in total_pure:
				total_pure[dictionary['TYPE1'][i]] = total_pure[dictionary['TYPE1'][i]]+1   #frequency of pokemon type increasing by one if pokemon type exists in dictionary
				
			else:
				total_pure[dictionary['TYPE1'][i]] = 1   # creates a new key in dictionary to contain new type
				
	return(total_pure)






gen1 = TypeGen(dictionary,1)    # Counts the frequency of Pokemon that also share Generation : 1
gen1_types = list(gen1.keys())
gen1_values = list(gen1.values())
plt.pie(gen1_values, labels = gen1_types)
plt.title("Gen 1 Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")
plt.show()
ref = db.reference("/TypeGen1/")
ref.set(gen1)


gen2 = TypeGen(dictionary,2)    # Counts the frequency of Pokemon that also share Generation : 2
gen2_types = list(gen2.keys())
gen2_values = list(gen2.values())
plt.pie(gen2_values, labels = gen2_types)
plt.title("Gen 2 Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")
plt.show()
ref = db.reference("/TypeGen2/")
ref.set(gen2)


gen3 = TypeGen(dictionary,3)  # Counts the frequency of Pokemon that also share Generation : 3
gen3_types = list(gen3.keys())
gen3_values = list(gen3.values())
plt.pie(gen3_values, labels = gen3_types)
plt.title("Gen 3 Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")
plt.show()
ref = db.reference("/TypeGen3/")
ref.set(gen3)


gen4 = TypeGen(dictionary,4)  # Counts the frequency of Pokemon that also share Generation : 4
gen4_types = list(gen4.keys())
gen4_values = list(gen4.values())
plt.pie(gen4_values, labels = gen4_types)
plt.title("Gen 4 Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")
plt.show()
ref = db.reference("/TypeGen4/")
ref.set(gen4)

 
gen5 = TypeGen(dictionary,5)  # Counts the frequency of Pokemon that also share Generation : 5
gen5_types = list(gen5.keys())
gen5_values = list(gen5.values())
plt.pie(gen5_values, labels = gen5_types)
plt.title("Gen 5 Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")
plt.show()
ref = db.reference("/TypeGen5/")
ref.set(gen5)


gen6 = TypeGen(dictionary,6)  # Counts the frequency of Pokemon that also share Generation : 6
gen6_types = list(gen6.keys())
gen6_values = list(gen6.values())
plt.pie(gen6_values, labels = gen6_types)
plt.title("Gen 6 Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")
plt.show()
ref = db.reference("/TypeGen6/")
ref.set(gen6)







