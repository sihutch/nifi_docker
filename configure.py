import logging
import nipyapi
import ssl
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.getLogger('nipyapi.utils').setLevel(logging.INFO)
logging.getLogger('nipyapi.security').setLevel(logging.INFO)
logging.getLogger('nipyapi.versioning').setLevel(logging.INFO)

registryEndpoint = 'http://registry:18080'
nipyapi.config.nifi_config.host = 'https://nifi:8443/nifi-api'
nipyapi.config.registry_config.host = 'http://registry:18080/nifi-registry-api'

nipyapi.nifi.configuration.verify_ssl = False

log.info("Waiting for NiFi to be ready for login")
admin_user = nipyapi.utils.wait_to_complete(
    test_function=nipyapi.security.service_login,
    service='nifi',
    username='admin',
    password='admin',
    bool_response=True,
    nipyapi_delay=nipyapi.config.long_retry_delay,
    nipyapi_max_wait=nipyapi.config.long_max_wait
)

log.info("Waiting for NiFi Registry to be ready")
nipyapi.utils.wait_to_complete(
    test_function=nipyapi.security.get_service_access_status,
    service='registry',
    bool_response=True,
    nipyapi_delay=nipyapi.config.long_retry_delay,
    nipyapi_max_wait=nipyapi.config.long_max_wait
)

nipyapi.security.service_login(service='nifi', username='admin', password='admin', bool_response=False)

nipyapi.versioning.create_registry_client(
            name='Test Registry',
            uri=registryEndpoint,
            description='Tet Registry creted during docker setup'
)

nipyapi.versioning.create_registry_bucket('Test Bucket')

"""
Grant all users access to the root process group
"""

user1 = nipyapi.security.get_service_user('user1')
user2 = nipyapi.security.get_service_user('user2')
admin = nipyapi.security.get_service_user('admin')

users = [admin,user1,user2]

rpg_id = nipyapi.canvas.get_root_pg_id()

access_policies = [
        ('write', 'process-groups', rpg_id),
        ('read', 'process-groups', rpg_id)
    ]
for pol in access_policies:
    ap = nipyapi.security.create_access_policy(
    action=pol[0],
    resource=pol[1],
    r_id=pol[2],
    service='nifi'
    )

    for u in users:
        nipyapi.security.add_user_to_access_policy(
        u,
        policy=ap,
        service='nifi',
        refresh=True
        )
