import requests

def get_website_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    url = "https://www.github.com"
    print(f"Status code for {url}: {get_website_status(url)}")
