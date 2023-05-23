import math

# breakdown of rackspace salary
rs_salary = 49245
rs_daily_salary = float((rs_salary / 260))
rs_hourly_salary = float((rs_daily_salary / 8))
rs_bonus = float(7 / 100 * rs_salary)
rs_pension = float(5 / 100 * rs_salary)

# Value of extra benefits
rs_phi = 622
rs_incprotection = 300
rs_lifecover = 200
rs_holidaydays = 31.5

# hours of work
rs_weeklyhours = 40
# total yearly hours
rs_yearlyhours = rs_weeklyhours * 52

# print(rs_yearlyhours)
# print(rs_yearlyhours * rs_hourly_salary)

rs_totalvalue = int(rs_salary + rs_bonus + rs_pension + rs_phi + rs_incprotection + rs_lifecover)

rs_holidayvalue = int(rs_holidaydays * rs_daily_salary)

print("Rackspace Base Salary", '£', rs_salary)
print("Rackspace Daily Salary:", '£', format(rs_daily_salary, ".2f"))
print("Rackspace Hourly Salary:" ,'£', format(rs_hourly_salary, ".2f"))
print("Rackspace Annual Bonus:", '£', format(rs_bonus, ".2f"))
print("Rackspace Annual Employer Pension Contributions:", '£', format(rs_pension, ".2f"))

print("Rackspace Total Compensation Value:", '£', rs_totalvalue)
print("Rackspace Value of holiday days:", '£', rs_holidayvalue, 'for', rs_holidaydays, 'days')

# following are inputs with details of new salary/offer


# breakdown of new salary
new_salary = int(input("Enter New Salary: ",))
days_perweek = int(input("Enter Days worked per week: ",))
new_daily_salary = float((new_salary / 260*(5/days_perweek)))
print(new_daily_salary)
new_hourly_salary = float((new_daily_salary / 8))
new_bonus = int(input("Enter New Bonus Percentage: ",)) / 100 * new_salary
new_pension = int(input("Enter New Employer Pension Contribution: ",)) / 100 * new_salary

# Value of extra benefits
new_phi = 622
new_incprotection = 300
new_lifecover = 200
new_holidaydays = int(input("Enter New Holiday Days: ",)) * days_perweek/5

if days_perweek < 5:
    print("You are entitled to", new_holidaydays, "days holiday")

# hours of work
new_weeklyhours = float(input("Enter New Weekly Hours: ",))
# total yearly hours
new_yearlyhours = new_weeklyhours * 52

# print(new_yearlyhours)
# print(new_yearlyhours * new_hourly_salary)

new_totalvalue = int(new_salary + new_bonus + new_pension + new_phi + new_incprotection + new_lifecover)

new_holidayvalue = int(new_holidaydays * new_daily_salary)

print("New Base Salary", '£', new_salary)
print("New Daily Salary:", '£', format(new_daily_salary, ".2f"))
print("New Hourly Salary:", '£', format(new_hourly_salary, ".2f"))
print("New Annual Bonus:", '£', format(new_bonus, ".2f"))
print("New Annual Employer Pension Contributions:", '£', format(new_pension, ".2f"))

print("New Total Compensation Value:", '£', new_totalvalue)
print("New Value of holiday days:", '£', new_holidayvalue, 'for', new_holidaydays, 'days')
