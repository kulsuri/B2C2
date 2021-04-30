import click
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

# @click.group()
# def main():
#     """Demo WP Control Help"""

# @main.group()
# def wp():
#     """Commands for WP"""

# @wp.command('install')
# def wp_install():
#     """Install WP instance"""

# @wp.command('duplicate')
# def wp_dup():
#     """Duplicate WP instance"""

# @main.group()
# def https():
#     """Commands for HTTPS"""

# @https.command('create')
# def https_create():
#     """Create HTTPS configuration"""

# @https.command('sync')
# def https_sync():
#     """Sync HTTPS configuration with Apache"""

# if __name__ == '__main__':
#     main()