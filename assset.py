
# sending an sms 
import africastalking
africastalking.initialize(
username="joe2022",
api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
)
sms = africastalking.SMS
def send_sms(phone, message):
    recepients= [phone]
    sender = "AFRICASTALKING"
    try:
        response = sms.send(message, recepients)
        return (response)
    except:
        return ("An error occured")

send_sms("+254757821060", "Thank you for registering Bliss hospital")