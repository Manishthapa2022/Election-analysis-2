from calendar import c
print ("Hello World")
counties=["Arapahoe","Denver","Jefferson"]
# to print the number of items in a list 
print(len(counties))
# working with tuples
counties_tuple=["Arapahoe","Denver","Jefferson"]
# print(len(counties_tuple))
print(counties_tuple[1])
#creating dictionaries open one where you can input values
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.keys())
# to get values from the dictonary
print(counties_dict.get("Denver"))
# adding items to dictionary and further work
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)





















