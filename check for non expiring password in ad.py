from ldap3 import Server, Connection, ALL
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def check_ad_security(server_name, user_name, password):
    # Define the server
    server = Server(server_name, get_info=ALL)

    # Define the connection
    conn = Connection(server, user=user_name, password=password, auto_bind=True)

    # Search for users with non-expiring passwords
    conn.search('dc=example,dc=com', '(userAccountControl:1.2.840.113556.1.4.803:=65536)')

    # Return the results
    return conn.entries

def generate_report(entries):
    # Define the PDF document
    doc = SimpleDocTemplate("report.pdf")

    # Define the styles
    styles = getSampleStyleSheet()

    # Create the report
    report = []
    for entry in entries:
        report.append(Paragraph(str(entry), styles["BodyText"]))

    # Build the PDF document
    doc.build(report)

if __name__ == "__main__":
    server_name = input("Enter the server name: ")
    user_name = input("Enter the user name: ")
    password = input("Enter the password: ")
    entries = check_ad_security(server_name, user_name, password)
    generate_report(entries)