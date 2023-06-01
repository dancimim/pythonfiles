# Program to compare old salary and package with new salary and package when you are considering job offers

# still to work on -  presenting the data nicely
# figure out whether using classes will be beneficial


import math

# breakdown of current salary

# define current salary function - calculates current base, hourly, daily salary with bonus and pensions




def currsal():
    global current_salary
    global current_daily_salary
    global current_hourly_salary
    global current_holidayvalue
    global current_benefit_value
    global current_totalvalue
    global current_bonus
    global current_pension
    global current_holidaydays
    while True:
        try:
            current_salary = int(input("Enter current Salary: "))
            current_salary = int(current_salary)
            current_daily_salary = float((current_salary / 260))
            # define working hours
            while True:
                try:
                    current_weeklyhours = input("Enter Weekly Hours: ")
                    current_weeklyhours = float(current_weeklyhours)
                    break
                except ValueError:
                    print("Please enter a number...")
            current_yearlyhours = current_weeklyhours * 52
            current_dailyhours = current_weeklyhours / 5
            current_hourly_salary = float(current_daily_salary / current_dailyhours)
            while True:
                try:
                    bonus_percentage = input("Enter Bonus Percentage: ")
                    bonus_percentage = float(bonus_percentage)
                    break
                except ValueError:
                    print("Please enter a number...")
            current_bonus = bonus_percentage / 100 * current_salary
            while True:
                try:
                    pension_percentage = input("Enter Pension Percentage: ")
                    pension_percentage = float(pension_percentage)
                    break
                except ValueError:
                    print("Please enter a number...")
            current_pension = pension_percentage / 100 * current_salary
            phi = input("Do you receive Private Healthcare? (y/n)", )
            if phi == 'n':
                current_phi = 0
            else:
                while True:
                    try:
                        current_phi = input("Enter Current Annual Private Healthcare Premium: ")
                        current_phi = int(current_phi)
                        break
                    except ValueError:
                        print("Please enter a number...")
            incp = input("Do you receive Income Protection? (y/n)", )
            if incp == 'n':
                current_incprotection = 0
            else:
                while True:
                    try:
                        current_incprotection = input("Enter Current Annual Income Protection Premium: ")
                        current_incprotection = int(current_incprotection)
                        break
                    except ValueError:
                        print("Please enter a number...")
            lifecvr = input("Do you receive Life Cover? (y/n)", )
            if lifecvr == 'n':
                current_lifecover = 0
            else:
                while True:
                    try:
                        current_lifecover = input("Enter Current Annual Life Cover Premium: ")
                        current_lifecover = int(current_lifecover)
                        break
                    except ValueError:
                        print("Please enter a number...")
            while True:
                try:
                    current_holidaydays = input("Enter Holiday Days: ")
                    current_holidaydays = float(current_holidaydays)
                    break
                except ValueError:
                    print("Please enter a number...")
            current_benefit_value = current_bonus + current_pension + current_phi + current_incprotection + current_lifecover
            current_totalvalue = int(current_salary + current_benefit_value)
            current_holidayvalue = int(current_holidaydays * current_daily_salary)
            print("Current Base Salary", '£', current_salary)
            print("Current Daily Salary:", '£', format(current_daily_salary, ".2f"))
            print("Current Hourly Salary:", '£', format(current_hourly_salary, ".2f"))
            print("Current Annual Bonus:", '£', format(current_bonus, ".2f"))
            print("Current Annual Employer Pension Contributions:", '£', format(current_pension, ".2f"))
            print("Current Total Compensation Value:", '£', current_totalvalue)
            print("Current Value of holiday days:", '£', current_holidayvalue, 'for', current_holidaydays, 'days')
            break
        except ValueError:
            print("Please only enter numbers...")

