from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from collections import defaultdict
 
# SharePoint site and credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
site_url = 'https://<sharepoint>'
authority_url = 'https://login.microsoftonline.com/<clientid>'
 
# Get access token
context_auth = AuthenticationContext(authority_url)
context_auth.acquire_token_for_app(client_id, client_secret)
ctx = ClientContext(site_url, context_auth)
 
# Get the SharePoint list
sp_list = ctx.web.lists.get_by_title('Your List Name')
 
# Get all items in the list
items = sp_list.get_items().execute_query()
 
# Find duplicates
duplicates = defaultdict(list)
for item in items:
    # Assuming 'Title' is the field you want to check for duplicates
    duplicates[item.properties['Title']].append(item.properties)
 
# Print out duplicates
for title, duplicate_items in duplicates.items():
    if len(duplicate_items) > 1:
        print(f'Duplicates for title "{title}":')
        for item in duplicate_items:
            print(item)
