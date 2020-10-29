import requests
import json

Base = "http://127.0.0.1:5000/"

numbers_to_add = list(range(10000001))
print(f'sending post request to {Base}total')
#print('sending post requests')
r = requests.post(Base + 'total', data={'numbers_to_add': json.dumps(numbers_to_add)})
if r.status_code != 200:
    raise Exception('get request failed')
print('post request complete')
expected_data = 50000005000000
actual_data = r.json()
actual_data_val = r.json()['total']
assert expected_data == actual_data_val
