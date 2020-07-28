# api5paisa

Unoffical Browser Based Python API of 5paisa made at [Unofficed](https://unofficed.com/).

Its created live today morning only. https://youtube.com/watch?v=2PXSfi0Rsho

Feel Free to Tweak it, Modify it and Add the rest of the missing functions to it at your pace.

## Installation

Use the package manager [pip](https://pypi.org/project/api5paisa/) to install api5paisa.

```bash
pip install api5paisa
```

## Usage

```python
from api5paisa import Api5Paisa

api = Api5Paisa()
api.login("email or clientId", "passowrd", "dob in the format ddMMyyyy")
#for easy access create ~/.5paisa.conf and user api.login() refer examples/5paisa.conf

#Get Margin
print(api.get_margin())

#Get Trade Book
print(api.get_trade_book())

#Firing Order
order_response = api.order('SBIN', 170.2, 1)
print(order_response)
print(api.get_order_book())

```

## Documentation
For Documentation and Sample Code, Refer - https://forum.unofficed.com/

## Contributing
For Discussion and Improving this Code, Join - https://www.unofficed.com/chat/

## License
[MIT](https://choosealicense.com/licenses/mit/)
