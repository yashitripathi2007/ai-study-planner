from flask import Flask, render_template, request

app = Flask(__name__)

def generate_plan(subjects, hours, days):
    subject_list = [s.strip() for s in subjects.split(",")]
    total_days = int(days)
    hours_per_day = int(hours)

    plan = []
    subject_index = 0

    for day in range(1, total_days + 1):
        plan.append(f"Day {day}:")
        remaining_hours = hours_per_day

        while remaining_hours > 0:
            subject = subject_list[subject_index % len(subject_list)]
            study_time = min(2, remaining_hours)  # max 2 hrs per subject
            plan.append(f"  • {subject}: {study_time} hrs")
            remaining_hours -= study_time
            subject_index += 1

    return plan

@app.route("/", methods=["GET", "POST"])
def index():
    plan = []
    if request.method == "POST":
        subjects = request.form["subjects"]
        hours = request.form["hours"]
        days = request.form["days"]
        plan = generate_plan(subjects, hours, days)

    return render_template("index.html", plan=plan)

if __name__ == "__main__":
    app.run(debug=True)
