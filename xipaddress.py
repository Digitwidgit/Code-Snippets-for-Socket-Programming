
from requests import get

#Get your external ip address and print it to the screen.
#This can be useful, since most of the code I have been seeing is -
#getting the internal ip address.
ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
