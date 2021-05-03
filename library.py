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
        response = requests.get('%s/instruments/' % self.api, headers=self.headers)
        response_json = response.json()
        return response_json

    def request_for_quote(self):
        instrument = self.data[0].upper()+'.SPOT'
        side = self.data[1].lower()
        quantity = str(self.data[2])

        # check instrument is valid
        instrument_valid = self.check_instrument_valid(instrument)
        
        if instrument_valid == True:
            post_data = {
                'instrument': instrument,
                'side': side,
                'quantity': quantity,
                'client_rfq_id': str(uuid.uuid4())
                }

            response = requests.post('%s/request_for_quote/' % self.api, json=post_data, headers=self.headers)
            response_json = response.json()
            return response_json
        else:
            return False #Instrument ivalid
    
    def execute_order(self):
        instrument = self.data[0]['instrument']
        side = self.data[0]['side']
        quantity = self.data[0]['quantity']
        client_order_id = self.data[0]['client_rfq_id']
        price = self.data[0]['price']
        order_type = 'FOK'
        valid_until = self.data[0]['valid_until']
        
        #check quote validity
        quote_valid = self.check_quote_validity( valid_until )

        if quote_valid:
            post_data = {
            'instrument': instrument,
            'side': side,
            'quantity': quantity,
            'client_order_id': client_order_id,
            'price': price,
            'order_type': order_type,
            'valid_until': valid_until
            }

            response = requests.post('%s/order/' % self.api, json=post_data, headers=self.headers)
            response_json = response.json()
            return response_json
        else:
            return False

    def check_quote_validity(self, quote_valid_until):
        dt_now = datetime.datetime.utcnow()
        quote_valid_time_str = quote_valid_until
        quote_valid_time_dt = parse(quote_valid_time_str)
        quote_valid_time_dt_naive = quote_valid_time_dt.replace(tzinfo=None)
        if dt_now < quote_valid_time_dt_naive:
            return True

    def check_instrument_valid(self, instrument):
        tradable_instruments = self.view_tradable_instruments()
        for i in tradable_instruments:
            if instrument.lower() == i['name'].lower():
                return True
    
    def view_account_balance(self): 
        response = requests.get('%s/balance/' % self.api, headers=self.headers)
        response_json = response.json()
        return response_json
    
    def check_connection_status(self):
        response = requests.get('%s/balance/' % self.api, headers=self.headers)
        if response.status_code == 200:
            status = 'Connection status GOOD. Status code: 200'
        else: 
            status = 'Connection status BAD. Status code: %s' % response.status_code
        return status
    
    def view_ledger(self):
        response = requests.get('%s/ledger/' % self.api, headers=self.headers)
        response_json = response.json()
        return response_json
    
    def view_trade_info(self):
        response = requests.get('%s/trade/' % self.api, headers=self.headers)
        response_json = response.json()
        order_id = self.data[0]
        if len(order_id) == 0:
            return response_json
        else:
            for i,v in enumerate(response.json()):
                if v['order'] == order_id or v['client_order_id'] == order_id or v['trade_id'] == order_id:
                #print(v)
                    return v
                else:
                    return 'ERROR: TRADE NOT FOUND'