import requests

# response = requests.get("https://github.com/PRANJALxDEVxAI/python-learning.git")
# print(response.text)
data = {"title" : 'foo' , "body" : 'bar' , "userId" : 1 ,}
headers = {'Content-type' : 'application/json; charset=UTF-8'}
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url , headers = headers , json = data)
print(response.text)