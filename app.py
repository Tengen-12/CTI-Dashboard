from flask import Flask, render_template, jsonify, request
import random
import datetime

app = Flask(__name__)

def fetch_real_threat_data(start_date=None, end_date=None):
    """
    TODO: Replace this dummy function with actual integration to real cybersecurity threat feeds,
    such as SIEM logs, threat intelligence APIs, etc.
    For now, we simulate data filtering by ignoring the dates.
    """
    severities = ["Low", "Medium", "High", "Critical"]
    threat_data = []
    for i in range(5):
        threat_data.append({
            "id": i,
            "name": f"Threat {i}",
            "severity": random.choice(severities),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return threat_data

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/threats")
def get_threats():
    # Retrieve filter parameters if provided (as a next step for enhanced GUI)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Use the function that you would replace with real data integration.
    threat_data = fetch_real_threat_data(start_date, end_date)
    return jsonify(threat_data)

if __name__ == "__main__":
    app.run(debug=True)
