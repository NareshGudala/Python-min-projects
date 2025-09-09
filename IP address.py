from requests import get

ip = get('http://api.ipify.org').text

print("================ IP address ==================")

print(f'my public IP address is:{ip}')

print("============*=================*===============*")