# A simple Flask-based admin panel.  This placeholder application
# serves a minimal HTML dashboard that links to various API
# endpoints exposed by the microservices.  In a real deployment,
# you might replace this with a full SPA built in React or Vue.

from flask import Flask, render_template_string, request
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

# The API gateway base URL.  When running via docker compose the
# gateway is available on the internal network at http://gateway.
GATEWAY_URL = os.environ.get('GATEWAY_URL', 'http://gateway')

@app.route('/')
def index():
    html = """
    <html>
    <head><title>POS Admin Panel</title></head>
    <body>
        <h1>POS Admin Panel</h1>
        <p>This is a placeholder admin interface.  Use the links
        below to call the underlying microservice APIs via the
        gateway.  In a real application this would be replaced by
        a full featured dashboard.</p>
        <ul>
            <li><a href="{{ url_for('call_api', path='api/auth/user/your-user-id') }}">Get User by ID</a></li>
            <li><a href="{{ url_for('call_api', path='api/profile') }}">My Profile</a></li>
            <li><a href="{{ url_for('call_api', path='api/products') }}">List Products</a></li>
            <li><a href="{{ url_for('call_api', path='api/transactions') }}">List Transactions</a></li>
            <li><a href="{{ url_for('call_api', path='api/orders') }}">List Orders</a></li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/call/<path:path>')
def call_api(path):
    # Forward the request to the API gateway.  In this simple
    # implementation we ignore query parameters and authentication.
    url = f"{GATEWAY_URL}/{path}"
    try:
        resp = requests.get(url)
        return resp.json(), resp.status_code
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
