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
    tradable_instruments = b2c2_lib().view_tradable_instruments()
    #click.echo(tradable_instruments)
    print(tradable_instruments)
    return tradable_instruments

# request for quote
@cli.command()
@click.option('--instrument', type=str, prompt='Enter the name of the instrument', help='Tradable instrument name')
@click.option('--side', type=click.Choice(['buy', 'sell'], case_sensitive=False), prompt='Enter the side of the trade', help='Side of the trade')
@click.option('--quantity', type=float, prompt='Enter the quantity', help='Quantity to trade')
def request_for_quote(instrument, side, quantity):
    """Request for Quote"""
    print(f'{side} {instrument} {quantity}')

    quote_data = b2c2_lib(instrument, side, quantity).request_for_quote()
    pprint.pprint(quote_data)

    if quote_data != False:
        quote_data = {
            "valid_until": "2017-01-01T19:45:22.025464Z",
            "rfq_id": "d4e41399-e7a1-4576-9b46-349420040e1a",
            "client_rfq_id": "149dc3e7-4e30-4e1a-bb9c-9c30bd8f5ec7",
            "quantity": "1.0000000000",
            "side": "buy",
            "instrument": "BTCUSD.SPOT",
            "price": "700.00000000",
            "created": "2018-02-06T16:07:50.122206Z"
            }

        execute_decision = input("Would you like to execute this quote? (Y/n)")

        if execute_decision == 'Y':
            execute_order_data = b2c2_lib(quote_data).execute_order()

            if execute_order_data != False:
                return print(execute_order_data)
            else:
                return print('Quote expired. The time valid has passed.')     
    else:
        #print('here')
        return print('Instrument not valid. Please check and try again.')

# view account balance
@cli.command()
def view_balance():
    """View account balance"""
    account_balance = b2c2_lib().view_account_balance()
    print(account_balance)
    #click.echo(account_balance)
    return account_balance

# check connection status
@cli.command()
def connection_status():
    """Check connection status"""
    conn_status = b2c2_lib().check_connection_status()
    print(conn_status)
    #click.echo(conn_status)
    return conn_status

# view ledger
@cli.command()
def view_ledger():
    """View ledger"""
    ledger = b2c2_lib().view_ledger()
    print(ledger)
    #click.echo(ledger)
    return data

# view trade info
@cli.command()
def trade_history():
    """View specific trade information"""
    trade_info = b2c2_lib().view_trade_info()
    print(trade_info)
    #click.echo(trade_info)
    return data

if __name__ == "__main__":
    cli()