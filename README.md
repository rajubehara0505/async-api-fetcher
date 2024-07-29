# async-api-fetcher
Async API Fetcher
A Python script that asynchronously fetches data from a JSON API endpoint, processes the data, and writes it to a file.

Overview

This script uses the aiohttp library to make an asynchronous GET request to the JSONPlaceholder API, which returns a list of posts. The script then processes the data by selecting only the id and title fields, and writes the processed data to a file named data.json.

Features

Asynchronous API request using aiohttp
Data processing using list comprehension
Writing data to a file using the json module
Error handling for API request failures
Usage

Clone the repository: git clone https://github.com/your-username/async-api-fetcher.git
Install the required libraries: pip install aiohttp json
Run the script: python main.py
Notes

This script uses a separate thread to write the data to the file, allowing the main thread to continue executing without blocking.
The data.json file will be created in the same directory as the script.
