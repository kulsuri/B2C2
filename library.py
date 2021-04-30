import requests

class b2c2_lib:
    def __init__(self, api, api_token):
        self.api = api
        self.api_token = api_token
        self.headers = {'Authorization': 'Token %s' % api_token}
        self.handlers = {
            1 : self.view_tradable_instruments,
            2 : self.request_for_quote,
            3 : self.execute_order,
            4 : self.view_account_balance,
            5 : self.check_connection_status,
            6 : self.view_trade_history,
            7 : self.view_trade_info,
            8 : self.exit_app
        }

    def view_tradable_instruments(self):
        print('view tradable instruments')
        response = requests.get('%s/instruments/' % self.api, headers=self.headers)
        return response

    def request_for_quote(self):
        print('request for quote')
    
    def execute_order(self):
        print('execute order')
    
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
    
    def view_trade_history(self):
        print('trade history')
        response = requests.get('%s/ledger/' % self.api, headers=self.headers)
        return response
    
    def view_trade_info(self):
        print('trade info')
    
    def exit_app(self):
        print('exiting app')
        exit()




# r = requests.get('https://api.uat.b2c2.net/balance/', headers = headers)

# print(r)