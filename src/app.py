from flask import Flask, request, render_template_string
from sqlalchemy.orm import sessionmaker
from src.db_initialize import EquipmentEvent, get_engine
import random

app = Flask(__name__)

# Database session
engine = get_engine()
SessionLocal = sessionmaker(bind=engine)

# Simple HTML UI (enough for demo)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Predictive Maintenance Dashboard</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        input { margin: 5px; }
        table, th, td { border: 1px solid black; border-collapse: collapse; padding: 6px; }
    </style>
</head>
<body>

<h2>Predict Equipment Failure Risk</h2>

<form method="POST">
    <input name="machine_id" placeholder="Machine ID" required><br>
    <input name="temperature" placeholder="Temperature" type="number" step="0.1" required><br>
    <input name="vibration" placeholder="Vibration" type="number" step="0.1" required><br>
    <input name="pressure" placeholder="Pressure" type="number" step="0.1" required><br>
    <input name="run_hours" placeholder="Run Hours" type="number" required><br>
    <button type="submit">Predict</button>
</form>

{% if prediction %}
<p><strong>Failure Risk:</strong> {{ prediction }}%</p>
<p><strong>Status:</strong> {{ "⚠ MAINTENANCE REQUIRED" if prediction > 50 else "✔ OK" }}</p>
{% endif %}

<hr>
<h3>Logged Maintenance Events</h3>

<table>
<tr>
    <th>ID</th><th>Machine</th><th>Temp</th><th>Vibration</th><th>Pressure</th><th>Hours</th><th>Risk</th><th>Required</th>
</tr>
{% for row in rows %}
<tr>
<td>{{row.id}}</td>
<td>{{row.machine_id}}</td>
<td>{{row.temperature}}</td>
<td>{{row.vibration}}</td>
<td>{{row.pressure}}</td>
<td>{{row.run_hours}}</td>
<td>{{row.failure_risk}}</td>
<td>{{row.maintenance_required}}</td>
</tr>
{% endfor %}
</table>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form():
    prediction = None
    session = SessionLocal()

    if request.method == "POST":
        # Fake ML prediction for now (you can replace with model later)
        failure_risk = random.randint(0, 100)

        event = EquipmentEvent(
            machine_id=request.form["machine_id"],
            temperature=float(request.form["temperature"]),
            vibration=float(request.form["vibration"]),
            pressure=float(request.form["pressure"]),
            run_hours=float(request.form["run_hours"]),
            failure_risk=failure_risk,
            maintenance_required=failure_risk > 50
        )

        session.add(event)
        session.commit()

        prediction = failure_risk

    rows = session.query(EquipmentEvent).all()
    return render_template_string(HTML_TEMPLATE, rows=rows, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