# function to calculate real cost of commuting
def currentsaldeductions():
    global current_weekly_price_of_commute
    global current_yearly_price_of_commute
    global current_weekly_value_of_commuting_hours
    global current_yearly_value_of_commuting_hours
    global current_total_weekly_cost_of_commute
    global current_total_yearly_cost_of_commute
    global current_days_in_office
    remote = input("Is your current job remote only? (y/n)", )
    if remote == 'y':
        current_days_in_office = 0
        current_daily_commute_time = 0
    else:
        while True:
            try:
                current_days_in_office = input("Enter current amount of days each week in the office: ")
                current_days_in_office = float(current_days_in_office)
                break
            except ValueError:
                    print("Please enter a number...")
        while True:
            try:
                current_daily_commute_time = input("Enter total current commute time per day: ")
                current_daily_commute_time = float(current_daily_commute_time)
                break
            except ValueError:
                print("Please enter a number...")
        new_weekly_hours_commuting = current_days_in_office * current_daily_commute_time
        while True:
            try:
                current_commute_price_perday = input("Enter total price of commute per day: ")
                current_commute_price_perday = float(current_commute_price_perday)
                break
            except ValueError:
                print("Please enter a number...")
        current_weekly_price_of_commute = current_commute_price_perday * current_days_in_office
        print("Total weekly current price of commute is:", '£', format(current_weekly_price_of_commute, ".2f"))
        current_yearly_price_of_commute = current_weekly_price_of_commute * 47
        print("Total yearly current price of commute is:", '£', format(current_yearly_price_of_commute, ".2f"))
        current_weekly_hours_lost_whilst_commuting = current_daily_commute_time * current_days_in_office
        current_weekly_value_of_commuting_hours = current_weekly_hours_lost_whilst_commuting * current_hourly_salary
        current_yearly_value_of_commuting_hours = current_weekly_value_of_commuting_hours * 47
        print("You could have earned", '£', format(current_weekly_value_of_commuting_hours, ".2f"),
              "extra per week instead of commuting")
        print("You could have earned", '£', format(current_yearly_value_of_commuting_hours, ".2f"),
              "extra per year instead of commuting")
        current_total_weekly_cost_of_commute = current_weekly_price_of_commute + current_weekly_value_of_commuting_hours
        current_total_yearly_cost_of_commute = current_yearly_price_of_commute + current_yearly_value_of_commuting_hours
        print("Your total weekly current cost of commuting is:", '£', format(current_total_weekly_cost_of_commute, ".2f"))
        print("Your total yearly current cost of commuting is:", '£', format(current_total_yearly_cost_of_commute, ".2f"))





currsal()

currentsaldeductions()

# define new salary function - calculates current base, hourly, daily salary with bonus and pensions - part time and benefits too


def newsal():
    global new_salary
    global new_daily_salary
    global new_hourly_salary
    global new_holidayvalue
    global new_benefit_value
    global new_totalvalue
    global new_bonus
    global new_pension
    global new_holidaydays
    while True:
        try:
            new_salary = input("Enter new Salary: ")
            new_salary = int(new_salary)
            part_time = input("Is job part time? (y/n)", )
            if part_time == 'n':
                days_perweek = 5
            while True:
                    try:
                        if part_time == 'y':
                            days_perweek = input("Enter days worked per week: ")
                            days_perweek = int(days_perweek)
                        break
                    except ValueError:
                        print("Please enter a number...")
            new_daily_salary = float((new_salary / 260 * (5 / days_perweek)))
            while True:
                try:
                    new_weeklyhours = input("Enter Weekly Hours: ")
                    new_weeklyhours = float(new_weeklyhours)
                    break
                except ValueError:
                    print("Please enter a number...")
            new_yearlyhours = new_weeklyhours * 52
            new_dailyhours = new_weeklyhours / days_perweek
            new_hourly_salary = float(new_daily_salary / new_dailyhours)
            while True:
                try:
                    bonus_percentage = input("Enter bonus Percentage: ")
                    bonus_percentage = float(bonus_percentage)
                    break
                except ValueError:
                    print("Please enter a number...")
            new_bonus = float(bonus_percentage) / 100 * new_salary
            while True:
                try:
                    pension_percentage = input("Enter Pension Percentage: ")
                    pension_percentage = float(pension_percentage)
                    break
                except ValueError:
                    print("Please enter a number...")
            new_pension = float(pension_percentage) / 100 * new_salary
            phi = input("Will you receive Private Healthcare? (y/n)", )
            if phi == 'n':
                new_phi = 0
            else:
                while True:
                    try:
                        new_phi = input("Enter Annual Private Healthcare Premium: ")
                        new_phi = int(new_phi)
                        break
                    except ValueError:
                        print("Please enter a number...")
            incp = input("Will you receive Income Protection? (y/n)", )
            if incp == 'n':
                new_incprotection = 0
            else:
                while True:
                    try:
                        new_incprotection = input("Enter Annual Income Protection Premium: ")
                        new_incprotection = int(new_incprotection)
                        break
                    except ValueError:
                        print("Please enter a number...")
            lifecvr = input("Will you receive Life Cover? (y/n)", )
            if lifecvr == 'n':
                new_lifecover = 0
            else:
                while True:
                    try:
                        new_lifecover = input("Enter Annual Life Cover Premium: ")
                        new_lifecover = int(new_lifecover)
                        break
                    except ValueError:
                        print("Please enter a number...")
            while True:
                try:
                    new_holidaydays = input("Enter Holiday Days: ")
                    new_holidaydays = float(new_holidaydays)
                    break
                except ValueError:
                    print("Please enter a number...")
            if days_perweek < 5:
                new_holidaydays = new_holidaydays * days_perweek / 5
                print("You are entitled to", new_holidaydays, "days holiday")
            if days_perweek > 5:
                print("You should work less!!!!")
            new_benefit_value = new_phi + new_incprotection + new_lifecover + new_pension + new_bonus
            new_totalvalue = int(new_salary + new_benefit_value)
            new_holidayvalue = int(new_holidaydays * new_daily_salary)
            print("New Base Salary", '£', new_salary)
            print("New Daily Salary:", '£', format(new_daily_salary, ".2f"))
            print("New Hourly Salary:", '£', format(new_hourly_salary, ".2f"))
            print("New Annual Bonus:", '£', format(new_bonus, ".2f"))
            print("New Annual Employer Pension Contributions:", '£', format(new_pension, ".2f"))
            print("New Total Compensation Value:", '£', new_totalvalue)
            print("New Value of holiday days:", '£', new_holidayvalue, 'for', new_holidaydays, 'days')
            break
        except ValueError:
            print("Please enter a number...")

