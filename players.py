import re
import string
import requests
from bs4 import BeautifulSoup

def get_all_players():
    """
    Function to get all players that have ever played to euroleague.
    Returns a dictionary containing the player name and the player code.
    """
    players = {}

    for char in list(string.ascii_uppercase):
        req = requests.get(
            'http://www.euroleague.net/competition/players?listtype=alltime&letter=' + char
        )

        soup = BeautifulSoup(req.text, 'html5lib')

        mydivs = soup.findAll('div', {'class': 'items-list'})

        for div in mydivs:
            itemdivs = soup.findAll('div', {'class': 'item'})


        for div in itemdivs:
            links = div.findAll('a')
            for index, link in enumerate(links):
                if index % 2 == 0:
                    player = link.text.replace(',', '').strip()
                    link['href'] = link['href'].replace('?', '')
                    result = re.findall(
                        '/competition/players/showplayerpcode=(.*)&seasoncode=', link['href']
                    )
                    code = result[0]
                    players[code] = player
                    
    return players

if __name__ == '__main__':
    get_all_players()
