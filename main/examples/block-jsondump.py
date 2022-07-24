"""
json.dumps() function converts a Python object into a json string.
"""
import json
 
# Creating a dictionary
block = {
            'index': 1,
            'timestamp': 1506057125.900785,
             "transactions": [
                {
                    "sender": "8527147fe1f5426f9dd545de4b27ee00",
                    "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
                    "amount": 5
                }
            ],
            'proof': 324984774000,
            'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        }
  
# Converts input dictionary into
# string and stores it in json_string


out_file = open("json-dump-block.json", "w")
json.dump(block,out_file, indent=6)

out_file.close()