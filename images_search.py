import requests
from random import sample


def get_images_urls(query, count=3):
	url = "https://bing-image-search1.p.rapidapi.com/images/search"
	querystring = {"q": query}
	headers = {
		"X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com",
		"X-RapidAPI-Key": "0e0345dbc8msh8a0de13a6e012d1p1c4379jsn3e8c02db7303"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	items = response.json()["value"]
	urls = [item["contentUrl"] for item in items]
	if len(urls) <= count:
		return urls
	else:
		return sample(urls, count)
