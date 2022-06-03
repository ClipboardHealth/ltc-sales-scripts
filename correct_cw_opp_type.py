import os
import requests
import pandas as pd


# Very simple script that changes the account types to 'Enrolled Customer' for CW Opp's
  # (question 1): https://docs.google.com/document/d/12azC949Ifpp-zZU9dvffpNgilsz9uFutZRDuQLMlRrc/edit

sf_access_token = os.environ.get('SF_TOKEN')
sf_headers = {"Authorization": "Bearer %s" % sf_access_token}   
sf_query_url = 'https://clipboardhealth.my.salesforce.com/services/data/v53.0/query/'

df = pd.read_csv('data/cw_accounts_incorrect_type.csv')
print("rows:", df.shape[0])

for index, row in df.iterrows():
  account_id = row['Account ID']
  update_account_url = 'https://clipboardhealth.my.salesforce.com/services/data/v53.0/sobjects/Account/' + account_id
  res = requests.patch(update_account_url, headers=sf_headers, json={
    'Type': 'Enrolled_Customer',
  })
  print('update response:', res)






