import requests
import json

def main():
    ## we define a request object that is equal to requests.get('API')
    req = requests.get('http://pokeapi.co/api/v2/pokemon/1/%27)
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    ## we then print out the http status_code that was returned on making this request
    ## you should see a successfull '200' code being returned.
    print("Pokemon Name: " + json_response['name'])

if name == 'main':
    main()
    