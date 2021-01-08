import requests

def main():
    r = requests.get('https://www.python.org')
    print(r.status_code)