CREDENTIALS = {
    'username': 'Replace with your WA username',
    'password': 'Replace with your WA password (b64)'
}

DEFAULT_RECIPIENTS = ('single-user@s.whatsapp.net', 'group-chat@g.us',)

HOST_NOTIFICATION = '%(emoji)s %(type)s HOST ALERT %(emoji)s\n\n' + \
                    'Host %(host)s, %(address)s is %(state)s.\n\n' + \
                    '%(info)s\n\n' + \
                    '%(time)s'

SERVICE_NOTIFICATION = '%(emoji)s %(type)s SERVICE ALERT %(emoji)s\n\n' + \
                       'Service %(service)s @ %(host)s, %(address)s is %(state)s.\n\n' + \
                       '%(info)s\n\n' + \
                       '%(time)s'