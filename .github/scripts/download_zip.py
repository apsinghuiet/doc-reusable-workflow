import requests
import os

def download_zip(api_url, temp_location):
    response = requests.get(api_url, stream=True)

    if response.status_code == 200:
        with open(temp_location, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"ZIP file downloaded and saved to: {temp_location}")
    else:
        print(f"Failed to download ZIP file. Status code: {response.status_code}")

if __name__ == "__main__":
    # Set the URL of the API endpoint that provides the ZIP file
    api_url = "https://www.free-css.com/assets/files/free-css-templates/download/page296/mediplus-lite.zip"

    # Set the temporary location to save the ZIP file
    temp_location = "/tmp/downloaded.zip"

    download_zip(api_url, temp_location)
