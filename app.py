from flask import Flask, request, jsonify
from threading import Thread
import logging
import time
import json

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Background task example
def handle_webhook_data(data):
    logging.info("Processing payload in background...")
    # Simulate processing time (replace with real logic)
    time.sleep(1)
    # Just logging the data here
    logging.info(json.dumps(data, indent=2))


@app.route('/', methods=['POST'])
def github_webhook():
    if request.method == 'POST':
        try:
            payload = request.get_json()
            if not payload:
                logging.warning("Received empty payload")
                return jsonify({"error": "Empty payload"}), 400

            logging.info("Webhook received successfully")

            # Process payload in background thread
            Thread(target=handle_webhook_data, args=(payload,)).start()

            # Respond immediately to avoid GitHub timeout
            return '', 200

        except Exception as e:
            logging.error(f"Error while handling webhook: {e}")
            return jsonify({"error": "Internal server error"}), 500

    return jsonify({"message": "Invalid method"}), 405


if __name__ == '__main__':
    logging.info("🚀 Starting GitHub Webhook Server on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)
