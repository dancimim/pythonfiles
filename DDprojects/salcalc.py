from DDprojects.salcompfunc import new_benefit_value, current_benefit_value, new_totalvalue, current_totalvalue, \
    new_daily_salary, current_daily_salary, new_hourly_salary, current_hourly_salary, new_holidayvalue, \
    current_holidayvalue, currsal, newsal


def salcomp():
    # Comparison calculations between current and new salary
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


currsal()
newsal()
salcomp()
