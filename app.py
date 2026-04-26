from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

events = []
traffic_count = 0
alert_count = 0
block_count = 0


# ================= HTML =================
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>IDS Dashboard Server</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body {
            font-family: Arial;
            background: #f4f6f8;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        .top-box {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }

        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 200px;
        }

        .big {
            font-size: 28px;
            font-weight: bold;
        }

        table {
            width: 100%;
            background: white;
            border-collapse: collapse;
        }

        th {
            background: black;
            color: white;
            padding: 10px;
        }

        td {
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }

        .row-alert { background: #fff4e5; }
        .row-block { background: #ffe5e5; }
        .row-traffic { background: #eaf4ff; }

        .danger {
            color: red;
            font-weight: bold;
        }

        .safe {
            color: green;
            font-weight: bold;
        }
    </style>
</head>

<body>

<h1>🚀 IDS Dashboard Server</h1>

<div class="top-box">
    <div class="card">
        <div>Total Traffic</div>
        <div class="big">{{ traffic_count }}</div>
    </div>

    <div class="card">
        <div>Total Alerts</div>
        <div class="big">{{ alert_count }}</div>
    </div>

    <div class="card">
        <div>Total Blocks</div>
        <div class="big">{{ block_count }}</div>
    </div>

    <div class="card">
        <div>Status</div>
        {% if alert_count > 0 %}
            <div class="danger">⚠ ATTACK DETECTED</div>
        {% else %}
            <div class="safe">✅ SAFE</div>
        {% endif %}
    </div>
</div>

<table>
<tr>
    <th>Time</th>
    <th>Type</th>
    <th>Source</th>
    <th>Destination</th>
    <th>Protocol</th>
    <th>Port</th>
    <th>Status</th>
</tr>

{% for e in events %}
<tr class="
{% if e.type == 'alert' %}row-alert{% endif %}
{% if e.type == 'block' %}row-block{% endif %}
{% if e.type == 'traffic' %}row-traffic{% endif %}
">
<td>{{ e.time }}</td>
<td>{{ e.type.upper() }}</td>
<td>{{ e.source }}</td>
<td>{{ e.destination }}</td>
<td>{{ e.protocol }}</td>
<td>{{ e.port }}</td>
<td>{{ e.status }}</td>
</tr>
{% endfor %}

</table>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML_PAGE,
        events=list(reversed(events[-20:])),
        traffic_count=traffic_count,
        alert_count=alert_count,
        block_count=block_count
    )


# ================= EVENT FUNCTION =================
def add_event(event_type, source, destination, protocol, port, status):
    global traffic_count, alert_count, block_count

    event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    events.append({
        "type": event_type,
        "source": source,
        "destination": destination,
        "protocol": protocol,
        "port": port,
        "status": status,
        "time": event_time
    })

    if event_type == "traffic":
        traffic_count += 1

    elif event_type == "alert":
        alert_count += 1

    elif event_type == "block":
        block_count += 1


# ================= MAIN =================
if __name__ == "__main__":

    # 🔹 DEMO EVENTS (IMPORTANT)
    add_event("traffic", "10.0.0.2", "192.168.1.2", "TCP", "80", "HTTP allowed")

    add_event("alert", "10.0.0.2", "192.168.1.2", "TCP", "21", "FTP suspicious activity")

    add_event("alert", "10.0.0.2", "192.168.1.2", "TCP", "23", "Telnet attack detected")

    add_event("block", "10.0.0.2", "192.168.1.2", "TCP", "23", "Blocked by ACL 101")

    app.run(host="0.0.0.0", port=5000, debug=True)