# function to calculate real cost of commuting
def newsaldeductions():
    global new_weekly_price_of_commute
    global new_yearly_price_of_commute
    global new_weekly_value_of_commuting_hours
    global new_yearly_value_of_commuting_hours
    global new_total_weekly_cost_of_commute
    global new_total_yearly_cost_of_commute
    global new_days_in_office
    remote = input("Is your new job remote only? (y/n)", )
    if remote == 'y':
        new_days_in_office = 0
        new_daily_commute_time = 0
    else:
        while True:
            try:
                new_days_in_office = input("Enter new amount of days each week in the office: ")
                new_days_in_office = int(new_days_in_office)
                break
            except ValueError:
                print("Please enter a number...")
        while True:
            try:
                new_daily_commute_time = input("Enter total new commute time per day: ")
                new_daily_commute_time = float(new_daily_commute_time)
                break
            except ValueError:
                print("Please enter a number...")
        new_weekly_hours_commuting = new_days_in_office * new_daily_commute_time
        while True:
            try:
                new_commute_price_perday = input("Enter total price of commute per day: ")
                new_commute_price_perday = float(new_commute_price_perday)
                break
            except ValueError:
                print("Please enter a number...")
        new_weekly_price_of_commute = new_commute_price_perday * new_days_in_office
        print("Total new weekly price of commute is:", '£', format(new_weekly_price_of_commute, ".2f"))
        new_yearly_price_of_commute = new_weekly_price_of_commute * 47
        print("Total new yearly price of commute is:", '£', format(new_yearly_price_of_commute, ".2f"))
        new_weekly_hours_lost_whilst_commuting = new_daily_commute_time * new_days_in_office
        new_weekly_value_of_commuting_hours = new_weekly_hours_lost_whilst_commuting * new_hourly_salary
        new_yearly_value_of_commuting_hours = new_weekly_value_of_commuting_hours * 47
        print("You could have earned", '£', format(new_weekly_value_of_commuting_hours, ".2f"),
              "extra per week instead of commuting")
        print("You could have earned", '£', format(new_yearly_value_of_commuting_hours, ".2f"),
              "extra per year instead of commuting")
        new_total_weekly_cost_of_commute = new_weekly_price_of_commute + new_weekly_value_of_commuting_hours
        new_total_yearly_cost_of_commute = new_yearly_price_of_commute + new_yearly_value_of_commuting_hours
        print("Your new total weekly cost of commuting is:", '£', format(new_total_weekly_cost_of_commute, ".2f"))
        print("Your new total yearly cost of commuting is:", '£', format(new_total_yearly_cost_of_commute, ".2f"))



newsal()

newsaldeductions()


