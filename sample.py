from api5paisa import *

#Add Your UserName,Password,TwoFA
username=''
password=''
twofa=''

r=VerifyEmailStatus(s)
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
