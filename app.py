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
    data = b2c2_lib().view_tradable_instruments()
    click.echo(data)
    return data

# request for quote
@cli.command()
@click.option('--instrument', type=str, prompt='Enter the name of the instrument', help='Tradable instrument name')
@click.option('--side', type=click.Choice(['buy', 'sell'], case_sensitive=False), prompt='Enter the side of the trade', help='Side of the trade')
@click.option('--quantity', type=float, prompt='Enter the quantity', help='Quantity to trade')
#@click.pass_context
def request_for_quote(instrument, side, quantity):
    """Request for Quote"""
    print(f'{side} {instrument} {quantity}')

    #rfq_data = (instrument, side, quantity)
        
    quote_data = b2c2_lib(instrument, side, quantity).request_for_quote()
    pprint.pprint(quote_data)

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
        return print(execute_order_data)
    else:
        return print(quote_data)


# @cli.group()
# def req_for_qoute():
#     """Request for Quote"""

# @req_for_qoute.command()
# @click.option('--instrument', default="dev", type=click.Choice(['dev', 'stg', 'prd'], case_sensitive=False), prompt='Enter env name to deploy', help='Env to deploy')
# @click.option('--side', default="buy", type=click.Choice(['aws', 'gcp', 'azure'], case_sensitive=False), prompt='Enter cloud to deploy to', help='Cloud to deploy to')
# @click.option('--quantity', type=float, prompt='Enter cloud to deploy to', help='Quantity to trade')
# def rfq_data(env, cloud):
#     print(f'{side} {instrument} {quantity}')

# execute order
# @cli.command()
# @click.option('--execute', type=str, prompt='Would you like to execute this order?', help='Execute order')
# def execute_order(execute, instrument, side, quantity):
#     """Execute order"""
#     print(execute)

# view account balance
@cli.command()
def view_balance():
    """View account balance"""
    data = b2c2_lib().view_account_balance()
    click.echo(data)
    return data

# check connection status
@cli.command()
def connection_status():
    """Check connection status"""
    data = b2c2_lib().check_connection_status()
    click.echo(data)
    return data

# view ledger
@cli.command()
def view_ledger():
    """View ledger"""
    data = b2c2_lib().view_ledger()
    click.echo(data)
    return data

# view trade info
@cli.command()
def trade_history():
    """View specific trade information"""
    data = b2c2_lib().view_trade_info()
    click.echo(data)
    return data

@cli.command()
def exit():
    """Exit app"""
    b2c2_lib().exit_app()

# @cli.group()
# def drop():
#     """create objects"""

# @drop.command()
# def table():
#     click.echo('drop table command')

# @drop.command()
# @click.option('--username')
# def user(username):
#     click.echo('drop user command: {}'.format(username))

if __name__ == "__main__":
    cli()