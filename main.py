import requests

# Store the Star Wars API
starships_url = "https://swapi.dev/api/starships/"

# Creates a variable storing the URL for the Star Wars API endpoint for starships
startships_response = requests.get(starships_url)

# This prints the Response object
print(startships_response)  
# Print the status code
print(startships_response.status_code)  
# Print the actual JSON response
print(startships_response.json())  

# Records the response in a variable
x = startships_response .json()
# Stores the next page of the API
next = x["next"]
# Stores the total count of starships
# count = x["count"]
print(x["count"])

# for i in x["results"]:
#     print(i["starship_class"])

iterator = 0

# List all of the startships in the API
# While there is still a next page, keep iterating through the pages
while next is not None:
    startships_response = requests.get(next)
    x = startships_response.json()
    next = x["next"]
    for i in x["results"]:
        print(i["starship_class"])
        iterator += 1

