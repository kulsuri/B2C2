import requests
import uuid
import datetime
from dateutil.parser import parse


class b2c2_lib:
    def __init__(self, *data):
        self.api = 'https://api.uat.b2c2.net'
        self.api_token = 'e13e627c49705f83cbe7b60389ac411b6f86fee7'
        self.headers = {'Authorization': 'Token %s' % self.api_token}
        self.data = data

    def view_tradable_instruments(self):
        print('view tradable instruments')
        response = requests.get('%s/instruments/' % self.api, headers=self.headers)
        response = [{"name": "BTCUSD.CFD"},
                    {"name": "BTCUSD.SPOT"},
                    {"name": "BTCEUR.SPOT"},
                    {"name": "BTCGBP.SPOT"},
                    {"name": "ETHBTC.SPOT"},
                    {"name": "ETHUSD.SPOT"},
                    {"name": "LTCUSD.SPOT"},
                    {"name": "XRPUSD.SPOT"},
                    {"name": "BCHUSD.SPOT"}]
        return response

    def request_for_quote(self):
        print(self.data)

        # implement instrument input validity
        instrument_valid = self.check_instrument_valid( self.data[0] )

        if instrument_valid == True:
            post_data = {
                'instrument': self.data[0],
                'side': self.data[1],
                'quantity': self.data[2],
                'client_rfq_id': str(uuid.uuid4())
                }
            print(post_data)

            response = requests.post('%s/request_for_quote/' % self.api, json=post_data, headers=self.headers)
            return response
        else:
            return False #'Instrument not valid. Please check and try again.'
    
    def execute_order(self):
        print('execute order')

        print(self.data)

        # implement check quote validity
        quote_valid = self.check_quote_validity( self.data[0]['valid_until'] )

        if quote_valid:
            post_data = {
            'instrument': self.data[0]['instrument'],
            'side': self.data[0]['side'],
            'quantity': self.data[0]['quantity'],
            'client_order_id': self.data[0]['client_rfq_id'],
            'price': self.data[0]['price'],
            'order_type': 'FOK',
            'valid_until': self.data[0]['valid_until']
            }

            print(post_data)

            response = requests.post('%s/order/' % self.api, json=post_data, headers=self.headers)
            return response
        
        else:
            return False

        # post_data = {
        #     'instrument': self.data[0]['instrument'],
        #     'side': self.data[0]['side'],
        #     'quantity': self.data[0]['quantity'],
        #     'client_order_id': self.data[0]['client_rfq_id'],
        #     'price': self.data[0]['price'],
        #     'order_type': 'FOK',
        #     'valid_until': self.data[0]['valid_until']
        # }

        # print(post_data)

        # response = requests.post('%s/order/' % self.api, json=post_data, headers=self.headers)
        # return response

    def check_quote_validity(self, quote_valid_until):
        dt_now = datetime.datetime.utcnow()
        quote_valid_time_str = quote_valid_until #self.data[0]['valid_until'] 
        quote_valid_time_dt = parse(quote_valid_time_str)
        quote_valid_time_dt_naive = quote_valid_time_dt.replace(tzinfo=None)

        if dt_now < quote_valid_time_dt_naive:
            return True
        # else:
        #     return False

    def check_instrument_valid(self, instrument):
        tradable_instruments = self.view_tradable_instruments()

        for i in tradable_instruments:
            if instrument.lower() == i['name'].lower():
                return True
    
    def view_account_balance(self):
        print('view account balance')
        response = requests.get('%s/balance/' % self.api, headers=self.headers)
        return response
    
    def check_connection_status(self):
        print('check connection status')
        response = requests.get(self.api, headers=self.headers)
        if response.status_code == 200:
            status = 'Connection status GOOD. Status code: 200'
        else: 
            status = 'Connection status BAD. Status code: %s' % response.status_code
        return status
    
    def view_ledger(self):
        print('List all entries affecting your balance, such as trade legs and settlements.')
        response = requests.get('%s/ledger/' % self.api, headers=self.headers)
        return response
    
    def view_trade_info(self):
        print('trade info')
        response = requests.get('%s/trade/' % self.api, headers=self.headers)
        return response