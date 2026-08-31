# # Open the file and read lines into a list
# with open('/home/phantomMenace/portswigger_labs/Authentication/password.txt', 'r') as file:
#     # readlines() keeps the newline characters (\n)
#     usernames_list = file.read().splitlines()

# print(usernames_list)

import json

# Read the file and clean up the usernames
with open("/home/phantomMenace/portswigger_labs/Authentication/password.txt", 'r') as file:
    # Strips whitespace and filters out any blank lines
    usernames = [line.strip().strip("'\"") for line in file if line.strip()]

# Convert the Python list directly into a valid JSON string (uses double quotes)
json_list_string = json.dumps(usernames)

print(json_list_string)