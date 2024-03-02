import requests
import base64
import urllib

# Step 1: Have your application's client ID and secret
client_id = "your_client_id"
client_secret = "your_client_secret"

# Step 2: Have your application request authorization; the user logs in and
# authorizes access
auth_url = "https://accounts.spotify.com/authorize"
params = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "your_redirect_uri",  # replace with your redirect uri
    "scope": "user-read-private",  # replace with your needed scopes
}
url = f"{auth_url}?{urllib.parse.urlencode(params)}"
print(f"Please go to the following URL: \n{url}")

# Step 3: The user is redirected back to your specified redirect URI, with an
# authorization code
authorization_code = input("Enter the authorization code: ")

# Step 4: Your application sends the authorization code to the Spotify Accounts
# service
token_url = "https://accounts.spotify.com/api/token"
payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": "your_redirect_uri",  # replace with your redirect uri
}
headers = {
    "Authorization": "Basic "
    + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
}
response = requests.post(token_url, data=payload, headers=headers)

# Step 5: If the code is valid, Spotify responds with an access token and a
# refresh token
access_token = response.json().get("access_token")
refresh_token = response.json().get("refresh_token")
