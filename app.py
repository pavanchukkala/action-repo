from flask import Flask, request, jsonify
from threading import Thread
import logging
import json
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def process_payload(payload):
    logging.info("✅ Payload received:")
    logging.info(json.dumps(payload, indent=2))
    # Replace with your logic:
    # Save to DB, send email, start CI, trigger deployment, etc.

@app.route('/', methods=['POST'])
def webhook():
    try:
        payload = request.get_json(force=True)
        if not payload:
            return jsonify({"error": "Empty payload"}), 400

        Thread(target=process_payload, args=(payload,)).start()
        return '', 200  # Respond fast
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": "Webhook error"}), 500

@app.route('/', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
