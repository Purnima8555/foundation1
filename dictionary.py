"""
It is always represent in the form of:
my_dictionary = {"key":"Value"}
"""

# why we need dictionary?
#--> To overcome the problem exist in list.
#for eg:
#user_detail=["Purnima","Rana",18,["English","Nepali","Japanese"]9845141112,{"Burger","Pizza","Momo"}]

user_details = {
    "First_name":"Purnima",
    "Last_name":"Rana",
    "Language-spoken":["English","Nepali","Japanese"],
    "contact":9845141112,
    "fav_food":["Burger","Pizza","Momo"]
}

#print(user_details["First_name"])

for key,value in user_details,iter():
    print(f"The key is:{key} and its value is: {value}")

for key in user_details.keys():
    print(f"The key is:{key}")

for value in user_details.values():\
    print(f"")