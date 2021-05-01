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
def request_for_quote(instrument, side, quantity):
    """Request for Quote"""
    print(f'{side} {instrument} {quantity}')

    #rfq_data = (instrument, side, quantity)
        
    data = b2c2_lib(instrument, side, quantity).request_for_quote()
    pprint.pprint(data)
    return data

@cli.group()
def req_for_qoute():
    """Request for Quote"""

@req_for_qoute.command()
@click.option('--instrument', default="dev", type=click.Choice(['dev', 'stg', 'prd'], case_sensitive=False), prompt='Enter env name to deploy', help='Env to deploy')
@click.option('--side', default="buy", type=click.Choice(['aws', 'gcp', 'azure'], case_sensitive=False), prompt='Enter cloud to deploy to', help='Cloud to deploy to')
@click.option('--quantity', type=float, prompt='Enter cloud to deploy to', help='Quantity to trade')
def rfq_data(env, cloud):
    print(f'{side} {instrument} {quantity}')

# execute order
@cli.command()
def execute_order():
    """Execute order"""

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