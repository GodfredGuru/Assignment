# this code is used for sending a message by sms to my phone number
import nexmo

client = nexmo.Client(key='5cec9625', secret='UkKE51o68ci5cd0Z')

client.send_message({
    'from': 'Protojay',
    'to': '233548670632',
    'text': 'Hi from Godfred.',
})
