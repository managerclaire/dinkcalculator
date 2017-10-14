#personal finance calculator developed by managerclaire
def DINKcalculator():
    name_a = input("First spouse's name: ")
    name_b = input("Second spouse's name: ")
    #print(name_a + " and " + name_b + " are evaluating job offers. ")
    income_a = ene(name_a)
    income_b = ene(name_b)
    combined_income = income_a + income_b
    print("Gross monthly income: " + '${:,.2f}'.format(combined_income))
    tax = taxes(combined_income)
    monthly_taxes = tax / 12
    print("Approximate monthly taxes: " + '${:,.2f}'.format(monthly_taxes))
    total_expenses = expenses()
    savings = combined_income - total_expenses - monthly_taxes
    print("Approximate monthly savings: " + '${:,.2f}'.format(savings))
    final_savings = retirement(savings)
    print("Retirement balance: " + '${:,.2f}'.format(final_savings))

#pulls name_a or name_b from DINKcalculator()
def ene(name_var):
    valid = False
    while valid == False:
        try:
            ene = int(input("Enter 1 if " + name_var + " is paid an hourly wage or 2 if " + name_var + " is paid a salary: "))
            if ene == 1:
                income = wage(name_var)
                valid = True
            elif ene == 2:
                income = salary(name_var)
                valid = True
        except ValueError:
            print("Please try again.")
    return income

#pulls name_a or name_b from DINKcalculator()
def wage(name_var):
    hoursvalid = False
    wagevalid = False
    while hoursvalid == False:
        hours = input("How many hours does " + name_var + " work per week? ")
        try:
            hours = float(hours)
            hoursvalid = True
        except ValueError:
            hoursvalid = False
    while wagevalid == False:
        wage_var = input("How much does " + name_var + " make per hour? ")
        try:
            wage_var = float(wage_var)
            wagevalid = True
        except ValueError:
            wagevalid = False
    weekly = hours*wage_var
    monthly = weekly*4
    print(name_var + " makes " + '${:,.2f}'.format(weekly) + " per week and approximately " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

#pulls name_a or name_b from DINKcalculator()
def salary(name_var):
    valid = False
    while valid == False:
        yearly = input("What is " + name_var + "'s annual salary? ")
        try:
            yearly = float(yearly)
            valid = True
        except ValueError:
            valid = False
    monthly = yearly / 12
    print(name_var + " makes " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

#pulls combined_income from DINKcalculator()
def taxes(income):
    annual_income = income*12
    tax_income = annual_income - 12700 - 4050*2
    if tax_income <= 18650:
        pct = .10
    elif tax_income <= 75900:
        pct = .15
    elif tax_income <= 153100:
        pct = .25
    elif tax_income <= 233350:
        pct = .28
    elif tax_income <= 416700:
        pct = .33
    elif tax_income <= 470700:
        pct = .35
    else:
        pct = .396
    taxes = tax_income*pct + tax_income*.0765
    return taxes

def expenses():
    valid = False
    r_valid = False
    h_valid = False
    t_valid = False
    f_valid = False
    d_valid = False
    s_valid = False
    while valid == False:
        try:
            exp_option = int(input("Enter 1 if you would like to itemize expenses or 2 to not: "))
            #int input for each expense category
            if exp_option == 1:
                valid = True
                while r_valid == False:
                    try:
                        rent = float(input("Monthly housing costs: "))
                        r_valid = True
                    except ValueError:
                        print("Try again.")
                while h_valid == False:
                    try:
                        health = float(input("Monthly healthcare costs: "))
                        h_valid = True
                    except ValueError:
                        print("Try again.")
                while t_valid == False:
                    try:
                        transportation = float(input("Monthly transportation costs: "))
                        t_valid = True
                    except ValueError:
                        print("Try again.")
                while f_valid == False:
                    try:
                        food = float(input("Monthly food costs: "))
                        f_valid = True
                    except ValueError:
                        print("Try again.")
                while d_valid == False:
                    try:
                        debt = float(input("Monthly debt payments: "))
                        d_valid = True
                    except ValueError:
                        print("Try again.")
                while s_valid == False:
                    try:
                        shopping = float(input("Other monthly expenses: "))
                        s_valid = True
                    except ValueError:
                        print("Try again.")
                total_expenses = rent + health + transportation + food + shopping + debt
                #int input for total expenses
            elif exp_option == 2:
                valid = True
                te_valid = False
                while te_valid == False:
                    try:
                        total_expenses = float(input("Total monthly expenses: "))
                        te_valid = True
                    except ValueError:
                        print("Try again.")
        except ValueError:
            print("Try again.")
    print("Total monthly expenses: " + '${:,.2f}'.format(total_expenses))
    return total_expenses

def retirement(mon_save):
    
    monthly_rate = rate/12
    n_months = years_till*12
    final_savings = balance*(1+monthly_rate)**n_months + ((1+monthly_rate)**n_months-1)/monthly_rate*mon_save
    return final_savings

DINKcalculator()
