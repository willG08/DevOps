# Star Wars API Starships and Pilots Information From SWAPI (https://swapi.dev/)
# Author: Will Gunther
# Project Name: Star Wars API Starships and Pilots Information
# Project Description: This project retrieves and displays information about starships and pilots from the Star Wars API (SWAPI).
# It includes details such as name, model, crew, passengers, and more for each starship and pilot. The project also collects unique
# URLs for pilots and films associated with the starships and pilots.

import requests, time

###################Method for Retrieving Data for Error Handling#######################
# Stores the maximum number of retries for a timed out request
MAX_RETRIES = 3

# Function to make a GET request to a given URL with built-in error handling and retry logic for timeouts.
# Retries the request up to 3 times in case of a timeout, with a 5-second wait between retries.
def get_data_from_api(url, retries=0):
    try:
        # Make a GET request to the provided URL, with a 10 second timeout
        response = requests.get(url, timeout=10)  
        # Raise exception for non-200 status codes
        response.raise_for_status()  
        # Return the JSON response if the request is successful
        return response.json()
    # Handle Timeout Exception
    except requests.exceptions.Timeout:
        if retries < MAX_RETRIES:
            print(f"Request timed out. Retrying... (Attempt {retries + 1})")
            # Wait 5 seconds before retrying
            time.sleep(5)  
            # Retry the request
            return get_data_from_api(url, retries + 1)  
        else:
            print("Max retries reached. Exiting...")
            return None
    # Handle Exceptions for other HTTP errors
    except requests.exceptions.RequestException as e:
        # Print the error message and return None
        print(f"An error occurred: {e}")
        return None 
    

 ###################Starships#######################
def get_starships():

    # Define the URL for the Star Wars API Endpoint for Starships 
    starships_url = "https://swapi.dev/api/starships/"

    # Initialize the list of starships
    starships = []

    # Create a unique list of all pilot urls, used with the get_pilots function
    unique_pilots = set()

    # List all of the starships in the API
    # While there is still a next page, keep iterating through the pages to get the data
    while True:
        # Get the data for starships from the current page
        x = get_data_from_api(starships_url)

        # If the data is None, break the loop
        if x is None:
            break

        # Loop through the starships of the current page of the API
        for starship in x["results"]:

            # Store all of the starship information in a starship dictionary
            starship_dict = {
                "Name": starship['name'],
                "Model": starship['model'],
                "Manufacturer": starship['manufacturer'],
                "Cost in Credits": starship['cost_in_credits'],
                "Length": starship['length'],
                "Max Atmosphering Speed": starship['max_atmosphering_speed'],
                "Crew": starship['crew'],
                "Passengers": starship['passengers'],
                "Cargo Capacity": starship['cargo_capacity'],
                "Consumables": starship['consumables'],
                "Hyperdrive Rating": starship['hyperdrive_rating'],
                "MGLT": starship['MGLT'],
                "Starship Class": starship['starship_class'],
                "Pilots": starship['pilots'],
                "Films": starship['films'],
                "Created": starship['created'],
                "Edited": starship['edited'],
                "URL": starship['url']
            }

            
            # Append the dictionary to the list
            starships.append(starship_dict)

            # Used in the get_pilots function, Add the pilot to the set of unique pilots
            unique_pilots.update(starship['pilots'])

        # After retrieving the information from this page select the next page of the API 
        next = x["next"]

        # If there is no next page, break the loop
        if next is None:
            return starships, unique_pilots
            break

        # Select the next page of the API
        else:
            # Store the url for the next page of the API
            starships_url = next


def print_starships(all_starships, all_people):
    # Divider line
    print("\n" + "="*50)  
    # Starships Header
    print("Star Wars Starships Information")  
    # Divider Line
    print("="*50)

    iterator = 1

    # Print the starship header with starship number
    for starship in all_starships:
        # Print the starship header with starship number
        print(f"\nStarship {iterator}")
        # Increment the iterator
        iterator += 1
        # Print the starship details
        print(f"Name: {starship['Name']}")
        print(f"Starship Class: {starship['Starship Class']}")
        print(f"Model: {starship['Model']}")
        print(f"Length: {starship['Length']}")
        print(f"Crew: {starship['Crew']}")
        print(f"Passengers: {starship['Passengers']}")
        print(f"Cost in Credits: {starship['Cost in Credits']}")

        # Check if the pilots list is empty
        if starship['Pilots'] == []:
            # Print the pilots header
            print("Pilots: None")
        else:
            # Print the pilots header
            print("Pilots:", end=" ")
            # Set first Pilot to true
            first_pilot = True

            # Look through the list of people 
            for pilot in all_people:
                # If the current pilot's url is found in the starships' list of pilot URLs print it out
                if pilot['URL'] in starship['Pilots']:
                    # If this is the first pilot don't print a comma and stay on the same print line
                    if first_pilot:
                        first_pilot = False
                        print(f"{pilot['Name']}", end="")
                    # If this is not the first pilot print a comma to separate the prior pilot
                    else:
                        print(f", {pilot['Name']}", end="")

            # Print a blank line to clear the end of the document
            print()


