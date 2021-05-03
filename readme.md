# b2c2 trading bot

Command line interface to interact and trade with the B2C2 api

# Screenshot
![alt text](https://i.ibb.co/JCXG7NS/Screenshot-2021-05-03-101008.jpg)

# Demo
![screengrab](https://media.giphy.com/media/pHXnQsrGs5N7mmSn7Z/giphy.gif)

# What Does This App Do?
1. command line interface
2. request instruments available to trade
3. request prices from api for given instrument 
- e.g. BTCUSD
- side (buy/sell)
- quantity
4. execute orders
5. display total balance of the account
6. ping to check if the connection is ok
7. ledgers to get trade history
8. get specific information about a trade
9. error handling:
- sending an outdated quote
- HTTP error from the server
- losing internet connection
11. ~~logging~~

# Pre-requisites
- Python 3
- Pip
- Git
- B2C2 sandbox API token
- Whitelist client machine IP address

# Installation Instructions

1. Open command prompt (windows) or terminal (mac/linux)
2. Navigate to a path for which to host project files e.g
```
cd C:\project
```
1. Clone repo
```
git clone https://github.com/kulsuri/B2C2
```
4. Navigate to the project folder e.g.
```
cd C:\project\B2C2
```
5. Install required modules
```
pip install -r requirements.txt 
```

# Run the App
Navigate to the project folder and run the command:
```
python app.py
```

# Using the App (Commands)
1. View tradable instruments
```
python app.py view-instruments
```
2. Request a quote
```
python app.py request-for-quote
```
3. Execute a quote (order)
```
tbc
```
4. View trade history
```
python app.py trade-history
```
5. View ledger
```
python app.py view-ledger
```
6. View balance
```
python app.py view-balance
```
7. Check the connection status
```
python app.py connection-status
```

# Technologies (modules)
- requests
- click
- uuid
- datetime

# How Does It Work?

File | Technology | What Does It Do
--- | --- | ---
`app.py` | click | runs the app, handles the CLI and calls objects from the other files
`library.py` | requests | library of functions for interacting with the B2C2 API


# Bugs and Issues
:x: TBC

:x: TBC

# Feature Requests and Improvements
:black_square_button: Interactive and dynamic front-end built with React

:black_square_button: Improved error handling

:black_square_button: Improved logging