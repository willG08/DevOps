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

def get_starships():
    global unique_pilots, unique_starship_films

    ###################Starships#######################
    # Divider line
    print("\n" + "="*50)  
    # Starships Header
    print("Star Wars Starships Information")  
    # Divider Line
    print("="*50)

    # Define the URL for the Star Wars API Endpoint for Starships 
    starships_url = "https://swapi.dev/api/starships/"

    # Create a unique list of all pilot urls
    unique_pilots = set()

    # Create a unique list of all film urls, commented out because it is not in use
    unique_starship_films = set()

    # Iterator for starship count for easier reading
    iterator = 1

    # List all of the starships in the API
    # While there is still a next page, keep iterating through the pages to get the data
    while True:
        # Get the data for starships from the current page
        x = get_data_from_api(starships_url)
        # Loop through the starships of the current page of the API
        for starship in x["results"]:
            # Print the starship header with starship number
            print(f"\nStarship {iterator}")
            # Increment the iterator
            iterator += 1

            # Print the starship details
            print(f"Name: {starship['name']}")
            print(f"Starship Class: {starship['starship_class']}")
            print(f"Model: {starship['model']}")
            print(f"Length: {starship['length']}")
            print(f"Crew: {starship['crew']}")
            print(f"Passengers: {starship['passengers']}")
            print(f"Cost in Credits: {starship['cost_in_credits']}")

            # Additional features that are not currently used in the program
            # print(f"Manufacturer: {starship['manufacturer']}")
            # print(f"Max Atmosphering Speed: {starship['max_atmosphering_speed']}")
            # print(f"Cargo Capacity: {starship['cargo_capacity']}")
            # print(f"Consumables: {starship['consumables']}")
            # print(f"Hyperdrive Rating: {starship['hyperdrive_rating']}")
            # print(f"MGLT: {starship['MGLT']}")
            # print(f"Created: {starship['created']}")
            # print(f"Edited: {starship['edited']}")
            # print(f"URL: {starship['url']}")

            # Add the pilot to the set of unique pilots
            unique_pilots.update(starship['pilots'])

            # Add the film to the set of unique films
            unique_starship_films.update(starship['films'])

        # After retrieving the information from this page select the next page of the API 
        next = x["next"]

        # If there is no next page, break the loop
        if next is None:
            break

        # Select the next page of the API
        else:
            # Store the url for the next page of the API
            starships_url = next

def get_pilots():
    global unique_pilot_films, unique_pilot_species, unique_pilot_vehicles, unique_pilot_starships
    ###################Pilots#######################
    # Divider Line
    print("\n" + "="*50) 
    # Pilot header
    print("Star Wars Pilots Information")  
    # Divider Line
    print("="*50)

    # Create a unique list of film, species, vehicle, and starship urls attached to a pilot, commented out because it is not in use
    unique_pilot_films = set()
    unique_pilot_species = set()
    unique_pilot_vehicles = set()
    unique_pilot_starships = set()

    # Reset Iterator for pilot count
    iterator = 1

    # Loop through the unique pilots set and retrieve data for each pilot
    for p in unique_pilots:
        # Get the data for pilots from the current page
        pilot = get_data_from_api(p)

        # Print the pilot header with number
        print(f"\nPilot {iterator}")

        # Increment the iterator
        iterator += 1

        # Print the pilot details
        print(f"Name: {pilot['name']}")
        print(f"Height: {pilot['height']}")
        print(f"Mass: {pilot['mass']}")
        print(f"Hair Color: {pilot['hair_color']}")
        print(f"Skin Color: {pilot['skin_color']}")
        print(f"Eye Color: {pilot['eye_color']}")
        print(f"Birth Year: {pilot['birth_year']}")
        print(f"Gender: {pilot['gender']}")

        # Features that are not currently used in the program
        # print(f"Homeworld: {pilot['homeworld']}")
        # print(f"Created: {pilot['created']}")
        # print(f"Edited: {pilot['edited']}")
        # print(f"URL: {pilot['url']}")

        unique_pilot_films.update(pilot['films'])
        unique_pilot_species.update(pilot['species'])
        unique_pilot_vehicles.update(pilot['vehicles'])
        unique_pilot_starships.update(pilot['starships'])



###################Introduction#######################
# Print Project Name
print(f"\nStar Wars API Starships and Pilots Information")
# Print Name 
print("By: Will Gunther")

get_starships()

get_pilots()

###################Show Unique URL Lists#######################
# Ask the user if they want to see the unique lists of URLs, remove blank space and make lowercase
show_unique_lists = input(f"\nDo you want to see the unique lists of URLs? (yes/no): ").strip().lower()

if show_unique_lists == 'yes':
    ###################Unique Starship URL Lists#######################
    # Included this to show we have unique starship lists ready to be manipulated

    # Divider Line
    print("\n" + "="*50) 
    # Pilot header
    print("Star Wars Unique Starship URL Lists")  
    # Divider Line
    print("="*50)

    # Print the unique lists of pilots and films from starships
    print(f"\nUnique Pilots: {unique_pilots}")
    print(f"\nUnique Starship films: {unique_starship_films}")

    ###################Unique Pilot URL Lists#######################
    # Included this to show we have unique pilot lists ready to be manipulated

    # Divider Line
    print("\n" + "="*50) 
    # Pilot header
    print("Star Wars Unique Pilot URL Lists")  
    # Divider Line
    print("="*50)

    # Print the unique lists of pilots, films, species, vehicles, and starships from pilots
    print(f"\nUnique Pilots: {unique_pilots}")
    print(f"\nUnique Pilot films: {unique_pilot_films}")
    print(f"\nUnique Pilot Species: {unique_pilot_species}")
    print(f"\nUnique Pilot Vehicles: {unique_pilot_vehicles}")
    print(f"\nUnique Pilot Starships: {unique_pilot_starships}\n")



    ###################End of Program#######################