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

### Run code:
- POST /api/runcodev2  
```
['C', 'CPP', 'CPP11', 'CPP14', 'CLOJURE', 'CSHARP', 'GO', 'HASKELL', 
'JAVA', 'JAVA8', 'JAVASCRIPT', 'JAVASCRIPT_NODE', 'OBJECTIVEC', 'PASCAL', 
'PERL', 'PHP', 'PYTHON', 'PYTHON3', 'R', 'RUBY', 'RUST', 'SCALA', 'SWIFT', 'SWIFT_4_1']  
```

Example : http://localhost:5000/api/runcodev2/python3/print(5)
```json
{
  "async": 0,
  "memory_limit": 262144,
  "memory_used": "64",
  "output": "5\n",
  "output_html": "5<br>",
  "request_NOT_OK_reason": "",
  "request_OK": "True",
  "signal": "OTHER",
  "status": "AC",
  "status_detail": "NA",
  "stderr": "",
  "time_limit": 5,
  "time_used": "0.105635"
}
```
- POST /api/runcode  
```
languages = ['C', 'Cpp', 'Cpp14', 'Java', 'Python', 'Python3', 'Scala', 'Php', 'Perl', 'Csharp']
```

```json
{
  "cmpError": "",
  "compResult": "S",
  "hash": "815b333dde20afc694d4757ceed36e4e_Tester_U16",
  "id": "9CNgKChGku",
  "lxcOutput": "",
  "memory": "0.125",
  "output": "5\n",
  "rntError": "",
  "time": "0.02",
  "valid": "1"
}
```

### dev commands
- pipenv shell
- flask run

### License  
MIT