import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"The number of entities that were successfully fetched: {len(data)}")
  except requests.HTTPError as e:
    print(e)
    return None
    
  return data

option = input("Enter an option (e.g., 'people' or 'planets'): ").strip().lower()
data = fetch_data(option)
if data:
  for keys in data:
    print(keys["name"])

else:
  print("Unable to download data")