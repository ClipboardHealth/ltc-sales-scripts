import requests


## Very simple script that transfer's all contacts to the correct account owner
  # TODO: once Jamie reaches out, will abstract to entire LTC sales team

# Note: access token placed here since this was a 'quick throwaway script' in private repo
sf_access_token = '00D5w000002CFgX!AQ0AQLv4YtFZQJiPmQQjdWfT5wXIparCOSm7WrSGyAxIaBuko7QyU8NjNm.AIfwzzW1R7Cfv8TXSQzFyNard7ef.z8.ekNgd'
sf_headers = {"Authorization": "Bearer %s" % sf_access_token}   
sf_query_url = 'https://clipboardhealth.my.salesforce.com/services/data/v53.0/query/'

user_id = '0055w00000FK6OIAA1'  # Tucker Love's User-ID as a sample
all_accounts_query = "select Id, Name from Account where OwnerId='%s' " % (user_id,)
sf_params = {'q': all_accounts_query}
r = requests.get(sf_query_url, headers=sf_headers, params=sf_params)
data = r.json()
account_rows = data['records']

for account_dict in account_rows:
  account_id = account_dict['Id']
  contact_query = "select Id, OwnerId from Contact where AccountId='%s' " % (account_id,)
  sf_params = {'q': contact_query}
  r = requests.get(sf_query_url, headers=sf_headers, params=sf_params)
  contact_data = r.json()
  account_contacts = contact_data['records']
  
  for contact_dict in account_contacts:
    contact_owner_id = contact_dict['OwnerId']
    contact_id = contact_dict['Id']
    if contact_owner_id != user_id:
      print('found contact:', contact_id)
      update_contact_url = 'https://clipboardhealth.my.salesforce.com/services/data/v53.0/sobjects/Contact/' + contact_id
      res = requests.patch(update_contact_url, headers=sf_headers, json={
        'OwnerId': user_id
      })
      print('update response:', res)




