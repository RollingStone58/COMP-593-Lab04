
from turtle import title
import requests

def post_new_paste(title, body_text, expiration='1M', listed=True):
    """
    Posts new paste to PasteBin

    :param title: title of paste
    :param body_text: body text of paste
    :param expiration: expiration of paste (N = never, 10M = minutes, 1H. 1D, 1W, 2W, 1M, 6M, 1Y)
    :param listed: whether paste is posted publically or privately
    :returns: url of new paste, if unsuccessful returns nothing    
    """
    print('Posting new paste to PasteBin.....', end='')

    p = {
        'api_dev_key': 'D7e9C1MbOsMXIoHNH7792LQGi47-ePzn',
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_private': 0 if listed else 1, 
        'api_paste_expire_date': expiration
    }

    paste_url = 'https://pastebin.com/api/api_post.php'
    resp_msg = requests.post(paste_url, data=p)
    
    if resp_msg.status_code == requests.codes.ok:
         

        print('Success')
        return resp_msg.text 
        
    else:
        print('Failure')
        
        return None