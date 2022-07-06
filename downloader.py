import requests

# download image or pdf file
def download(url, tag, upload_folder):
    try:
        data = requests.get(url)
        # image tag must contain jpg
        with open(f"{upload_folder}/{tag}", "wb") as handler:
            handler.write(data)
    except:
        print(f"Kunne ikke laste ned fil med tag: {tag}")