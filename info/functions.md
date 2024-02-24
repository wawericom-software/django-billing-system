## Subscription Fields
- Field	Description
- currency	Choose a billing currency : KES, USD, EUR, GBP
- name	Provide a name for your subscription plane e.g Basic Standard, Premium e.t.c
- frequency	Provide a billing frequency. This determines the billing interval depending on the frequency unit selected. E.g if you set frequency as 1 and frequency unit as M(month), billing will happen every one month. - If frequency was 3, billing will happen after every three months.
- frequency_unit	Provide a frequency unit: 'D'(day), 'W'(week), 'M'(month), 'Y'(year)
- billing_cycles	This determines set the number of times billing should be done. E.g if you want to bill your customer monthly for the next one year, you can set this field as 12.
amount	Billing amount for the plan

import requests

url = "https://sandbox.intasend.com/api/v1/subscriptions-plans/"

payload = {  
    "currency": "KES",  
    "name": "Basic",  
    "frequency": 1,  
    "frequency_unit": "M",  
    "billing_cycles": 12,  
    "amount": "1000"  
}  
headers = {  
    "accept": "application/json",  
    "content-type": "application/json",  
    "Authorization": "Bearer ISSecretKey_test..."  
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)