def salcomp():
    if __name__ == "__main__":
    # Comparison calculations between current and new salary
        global daily_salary_diff
        global hourly_salary_diff
        global hourly_percent_increase
        daily_salary_diff = new_daily_salary - current_daily_salary
        hourly_salary_diff = new_hourly_salary - current_hourly_salary
        hourly_percent_increase = hourly_salary_diff / current_hourly_salary * 100
        print("You will earn", '£', format(daily_salary_diff, ".2f"), "extra per day")
        print("You will earn", '£', format(hourly_salary_diff, ".2f"), "extra per hour")
        print("This is a increase of", '%', format(hourly_percent_increase, ".2f"))
        holidayvalue_diff = new_holidayvalue - current_holidayvalue

    # Comparison calculations between total package value

        benefit_value_diff = new_benefit_value - current_benefit_value
        total_comp_diff = new_totalvalue + holidayvalue_diff - current_totalvalue

        print("Your new benefits are worth", '£', int(benefit_value_diff), "more than your old benefits")
        print("Your total package is worth", '£', int(total_comp_diff), "more than your old total package")


salcomp()


# function to print salary information to a file:
def printsalinfo():
    if __name__ == "__main__":
        with open("salinfo.txt", "w") as f:
            print("Current Base Salary", '£', current_salary, file=f)
            print("Current Daily Salary:", '£', format(current_daily_salary, ".2f"), file=f)
            print("Current Hourly Salary:", '£', format(current_hourly_salary, ".2f"), file=f)
            print("Current Annual Bonus:", '£', format(current_bonus, ".2f"), file=f)
            print("Current Annual Employer Pension Contributions:", '£', format(current_pension, ".2f"), file=f)
            print("Current Total Compensation Value:", '£', current_totalvalue, file=f)
            print("Current Value of holiday days:", '£', current_holidayvalue, 'for', current_holidaydays, 'days', file=f)
            if current_days_in_office > 0:
                print("Total weekly current price of commute is:", '£', format(current_weekly_price_of_commute, ".2f"), file=f)
                print("Total yearly current price of commute is:", '£', format(current_yearly_price_of_commute, ".2f"), file=f)
                print("You could have earned", '£', format(current_weekly_value_of_commuting_hours, ".2f"),
              "extra per week instead of commuting", file=f)
                print("You could have earned", '£', format(current_yearly_value_of_commuting_hours, ".2f"),
              "extra per year instead of commuting", file=f)
                print("Your total weekly current cost of commuting is:", '£', format(current_total_weekly_cost_of_commute, ".2f"), file=f)
                print("Your total yearly current cost of commuting is:", '£', format(current_total_yearly_cost_of_commute, ".2f"), file=f)

            print("New Base Salary", '£', new_salary, file=f)
            print("New Daily Salary:", '£', format(new_daily_salary, ".2f"), file=f)
            print("New Hourly Salary:", '£', format(new_hourly_salary, ".2f"), file=f)
            print("New Annual Bonus:", '£', format(new_bonus, ".2f"), file=f)
            print("New Annual Employer Pension Contributions:", '£', format(new_pension, ".2f"), file=f)
            print("New Total Compensation Value:", '£', new_totalvalue, file=f)
            print("New Value of holiday days:", '£', new_holidayvalue, 'for', new_holidaydays, 'days', file=f)
            if new_days_in_office > 0:
                print("Total new weekly price of commute is:", '£', format(new_weekly_price_of_commute, ".2f"), file=f)
                print("Total new yearly price of commute is:", '£', format(new_yearly_price_of_commute, ".2f"), file=f)
                print("You could have earned", '£', format(new_weekly_value_of_commuting_hours, ".2f"),
              "extra per week instead of commuting", file=f)
                print("You could have earned", '£', format(new_yearly_value_of_commuting_hours, ".2f"),
              "extra per year instead of commuting", file=f)
                print("Your new total weekly cost of commuting is:", '£', format(new_total_weekly_cost_of_commute, ".2f"), file=f)
                print("Your new total yearly cost of commuting is:", '£', format(new_total_yearly_cost_of_commute, ".2f"), file=f)

            print("You will earn", '£', format(daily_salary_diff, ".2f"), "extra per day", file=f)
            print("You will earn", '£', format(hourly_salary_diff, ".2f"), "extra per hour", file=f)
            print("This is a increase of", '%', format(hourly_percent_increase, ".2f"), file=f)


printsalinfo()
