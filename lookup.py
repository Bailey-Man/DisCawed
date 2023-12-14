import requests

def get_player_info(steamid):
    # Perform the lookup using requests

    # request from this url; https://steamid.uk/steamidapi/
    response = requests.get(f"https://steamid.uk/steamidapi.php?api={APIKEY}&steamids={steamid}")

    response = requests.get(f"https://api.example.com/users/{steamid}")
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        username = data["username"]
        avatar = data["avatar"]
    else:
        # Handle the case when the lookup fails
        username = "Unknown"
        avatar = ""
    
    return username, avatar
