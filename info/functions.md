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

## Creating a Customer
import requests

url = "https://sandbox.intasend.com/api/v1/subscriptions-customers/"

payload = {
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "reference": "string",
    "address": "string",
    "city": "string",
    "state": "string",
    "zipcode": "string",
    "country": "string"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ISSecretKey_test_......"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

## Creating a Subscription
import requests

url = "https://sandbox.intasend.com/api/v1/subscriptions/"

payload = {
    "customer_id": "<customer_id>",
    "reference": "string",
    "plan_id": "<plan_id>",
    "start_date": "2023-10-09"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ISSecretKey_test_......"
}

response = requests.post(url, json=payload, headers=headers)

print(response.get("setup_url"))

@simokamaa: Thank you for your response! However, it
## Subscription Response
{
  "subscription_id": "string",
  "customer_id": "string",
  "reference": "string",
  "plan_id": "string",
  "status": "string",
  "start_date": "2023-10-09",
  "setup_url": "string",
  "created_at": "2023-10-09T06:57:02.018Z",
  "updated_at": "2023-10-09T06:57:02.018Z"
}

## Creating a wallet
{
    'wallet_id': 'AWR19L',
    'currency': 'KES',
    'wallet_type': 'WORKING',
    'label': 'MY-WALLET-ID',
    'can_disburse': 'true',
    'current_balance': '0.00',
    'available_balance': '0.00',
    'updated_at': '2021-05-31T21:51:05.577470+03:00'
}

## wallet transcations
[{
    "invoice": "...",
    "value": "10.00",
    "running_balance": "20.00",
    "narrative": "Intra Txn. wallet 9",
    "created_at": "2020-08-03T15:08:40.263322+03:00",
    "updated_at": "2020-08-03T15:08:40.263349+03:00"
}, {
    "invoice": "...",
    "value": "10.00",
    "running_balance": "10.00",
    "narrative": "Intra Txn. wallet 9",
    "created_at": "2020-08-03T15:08:32.283968+03:00",
    "updated_at": "2020-08-03T15:08:32.283992+03:00"
}]