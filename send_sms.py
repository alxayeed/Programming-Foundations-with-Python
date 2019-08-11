# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'ACd63961950920c4cf052f9a5e58ab6032'
auth_token = '5ac1ee70513b8dabb4210779245d3df8'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey Al!Eid Mubarak to you and your beloved ones",
                     from_='+17023303472',
                     to='+8801683338978'
                 )

print(message.sid)
