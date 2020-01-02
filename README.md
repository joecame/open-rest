# Open rest

### Atom package details/stats
- GET https://open-rest.herokuapp.com/api/atom/package/{name} 
```json
{
  "package_author": "atom",
  "package_desc": "Share your workspace with team members and collaborate on code in real time",
  "package_downloads": "959,499",
  "package_gravatar": "https://github.com/atom.png",
  "package_name": "teletype",
  "package_stars": "600",
  "package_tags": [
    "collaboration",
    "collaborative-editing",
    "pair-programming",
    "real-time"
  ],
  "package_url": "https://atom.io/packages/teletype"
}
```

### Github user main languages used in repos
- GET https://open-rest.herokuapp.com/api/github/{username} 
example : https://open-rest.herokuapp.com/api/github/haikelfazzani
```json
[
  {
    "count": 2,
    "lang": "CSS",
    "percent": 3
  },
  {
    "count": 4,
    "lang": "Java",
    "percent": 7
  },
...etc]
```

### dev commands
- pipenv shell
- flask run

### License  
MIT