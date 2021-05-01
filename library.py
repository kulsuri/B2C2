import requests
import uuid

class b2c2_lib:
    def __init__(self, *rfq_data):
        self.api = 'https://api.uat.b2c2.net'
        self.api_token = 'e13e627c49705f83cbe7b60389ac411b6f86fee7'
        self.headers = {'Authorization': 'Token %s' % self.api_token}
        self.rfq_data = rfq_data

    def view_tradable_instruments(self):
        print('view tradable instruments')
        response = requests.get('%s/instruments/' % self.api, headers=self.headers)
        return response

    def request_for_quote(self):
        print(self.rfq_data)
        post_data = {
            'instrument': self.rfq_data[0],
            'side': self.rfq_data[1],
            'quantity': self.rfq_data[2],
            'client_rfq_id': str(uuid.uuid4())
            }
        print(post_data)

        response = requests.post('%s/request_for_quote/' % self.api, json=post_data, headers=self.headers)
        return response

    
    def execute_order(self):
        print('execute order')

        uuid = str(uuid.uuid4())
        quantity = '1'
        side = 'buy'
        instrument = 'BTCUSD.SPOT'
        price = '1000'
        valid_until = datetime.datetime.utcfromtimestamp(time.time() + 10).strftime("%Y-%m-%dT%H:%M:%S")
        executing_unit = 'risk-adding-strategy'


        post_data = {
            'instrument': instrument,
            'side': side,
            'quantity': quantity,
            'client_order_id': uuid,
            'price': price,
            'order_type': 'FOK',
            'valid_until': valid_until,
            'executing_unit': executing_unit,
        }

        response = requests.post('%s/order/' % self.api, json=post_data, headers=headers)
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