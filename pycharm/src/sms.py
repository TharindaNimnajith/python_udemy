from twilio.rest import Client

account_sid = 'ACa3543161e90e821ba8436f20edce392f'
auth_token = '23fab9783a29de0efb9c77751606973c'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+15039662030',
    body='Hello!',
    to='+94712089046'
)

print(message.sid)