###################Pilots#######################
def get_pilots(unique_pilots):

    # Create a unique list of film, species, vehicle, and starship urls attached to a pilot, commented out because it is not in use
    pilots = []

    # Loop through the unique pilots set and retrieve data for each pilot
    for p in unique_pilots:
        # Get the data for pilots from the current page
        pilot = get_data_from_api(p)

        if pilot is None:
            return None

        # Create a Dictionary with all of the pilot information
        pilot_dict = {
                "Name": pilot['name'],
                "Height": pilot['height'],
                "Mass": pilot['mass'],
                "Hair Color": pilot['hair_color'],
                "Skin Color": pilot['skin_color'],
                "Eye Color": pilot['eye_color'],
                "Birth Year": pilot['birth_year'],
                "Gender": pilot['gender'],
                "Homeworld": pilot['homeworld'],
                "Films": pilot['films'],
                "Species": pilot['species'],
                "Vehicles": pilot['vehicles'],
                "Starships": pilot['starships'],
                "Created": pilot['created'],
                "Edited": pilot['edited'],
                "URL": pilot['url']
            }
        
        # Append the dictionary to the list
        pilots.append(pilot_dict)

    # Return pilots, a list of dictionaries for pilots once they are all collected
    return pilots

def print_people(people):
    # Divider line
    print("\n" + "="*50)
    # Pilot Header
    print("Star Wars People Information")
    # Divider Line
    print("="*50)

    iterator = 1

    # Print the pilot header with number
    for person in people:
        # Print the pilot header with number
        print(f"\nPerson {iterator}")
        # Increment the iterator
        iterator += 1
        # Print the relevant pilot details
        print(f"Name: {person['Name']}")
        print(f"Height: {person['Height']}")
        print(f"Mass: {person['Mass']}")
        print(f"Hair Color: {person['Hair Color']}")
        print(f"Skin Color: {person['Skin Color']}")
        print(f"Eye Color: {person['Eye Color']}")
        print(f"Birth Year: {person['Birth Year']}")
        print(f"Gender: {person['Gender']}")
        # print(f"Homeworld: {person['Homeworld']}")
        # print(f"Created: {person['Created']}")
        # print(f"Edited: {person['Edited']}")
        # print(f"URL: {person['URL']}")

###################Everyone###########################
# Get Everyone from the Star Wars API
def get_everyone():
    # Define the URL for the Star Wars API Endpoint for people 
    people_url = "https://swapi.dev/api/people/"

    # Initialize the list of people
    people = []

    # List all of the people_url in the API
    # While there is still a next page, keep iterating through the pages to get the data
    while True:
        # Get the data for starships from the current page
        x = get_data_from_api(people_url)

        # If the data is None, break the loop
        if x is None:
            break

        # Loop through the people_url of the current page of the API
        for person in x["results"]:

             # Create a Dictionary with all of the people's information
            person_dict = {
                "Name": person['name'],
                "Height": person['height'],
                "Mass": person['mass'],
                "Hair Color": person['hair_color'],
                "Skin Color": person['skin_color'],
                "Eye Color": person['eye_color'],
                "Birth Year": person['birth_year'],
                "Gender": person['gender'],
                "Homeworld": person['homeworld'],
                "Films": person['films'],
                "Species": person['species'],
                "Vehicles": person['vehicles'],
                "Starships": person['starships'],
                "Created": person['created'],
                "Edited": person['edited'],
                "URL": person['url']
            }
        
            # Append the dictionary to the list
            people.append(person_dict)

        # After retrieving the information from this page select the next page of the API 
        next = x["next"]

        # If there is no next page, break the loop
        if next is None:
            return people
            break

        # Select the next page of the API
        else:
            # Store the url for the next page of the API
            people_url = next




###################Introduction#######################
# Print Project Name
print(f"\nStar Wars API Starships and Pilots Information")
# Print Name 
print("By: Will Gunther")

all_starships, unique_pilots = get_starships()

#all_people = get_pilots(unique_pilots)

all_people = get_everyone()

print_starships(all_starships, all_people)

#print_people(all_people)
