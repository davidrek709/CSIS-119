import urllib.request
import json

# Function to get country data from the REST Countries API
def get_country_data(country_name):
    base_url = "https://restcountries.com/v3.1/name/"
    try:
        # Construct the URL
        url = f"{base_url}{country_name}"
        # Make the API request
        with urllib.request.urlopen(url) as response:
            # Read and decode the response
            data = response.read().decode('utf-8')
            # Parse the JSON data
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} for {country_name}")
        return None
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
        return None
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")
        return None

# Prompt user for a country name
country = input("Enter a country name: ")

# Boolean variable to track if data was fetched
data_fetched = False

# Call the function to get country data
country_data = get_country_data(country)

# Ensure that data is available and is a valid country (uses if statement)
if country_data and isinstance(country_data, list):
    data_fetched = True  # Set boolean to True if data is fetched successfully

# Parse the data if it was fetched successfully
if data_fetched:
    # Work with the first country in the result (some countries have multiple results)
    country_info = country_data[0]

    # String, integer, and float variables
    country_name = country_info.get("name", {}).get("common", "Unknown")  # String
    population = country_info.get("population", 0)  # Integer
    area = country_info.get("area", 0.0)  # Float

    # Print basic country information
    print(f"\nCountry: {country_name}")
    print(f"Population: {population}")
    print(f"Area: {area} km²")

    # Check if the population is above or below a certain threshold (if statement)
    if population > 50_000_000:
        print("This is a highly populated country!")
    else:
        print("This is not a very highly populated country.")

    # Use of list and dictionary to parse and display languages spoken (Module 5 and 6)
    languages = country_info.get("languages", {})
    print("\nLanguages spoken:")
    for lang_code, language in languages.items():
        print(f"- {language} (Code: {lang_code})")

    # Use of a set to store unique continents/regions (set usage, Module 6)
    regions_set = set()
    region = country_info.get("region", "Unknown")
    subregion = country_info.get("subregion", "Unknown")
    regions_set.add(region)
    regions_set.add(subregion)

    # Print the unique regions/subregions
    print("\nRegions:")
    for reg in regions_set:
        print(f"- {reg}")

else:
    print(f"Could not retrieve data for {country}.")

# Bonus: Loop to allow user to check multiple countries
while True:
    another_country = input("\nDo you want to check another country? (yes/no): ").lower()
    if another_country == 'yes':
        country = input("Enter another country name: ")
        country_data = get_country_data(country)
        
        if country_data and isinstance(country_data, list):
            country_info = country_data[0]
            population = country_info.get("population", 0)
            print(f"\nPopulation in {country}: {population}")
        else:
            print(f"Could not retrieve data for {country}.")
    else:
        print("Exiting program.")
        break
