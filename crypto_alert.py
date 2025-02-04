import requests
from twilio.rest import Client
import time

# URL for CoinGecko API to get the price of XRP(ripple) to cad
url = 'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=cad'

#twilio credentials 
account_sid = '#enter account sid from twilio'
auth_token = '^^ but auth token'
client = Client(account_sid, auth_token)

# function to get the xrp(ripple) price
def get_xrp_price():
    try:
        response = requests.get(url)
        data = response.json()
        # Ensure the response is in the expected format
        if 'ripple' in data and 'cad' in data['ripple']:
            xrp_price = data['ripple']['cad']
            print(f"Fetched XRP price: {xrp_price} CAD")
            return xrp_price
        else:
            print("Error: Unexpected data format from API.")
            return None
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None


# function for sending an sms
def send_sms(message):
    try:
        message = client.messages.create(
            body=message,
            from_='+xxxxxxxxxx',  # Your Twilio number
            to='+1xxxxxxxx'  # Your personal phone number
        )
        print(f"SMS sent: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

def main():
    #price threshold for xrp in cad (should send text if higher)
    upper_threshold = 3.50

    while True:
        xrp_price = get_xrp_price()
        if xrp_price:
            print(f"Current XRP Price: {xrp_price} CAD")
            
            # Send SMS if price is above the upper threshold
            if xrp_price > upper_threshold:
                send_sms(f"ALERT: XRP price is now {xrp_price} CAD! It's above the threshold of {upper_threshold} CAD.")
        
        # Wait for 3 minutes before checking again (adjust this time as needed)
        time.sleep(60)

if __name__ == "__main__":
    main()



   

