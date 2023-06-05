from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        current_salary = int(request.form["current-salary"])
        current_daily_salary = float(current_salary / 260)

        current_weeklyhours = float(request.form["weekly-hours"])
        current_yearlyhours = current_weeklyhours * 52
        current_dailyhours = current_weeklyhours / 5
        current_hourly_salary = float(current_daily_salary / current_dailyhours)

        bonus_percentage = float(request.form["bonus-percentage"])
        current_bonus = bonus_percentage / 100 * current_salary

        pension_percentage = float(request.form["pension-percentage"])
        current_pension = pension_percentage / 100 * current_salary

        phi = request.form["phi"]
        if phi == 'n':
            current_phi = 0
        else:
            current_phi = int(request.form["phi"])

        incp = request.form["incp"]
        if incp == 'n':
            current_incprotection = 0
        else:
            current_incprotection = int(request.form["incp"])

        lifecvr = request.form["lifecvr"]
        if lifecvr == 'n':
            current_lifecover = 0
        else:
            current_lifecover = int(request.form["lifecvr"])

        current_holidaydays = float(request.form["holiday-days"])

        current_benefit_value = current_bonus + current_pension + current_phi + current_incprotection + current_lifecover
        current_totalvalue = int(current_salary + current_benefit_value)
        current_holidayvalue = int(current_holidaydays * current_daily_salary)

        return render_template("result.html", current_salary=current_salary, current_daily_salary=current_daily_salary,
                               current_hourly_salary=current_hourly_salary, current_bonus=current_bonus,
                               current_pension=current_pension, current_totalvalue=current_totalvalue,
                               current_holidayvalue=current_holidayvalue, current_holidaydays=current_holidaydays)

    except ValueError:
        return "Please only enter numbers..."

if __name__ == "__main__":
    app.run()