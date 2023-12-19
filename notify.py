import requests

def get_webex_message_details(token, message_id):
    # Define the Webex Teams API URL for getting message details
    api_url = f"https://webexapis.com/v1/messages/{message_id}"
    
    # Set the headers with the authorization token
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Send a GET request to the Webex Teams API to fetch message details
    response = requests.get(api_url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Print the message details
        message_details = response.json()
        print("Message Details:")
        print("Message ID:", message_details['id'])
        print("Room ID:", message_details['roomId'])
        print("Text:", message_details['text'])
        print("Sender ID:", message_details['personId'])
        print("Created:", message_details['created'])
    else:
        print(f"Failed to fetch message details. Status code: {response.status_code}")
        print(response.text)

# Replace these values with your own
webex_access_token = "your_webex_access_token"
message_id_to_fetch = "message_id_to_fetch"

# Call the function to get the details of a Webex Teams message
get_webex_message_details(webex_access_token, message_id_to_fetch)
