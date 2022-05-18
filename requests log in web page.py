#requests needed to interact with web page
import requests
#replace url with target url
url = 'urlOfTarget'
#user log-in data
data = {
#replace user log-in username and password respectively 
'User Id': 'username',
'Password': 'Password',
}
#create element to call request and pass through given info, as text
x=requests.post(url, data=data).text
print(x.status_code)
