import requests

USERNAME = "hfzh06"
TOKEN = ""

api_url = f"https://api.github.com/users/{USERNAME}"

headers = {
	"Authorization": f"token{TOKEN}",
	"Accept": "application/vnd.github.v3+json"
}


response = requests.get(api_url, headers=headers)

if response.status_code == 200:
	user_data = response.json()
	print(f"{user_data.get('name')}")
	print(f"{user_data.get('public_repos')}")
	print(f"{user_data.get('html_url')}")

else:
	print(response.txt)
# this is hfzh06 do

print("Hello World")
# this is hfzh062do

