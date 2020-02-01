#!/opt/utils/venv/pulp/3.6.5/bin/python
from pulpcore.client import pulpcore
from pulpcore.client import pulp_rpm
from pulpcore.client.pulp_rpm import (
    RemotesRpmApi,
    RpmRpmRemote
)
import hashlib

configuration = pulpcore.Configuration()
configuration.host = 'http://pulp3'
configuration.username = 'admin'
configuration.password = 'admin'
configuration.safe_chars_for_path_param = '/'
rpm_client = pulp_rpm.ApiClient(configuration)

remote = {}
with open('./redhat-uep.pem') as f:
    cert = f.read()
print( f"INPUT {hashlib.sha256(bytes(cert, 'utf8')).hexdigest()}")

remote['client_cert'] = cert
remote['name'] = "uep"
remote['url'] = "http://example.com"
rpm_client = pulp_rpm.ApiClient(configuration)
data = RpmRpmRemote(**remote)
remote = RemotesRpmApi(rpm_client).create(data)

for remote in RemotesRpmApi(rpm_client).list(name='uep').results:
    print(f"PULP client_cert {remote.client_cert}")
