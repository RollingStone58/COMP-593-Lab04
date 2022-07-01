import requests


URL = 'https://pokeapi.co/api/v2/pokemon/'

def search_poke_api(search_term=''):
    """
    Searches pokeapi for information regarding specific pokemon

    :param search_term: this is the input of which pokemon is to be searched
    :returns: dictionary about specific pokemon
    """
   
   # Defining search url
    search_url = URL + search_term
    
    #cleaning search
    search_term =str(search_term).strip().lower()

    print(f'Searching for pokemon with the name {search_term}')

    resp_msg = requests.get(search_url)
    if resp_msg.status_code == requests.codes.ok:
        print('Success')

        return resp_msg.json()         
        
    else:
        print('Failure')
        print(f'Error Code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')
        return None

