import click
import pprint
from library import b2c2_lib

# initialize CLI
@click.group()
def cli():
    """CLI app to interact with B2C2 API"""

# view instruments
@cli.command()
def view_instruments():
    """View tradable instruments"""
    print('\n ------------------------------------- \
            \n VIEW TRADABLE INSTRUMENTS \
            \n ------------------------------------- \n')
    tradable_instruments = b2c2_lib().view_tradable_instruments()
    pprint.pprint(tradable_instruments)
    return tradable_instruments

# request for quote
@cli.command()
@click.option('--instrument', type=str, prompt='\n ENTER INSTRUMENT NAME e.g. BTCUSD \n', help='Tradable instrument name')
@click.option('--side', type=click.Choice(['buy', 'sell'], case_sensitive=False), prompt='\n ENTER THE SIDE OF THE TRADE \n', help='Side of the trade - only buy or sell')
@click.option('--quantity', type=float, prompt='\n ENTER QUANTITY \n', help='Quantity to trade - must be a number')
def request_for_quote(instrument, side, quantity):
    """Request for Quote"""
    
    print('\n ------------------------------------- \
            \n REQUEST FOR QUOTE \
            \n ------------------------------------- \n')

    quote_data = b2c2_lib(instrument, side, quantity).request_for_quote()
    pprint.pprint(quote_data)

    if quote_data != False:
        execute_decision = input('\n ------------------------------------- \
                                \n EXECUTE THIS QUOTE? (Y/n) \
                                \n ------------------------------------- \n')

        if execute_decision == 'Y':
            execute_order_data = b2c2_lib(quote_data).execute_order()

            if execute_order_data != False:
                print('\n ------------------------------------- \
                        \n ORDER FULFILLED \
                        \n ------------------------------------- \n')
                print('ACCOUNT BALANCE: \n')
                pprint.pprint(b2c2_lib().view_account_balance())
                print('\n ORDER DETAILS: \n')
                pprint.pprint(execute_order_data)
            else:
                print('\n ------------------------------------- \
                        \n ERROR: QUOTE EXPIRED - TIME VALID PASSED \
                        \n ------------------------------------- \n')
    else:
        print('\n ------------------------------------- \
                \n ERROR: INSTRUMENT INVALID \
                \n ------------------------------------- \n')

# view account balance
@cli.command()
def view_balance():
    """View account balance"""
    print('\n ------------------------------------- \
            \n VIEW BALANCE \
            \n ------------------------------------- \n')
    account_balance = b2c2_lib().view_account_balance()
    pprint.pprint(account_balance)
    return account_balance

# check connection status
@cli.command()
def connection_status():
    """Check connection status"""
    print('\n ------------------------------------- \
        \n CONNECTION STATUS \
        \n ------------------------------------- \n')
    conn_status = b2c2_lib().check_connection_status()
    print(conn_status)
    return conn_status

# view ledger
@cli.command()
def view_ledger():
    """View ledger"""
    print('\n ------------------------------------- \
        \n VIEW LEDGER \
        \n ------------------------------------- \n')
    ledger = b2c2_lib().view_ledger()
    pprint.pprint(ledger)
    return ledger

# view trade info
@cli.command()
@click.option('--order_id', type=str, prompt='\n ENTER CLIENT_ORDER_ID OR TRADE_ID OR ORDER FOR SPECIFIC TRADE OR PRESS ENTER FOR ALL TRADES \n', default="", help='Trade order id')
def trade_history(order_id):
    """View specific trade information"""
    print('\n ------------------------------------- \
            \n VIEW TRADE \
            \n ------------------------------------- \n')
    trade_info = b2c2_lib(order_id).view_trade_info()
    pprint.pprint(trade_info)
    return trade_info

if __name__ == "__main__":
    cli()