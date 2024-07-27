from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    action = data.get('action')
    print(f"Received action: {action}")

    if action == "buy":
        place_order("buy")
    elif action == "sell":
        place_order("sell")

    return jsonify({"status": "success"}), 200

def place_order(order_type):
    # Replace with your demo trading API endpoint and credentials
    api_url = "https://api.demo-trading-platform.com/v1/orders"  # Example API endpoint
    api_key = "your_api_key"  # Replace with your actual API key
    order_data = {
        "symbol": "AAPL",  # Replace with your desired trading symbol
        "qty": 10,         # Replace with your desired quantity
        "side": order_type,
        "type": "market",
        "time_in_force": "gtc"
    }
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(api_url, json=order_data, headers=headers)
    print(response.json())
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

