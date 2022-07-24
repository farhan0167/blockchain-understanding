"""
json.dumps() function converts a Python object into a json string.
"""
import json
 
# Creating a dictionary
Dictionary ={1:'Welcome', 2:'to',
            3:'Geeks',5:'Geeks', 4:'for',
            }
  
# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary, sort_keys=True)
print('Equivalent json string of input dictionary:', json_string.encode())

out_file = open("json-dump.json", "w")
json.dump(Dictionary,out_file, indent=6)

out_file.close()