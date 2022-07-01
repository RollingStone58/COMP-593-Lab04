from poke_api import search_poke_api
from pastebin_api import post_new_paste
from sys import argv

def get_paste_title(search_term):
    return f"{search_term.capitalize()}'s Amazing Abilities"


def main():

    # Get search term from user
    search_term = argv[1].replace("'", '')

    #Get pokemon abilities from api
    ability_dict = search_poke_api(search_term)

    #Determine Title of PasteBin
    paste_title = get_paste_title(search_term)

    #Determine Body Text
    paste_body = get_paste_body(ability_dict)
    pass 
    #Create new PasteBin paste
    paste_url = post_new_paste(paste_title, paste_body, '1M')

    print(paste_url)


def get_paste_body(ability_dict):

    ability_list = [a['ability'] for a in ability_dict['abilities']]
    paste_body = '\n\n'.join([str(a) for a in ability_list])
    return paste_body




main()