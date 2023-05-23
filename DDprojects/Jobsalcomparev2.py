import math

# breakdown of current salary
current_salary = int(input("Enter current Salary: ",))
current_daily_salary = float((current_salary / 260))
current_hourly_salary = float((current_daily_salary / 8))
current_bonus = float(input("Enter Bonus Percentage: ",)) / 100 * current_salary
current_pension = float(input("Enter Pension Percentage: ",)) / 100 * current_salary

# Value of extra benefits
current_phi = 622
current_incprotection = 300
current_lifecover = 200
current_holidaydays = float(input("Enter Holiday Days: ",))

# hours of work
current_weeklyhours = float(input("Enter Weekly Hours: ",))
# total yearly hours
current_yearlyhours = current_weeklyhours * 52

# print(current_yearlyhours)
# print(current_yearlyhours * current_hourly_salary)

current_benefit_value = current_bonus + current_pension + current_phi + current_incprotection + current_lifecover
current_totalvalue = int(current_salary + current_benefit_value)

current_holidayvalue = int(current_holidaydays * current_daily_salary)

print("current Base Salary", '£', current_salary)
print("current Daily Salary:", '£', format(current_daily_salary, ".2f"))
print("current Hourly Salary:" ,'£', format(current_hourly_salary, ".2f"))
print("current Annual Bonus:", '£', format(current_bonus, ".2f"))
print("current Annual Employer Pension Contributions:", '£', format(current_pension, ".2f"))

print("current Total Compensation Value:", '£', current_totalvalue)
print("current Value of holiday days:", '£', current_holidayvalue, 'for', current_holidaydays, 'days')

# following are inputs with details of new salary/offer


# breakdown of new salary
new_salary = int(input("Enter New Salary: ",))
part_time = input("Is job part time? (y/n)",)

if part_time == 'n':
    days_perweek = 5
else:
    days_perweek = int(input("Enter Days worked per week: ", ))

new_daily_salary = float((new_salary / 260*(5/days_perweek)))
# print(new_daily_salary)
# hours of work
new_weeklyhours = float(input("Enter New Weekly Hours: ",))
# total yearly hours
new_yearlyhours = new_weeklyhours * 52
new_dailyhours = new_weeklyhours / 5

new_hourly_salary = float(new_daily_salary / new_dailyhours)
new_bonus = float(input("Enter New Bonus Percentage: ",)) / 100 * new_salary
new_pension = float(input("Enter New Employer Pension Contribution: ",)) / 100 * new_salary

# Value of extra benefits

phi = input("Will you receive Private Healthcare? (y/n)",)

if phi == 'n':
    new_phi = 0
else:
    new_phi = int(input("Enter Annual Private Healthcare Premium: ", ))

incp = input("Will you receive Income Protection? (y/n)",)

if incp == 'n':
    new_incprotection = 0
else:
    new_incprotection = int(input("Enter Annual Income Protection Premium: ", ))

lifecvr = input("Will you receive Life Cover? (y/n)",)

if lifecvr == 'n':
    new_lifecover = 0
else:
    new_lifecover = int(input("Enter Annual Life Cover Premium: ", ))

new_holidaydays = int(input("Enter New Holiday Days: ",)) * days_perweek/5



# print(new_yearlyhours)
# print(new_yearlyhours * new_hourly_salary)

new_benefit_value =  new_phi + new_incprotection + new_lifecover + new_pension + new_bonus

new_totalvalue = int(new_salary + new_benefit_value)

new_holidayvalue = int(new_holidaydays * new_daily_salary)

print("New Base Salary", '£', new_salary)
print("New Daily Salary:", '£', format(new_daily_salary, ".2f"))
print("New Hourly Salary:", '£', format(new_hourly_salary, ".2f"))
print("New Annual Bonus:", '£', format(new_bonus, ".2f"))
print("New Annual Employer Pension Contributions:", '£', format(new_pension, ".2f"))

if days_perweek < 5:
    print("You are entitled to", new_holidaydays, "days holiday")

print("New Total Compensation Value:", '£', new_totalvalue)
print("New Value of holiday days:", '£', new_holidayvalue, 'for', new_holidaydays, 'days')


# Comparison calculations between current and new salary

daily_salary_diff = new_daily_salary - current_daily_salary
hourly_salary_diff = new_hourly_salary - current_hourly_salary
hourly_percent_increase = hourly_salary_diff/current_hourly_salary * 100
print("You will earn", '£', format(daily_salary_diff, ".2f"), "extra per day")
print("You will earn", '£', format(hourly_salary_diff, ".2f"), "extra per hour")
print("This is a increase of",'%', format(hourly_percent_increase, ".2f"))

# Comparison of holiday value

holidayvalue_diff = new_holidayvalue - current_holidayvalue

# Comparison calculations between total package value

benefit_value_diff = new_benefit_value - current_benefit_value
total_comp_diff = new_totalvalue + holidayvalue_diff - current_totalvalue

print("Your new benefits are worth", '£', int(benefit_value_diff), "more than your old benefits")
print("Your total package is worth", '£', int(total_comp_diff), "more than your old total package")

