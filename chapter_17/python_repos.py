# Processing an api response

import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# store the API repsonses in a variable
response_dict =r.json()
print(f"Total repositories: {response_dict['total_count']}")

# explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories return: {len(repo_dicts)}")

# examine the first repo
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
