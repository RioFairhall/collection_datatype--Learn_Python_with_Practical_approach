            '''Let's learn about Dictionary in Python'''

#using list in a unefficient mannar
shopping_list= ["Milk", "2pkt", "Soap", 1, "Coffee Powder", "2pkt"]
print(shopping_list)


'''
solution to our problem
|
v
Dictionary '''

#creating a Dictionary value
{"Milk":"2pkt"} #it become a 'key-value' pair
print(type({"Milk":"2pkt"})) #verifyting the type -> 'dict' - dictionary

#creating and accessing a dictionary variable
my_shopping_dictionary={"Milk":"2pkt", "Soap":1} #creating a dictionary variable
print(my_shopping_dictionary["Milk"]) #accessing value of "Milk" key from the dictionary name, "my_shopping_dictionary"
print(my_shopping_dictionary.keys())

#updating or changing a value of a key in a dictionary
my_shopping_dictionary["Milk"] = "3pkt"
print(my_shopping_dictionary)
print(my_shopping_dictionary["Milk"])

#add a key:value pair in already created dictionary
#key:value
my_shopping_dictionary["Coffee Powder"]= "2pkt"
print(my_shopping_dictionary)

#checking if successfully added or not
if( "Coffee Powder" in my_shopping_dictionary.keys()):
    print("Already Present")
else:
    print("Adding new value....")
    print(my_shopping_dictionary)
    
    
#using update command to add one or more key-value pair
my_shopping_dictionary.update({"Eggs":5, "Bread":"1pkt"}) #pass that value inside thw update()
print(my_shopping_dictionary)

#with creating a new dictionary variable
new_items = {"Butter":"500g","Sugar":"1kg"} #creating a dictionay value which you want to add
my_shopping_dictionary.update(new_items) #pass that value inside thw update()
print(my_shopping_dictionary)

#removing a key-value pair from a dictionary
print(my_shopping_dictionary.pop("Soap"))
print(my_shopping_dictionary)

#checking if successfully remove or not
if( "Soap" in my_shopping_dictionary.keys()):
    print("Not Removed from the Dictionary, try again..")
else:
    print("Removed Successfully!!")
    print(my_shopping_dictionary)
    

#deleting your dictionary variable
del my_shopping_dictionary

#checking if "my_shopping_dictionary" successfully delete or not
try:
    print(my_shopping_dictionary) #will give an error, "my_shopping list- not defined"
except:
    print("my_shopping_dictionary got deleted successfully!!")
    