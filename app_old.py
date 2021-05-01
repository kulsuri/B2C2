
# - command line interface
# - request prices from api for given instrument 
#     - e.g. BTCUSD
#     - side (buy/sell)
#     - quantity
# - request instruments available to trade
# - return 'request for quote' info
# - execute the order
# - display total balance of the account
# - message displaying the trade information contained in the order response

# error handling:
#     - sending an outdated quote
#     - HTTP error from the server
#     - losing internet connection
# logging

# other features:
# ping to check if the connection is ok
# ledgers to get your history
#  /trade/id/ to get specific information about a trade

import click
import uuid
from library import b2c2_lib

api = 'https://api.uat.b2c2.net'
api_token = 'e13e627c49705f83cbe7b60389ac411b6f86fee7'

@click.command()
@click.option('--menu', prompt= ' \
################################################### \n \
(1) View tradable instruments \n \
(2) Request for Quote \n \
(3) Execute order \n \
(4) View account balance \n \
(5) Check connection status \n \
(6) View trade history \n \
(7) View specific trade information \n \
(8) Exit \n \
################################################### \n \
What would you like to do? Enter number e.g. 5 \n \
---------------------------------------------------', \
help='Available options.', type=int)

def handle_menu(menu):
    if menu not in list(range(1,9)):
        raise Exception(f'No handler found for menu option: {menu}')
    handler = b2c2_lib(api, api_token).handlers[menu]
    print(handler())
    #return handle_menu()

if __name__ == '__main__':
    handle_menu()