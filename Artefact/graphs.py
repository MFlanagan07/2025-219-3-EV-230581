import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cred = credentials.Certificate("lc-2025-computer-science-firebase-adminsdk-5i2lh-9ab47d6f17.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://lc-2025-computer-science-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/")
dictionary = ref.get()
#print(dictionary)
#print(len(dictionary))



def getaverage_stat(diction,stats,a,b):
	sums = 0
	
	for column,row in diction.items():
		for stat,value in row.items():
			if stat == str(stats):
				statpoints = value[a:b]
	for point in statpoints:
		sums += point
	average = sums / len(statpoints)
	return(average)	
	
gen1 = getaverage_stat(dictionary,"TOTAL",0,151)   
gen2 = getaverage_stat(dictionary,"TOTAL",152,251)
gen3 = getaverage_stat(dictionary,"TOTAL",252,386)        # <--- uses the function to calculate the mean average of total statpoints within the range of Pokedex Numbers Corresponding to their Generation Number
gen4 = getaverage_stat(dictionary,"TOTAL",387,493)
gen5 = getaverage_stat(dictionary,"TOTAL",494,649)
gen6 = getaverage_stat(dictionary,"TOTAL",650,799)
totalaverages = [round(gen1), round(gen2), round(gen3), round(gen4), round(gen5), round(gen6)]  # <--- rounding total average stats
height = ["GENERATION 1","GENERATION 2","GENERATION 3","GENERATION 4","GENERATION 5","GENERATION 6"] # Setting X-Axis Labels
average_dictionary = dict(zip(height, totalaverages)) # Making a dictionary with X-Axis Labels as Keys and list of average stat values as values
ref = db.reference("/AVERAGE_STATS/")  # creating a database on firebase to store the dictionary
ref.set(average_dictionary)  
plt.bar(height, totalaverages) 
plt.title("Average Stats Across First 6 Generations")
plt.xlabel("Average Stats")
plt.ylabel("Generations")
plt.show()   # <--- Test graph for what I would like to make on the website




typelist = []
for column,row in dictionary.items():
	for stat,value in row.items():
		if stat == "TYPE1":
			#print(value) # all types
			for _type in value:
				#print(_type) # individual types
				if _type not in typelist:
					typelist.append(_type)
					
typelist.append("Pure")  # creates a list of all types to be used in future calculations 
print(typelist)
#print(dictionary)
total_pure = {}  # dictionary to store the frequency pokemon types appear



for _type in typelist:  #for each type that appears in the list of types
	total_pure[_type] = 0    #create a key with value 0 in total_pure dictionary
for column,row in dictionary.items():  
	for stat,allvalues in row.items():  # for all values in each column
		if stat == "TYPE1":
			# print(allvalues) #all types in type1   
			for type_ in allvalues:				
				total_pure[type_] = total_pure[type_] + 1    #if there is a type that is in the dictionary in a checked row, add 1 to total amount of that type
		elif stat == "TYPE2": 
			# print(allvalues) # all types in type2 
			for type_ in allvalues:
				if type_ == "NONE": pass      # as not all pokemon have two types 
				total_pure[type_] = total_pure[type_] + 1    #repeat of L:76
				
				
total_nopure = {}   # secondary dictionary that wil not contain the pokemon type "Pure" as that does not exist in the games
print(total_nopure)
print(total_pure)
total_nopure.update(total_pure)
total_nopure.pop("Pure")   # removing key and associated values for "Pure"
types = list(total_nopure.keys())
values = list(total_nopure.values())
plt.pie(values, labels = types)   # pie chart showing a distribution of types across all generations
plt.title("Total Pokemon Type Frequency")
plt.xlabel("Pokemon Types")
plt.ylabel("Frequency")   
plt.show()
ref = db.reference("/Total_Types/")   # creating a databse in firebase to store this data
ref.set(total_nopure)  # setting the dictionary without Pure type Pokemon
















