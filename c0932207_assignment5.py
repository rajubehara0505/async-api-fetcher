import asyncio
import aiohttp
import json
import threading

# Define the API endpoint
API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"

# Define the file to save the data
FILE_NAME = "data.json"

# Define an asynchronous function to fetch data from the API
async def fetch_data(session):
    try:
        # Make an asynchronous GET request to the API endpoint
        async with session.get(API_ENDPOINT) as response:
            # Wait for the response to be ready
            data = await response.json()
            # Return the fetched data
            return data
    except aiohttp.ClientError as e:
        # Handle any errors that occur during the request
        print(f"Error fetching data: {e}")
        # Return None if an error occurs
        return None

# Define a function to process the fetched data
def process_data(data):
    # Process the data as required (e.g., select specific fields)
    # In this example, we're selecting only the 'id' and 'title' fields
    processed_data = [{"id": post["id"], "title": post["title"]} for post in data]
    # Return the processed data
    return processed_data

# Define a function to write the data to a file
def write_data_to_file(data):
    # Open the file in write mode
    with open(FILE_NAME, "w") as f:
        # Use the json module to dump the data to the file
        json.dump(data, f, indent=4)

# Define the main asynchronous function
async def main():
    # Create an aiohttp client session
    async with aiohttp.ClientSession() as session:
        # Fetch the data from the API
        data = await fetch_data(session)
        if data:
            # Process the fetched data
            processed_data = process_data(data)
            # Create a separate thread to write the data to the file
            threading.Thread(target=write_data_to_file, args=(processed_data,)).start()

# Run the main function
if __name__ == "__main__":
    # Use asyncio to run the main function
    asyncio.run(main())s