import requests
import uuid
import datetime
import time


class b2c2_lib:
    def __init__(self, *data):
        self.api = 'https://api.uat.b2c2.net'
        self.api_token = 'e13e627c49705f83cbe7b60389ac411b6f86fee7'
        self.headers = {'Authorization': 'Token %s' % self.api_token}
        self.data = data

    def view_tradable_instruments(self):
        print('view tradable instruments')
        response = requests.get('%s/instruments/' % self.api, headers=self.headers)
        return response

    def request_for_quote(self):
        print(self.data)
        post_data = {
            'instrument': self.data[0],
            'side': self.data[1],
            'quantity': self.data[2],
            'client_rfq_id': str(uuid.uuid4())
            }
        print(post_data)

        response = requests.post('%s/request_for_quote/' % self.api, json=post_data, headers=self.headers)
        return response

    
    def execute_order(self):
        print('execute order')

        print(self.data)

        # uuid = self.data[0]['client_rfq_id'] #str(uuid.uuid4())
        # quantity = self.data[0]['quantity']
        # side = self.data[0]['side']
        # instrument = self.data[0]['instrument']
        # price = self.data[0]['price']
        # valid_until = self.data[0]['valid_until']

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
    
    def exit_app(self):
        print('exiting app')
        exit()