# api5paisa

Unoffical Browser Based Python API of 5paisa.

Its created live today morning only. https://youtube.com/watch?v=2PXSfi0Rsho
Feel Free to Tweak it, Modify it and Add the rest of the missing functions to it at your pace.

## Installation

Use the package manager [pip](https://pypi.org/project/api5paisa/) to install api5paisa.

```bash
pip install api5paisa
```

## Usage

```python
from api5paisa import *

#Add Your UserName,Password,TwoFA
username=''
password=''
twofa=''

r=VerifyEmailStatus(s,username)
print(r.text)
print(s.cookies.get_dict())

r,s=Login(s,username,password,twofa)
print(r.text)
print(s.cookies.get_dict())

r,s=getHome(s)
print(r.text.encode("utf-8"))
print(s.cookies.get_dict())

r=GetMarginData(s)
print(r)
print(s.cookies.get_dict())
```

## Documentation
For Documentation and Sample Code, Refer - https://forum.unofficed.com/t/nsepython-documentation/376

## Contributing
For Discussion and Improving this Code, Join - https://www.unofficed.com/chat/
Alternatively, You can write your issue at - https://forum.unofficed.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
