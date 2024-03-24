from ldap3 import Server, Connection, ALL

def search_ad(server_name, user_name, password, search_object):
    # Define the server
    server = Server(server_name, get_info=ALL)

    # Define the connection
    conn = Connection(server, user=user_name, password=password, auto_bind=True)

    # Search for the object
    conn.search('dc=example,dc=com', f'(objectclass={search_object})')

    # Print the results
    for entry in conn.entries:
        print(entry)

if __name__ == "__main__":
    server_name = input("Enter the server name: ")
    user_name = input("Enter the user name: ")
    password = input("Enter the password: ")
    search_object = input("Enter the object to search for: ")
    search_ad(server_name, user_name, password, search_object)