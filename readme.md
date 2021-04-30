# b2c2 trading bot

Command line interface to interact and trade with the B2C2 api

# Screenshot
![screengrab](https://media.giphy.com/media/yRx7YJn3sn3lSexn19/giphy.gif)

# What Does This App Do?
1. command line interface
2. request prices from api for given instrument 
- e.g. BTCUSD
- side (buy/sell)
- quantity
3. request instruments available to trade
4. return 'request for quote' info
5. execute orders
6. display total balance of the account
7. ping to check if the connection is ok
8. ledgers to get trade history
9. get specific information about a trade
10. error handling:
- sending an outdated quote
- HTTP error from the server
- losing internet connection
11. logging

# Pre-requisites
- Python 3
- Pip
- Git

# Installation Instructions

1. Open command prompt (windows) or terminal (mac/linux)
2. Navigate to a path for which to host project files e.g
```
cd C:\project
```
1. Clone repo
```
git clone https://github.com/kulsuri/jupiter-coding-test
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
1. Navigate to the project folder and run the command:
```
python app.py
```

# Technologies
- requests
- click

# How Does It Work?

File | Technology | What Does It Do
--- | --- | ---
`app.py` | click | runs the app, handles routes / requests and calls objects from the other files
`library.py` | requests | library of functions for interacting with the B2C2 API


# Bugs and Issues
:x: TBC

:x: TBC

# Feature Requests and Improvements
:black_square_button: Interactive and dynamic front-end built with React

:black_square_button: Improved error handling

:black_square_button: Improved logging