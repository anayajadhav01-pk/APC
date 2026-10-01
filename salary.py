def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    gross = basic + hra + da

    return gross


def deductions(gross):
    return gross * 0.05


def net_salary(gross, deduction):
    return gross - deduction