from tabulate import tabulate


def future_value_simple_interest(pv, r, n):
    fv = pv * (1 + r * n)
    return round(fv, 3)

def future_value_compound_interest(pv, r, n):
    fv = pv * (1 + r) **n
    return round(fv, 3)

def calculate_the_discount_factor(r, n):
    df = 1/(1 + r)**n
    return round(df, 3)

def discounting_present_value(fv, r, n):
    pv = fv / (1 + r)**n
    return round(pv, 3)



def calculate_future_value_annuity_factor_end_year_payment(r, n):
    """
        Calculate the future value annuity factor for a given interest rate and number of periods when payment is at the end of the
        calendar year.

        Args:
            r (float): The interest rate per period (e.g., 0.1 for 10).
            n (int): The number of periods.

        Returns:
            float: The annuity factor rounded to three decimal places.
    """
    fv_af = ((1 + r)**n - 1) / r
    return round(fv_af, 3)

def calculate_future_value_annuity_factor_start_year_payment(r, n):
    """
        Calculate the future value annuity factor for a given interest rate and number of periods when the payment is at the beginning
        of the calendar year.

        Args:
            r (float): The interest rate per period ( 0.1 for 10%).
            n (int): The number of periods.

        Returns:
            float: The annuity factor rounded to three decimal places.
        """
    fv_af = (((1 + r)**(n + 1) - 1) / r) - 1
    return round(fv_af, 3)


def calculate_present_value_annuity_factor_start_year_payment(r, n):
    """
    Calculate the present value annuity factor for a given interest rate and number of periods when the payment is at the beginning
    of the calendar year.

    Args:
        r (float): The interest rate per period ( 0.1 for 10%).
        n (int): The number of periods.

    Returns:
        float: The annuity factor rounded to three decimal places.
    """
    pv_af = (((1 + r)**(n - 1) - 1) / r * (1 + r)**(n - 1)) + 1
    return round(pv_af, 3)

def calculate_present_value_annuity_factor_end_year_payment(r, n):
    """
    Calculate the present value annuity factor for a given interest rate and number of periods when payment is at the end of the
    calendar year.

    Args:
        r (float): The interest rate per period (e.g., 0.1 for 10).
        n (int): The number of periods.

    Returns:
        float: The annuity factor rounded to three decimal places.

    Example:
        #>>> calculate_annuity_factor(0.1, 4)
        3.17
    """
    af = round(1/r * (1 - 1/(1 + r)**n), 3)
    return af


def calculate_equal_installment_repayment_plan(borrowed_amount, r, n):
    """
    Calculate the equal installment repayment plan.

    Args:
    borrowed_amount (float): The total amount borrowed.
    r (float): The interest rate per period (e.g., 0.1 for 10%).
    n (int): The number of repayment periods.

    Returns:
    str: A formatted table of the repayment plan.

    The table includes:
        - n: Period number
        - C: Installment amount
        - IP: Interest portion of the installment
        - PP: Principal portion of the installment
        - RP: Remaining principal after the installment

    Example:
    # >>> print(calculate_equal_installment_repayment_plan(31700, 0.1, 4))
    ┏━━━━━┳━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┓
    ┃   n ┃     C ┃      IP ┃      PP ┃       RP ┃
    ┣━━━━━╋━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
    ┃   1 ┃ 10000 ┃ 3170    ┃ 6830    ┃ 24870    ┃
    ┣━━━━━╋━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
    ┃   2 ┃ 10000 ┃ 2487    ┃ 7513    ┃ 17357    ┃
    ┣━━━━━╋━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
    ┃   3 ┃ 10000 ┃ 1735.7  ┃ 8264.3  ┃  9092.7  ┃
    ┣━━━━━╋━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
    ┃   4 ┃ 10000 ┃  909.27 ┃ 9090.73 ┃     1.97 ┃
    ┗━━━━━┻━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━┛
    """
    annuity_factor =  calculate_present_value_annuity_factor_end_year_payment(r, n)
    installment = borrowed_amount / annuity_factor

    payment_plan = []
    rp = borrowed_amount

    for i in range(1, n + 1):
        ip = rp * r
        pp = installment - ip
        rp -= pp
        payment_plan.append({"n": i, "C": round(installment, 2), "IP": round(ip, 2), "PP": round(pp, 2), "RP": round(rp, 2)})

    return tabulate(payment_plan, headers="keys", tablefmt="heavy_grid")

def calculate_equal_principal_portion_repayment_plan(borrowed_amount, r, n):
    """
    Calculate the equal principal portion payment plan.

    Args:
        borrowed_amount (float): the total amount borrowed
        r (float): The interest rate per period (e.g., 0.1 for 10%)
        n (int): The number of repayment periods

    Returns:
    str: A formatted table of the repayment plan.

    The table includes:
        - n: Period number
        - C: Installment amount
        - IP: Interest portion of the installment
        - PP: Principal portion of the installment
        - RP: Remaining principal after the installment

     Example:
        #>>> print(calculate_equal_principal_portion_repayment_plan(31700, 0.1, 4))
        ┏━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━┳━━━━━━━┓
        ┃   n ┃       C ┃     IP ┃   PP ┃    RP ┃
        ┣━━━━━╋━━━━━━━━━╋━━━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   1 ┃ 11095   ┃ 3170   ┃ 7925 ┃ 23775 ┃
        ┣━━━━━╋━━━━━━━━━╋━━━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   2 ┃ 10302.5 ┃ 2377.5 ┃ 7925 ┃ 15850 ┃
        ┣━━━━━╋━━━━━━━━━╋━━━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   3 ┃  9510   ┃ 1585   ┃ 7925 ┃  7925 ┃
        ┣━━━━━╋━━━━━━━━━╋━━━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   4 ┃  8717.5 ┃  792.5 ┃ 7925 ┃     0 ┃
        ┗━━━━━┻━━━━━━━━━┻━━━━━━━━┻━━━━━━┻━━━━━━━┛
    """
    payment_plan = []

    pp = borrowed_amount / n
    rp = borrowed_amount

    for i in range(1, n + 1):
        ip = rp * r
        installment = pp + ip
        rp -= pp
        payment_plan.append({"n": i, "C": round(installment, 2), "IP": round(ip, 2), "PP": round(pp, 2), "RP": round(rp, 2)})

    return tabulate(payment_plan, headers="keys", tablefmt="heavy_grid")


def calculate_equal_principal_portion_changeable_ip_repayment_plan(borrowed_amount, r1, r2,  n1, n2):
    """
    Calculate the equal principal portion payment plan with overtime changeable interest rate.

    Args:
        borrowed_amount (float): the total amount borrowed
        n1 (int): The number of the first repayment period
        n2 (int): The number of the second repayment period
        r1 (float): The interest rate for the first period (e.g., 0.1 for 10%)
        r2 (float): The interest rate for the second period (e.g., 0.08 for 8%)

    Returns:
    str: A formatted table of the repayment plan.

    The table includes:
        - n: Period number
        - C: Installment amount
        - IP: Interest portion of the installment
        - PP: Principal portion of the installment
        - RP: Remaining principal after the installment

     Example:
        # >>> print(calculate_equal_principal_portion_changeable_ip_repayment_plan(31700, 0.1, 0.08, 4, 2))
        ┏━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━┓
        ┃   n ┃     C ┃   IP ┃   PP ┃    RP ┃
        ┣━━━━━╋━━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   1 ┃ 11095 ┃ 3170 ┃ 7925 ┃ 23775 ┃
        ┣━━━━━╋━━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   2 ┃  9827 ┃ 1902 ┃ 7925 ┃ 15850 ┃
        ┣━━━━━╋━━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   3 ┃  9193 ┃ 1268 ┃ 7925 ┃  7925 ┃
        ┣━━━━━╋━━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━━┫
        ┃   4 ┃  8559 ┃  634 ┃ 7925 ┃     0 ┃
        ┗━━━━━┻━━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━━┛

    """

    payment_plan = []

    pp = borrowed_amount / n1
    rp = borrowed_amount

    for i in range(1, n1 + 1):
        if i == n2:
            break
        ip = rp * r1
        installment = pp + ip
        rp -= pp
        payment_plan.append({"n": i, "C": round(installment, 2), "IP": round(ip, 2), "PP": round(pp, 2), "RP": round(rp, 2)})

    for i in range(n2, n1 + 1):

        ip = rp * r2
        installment = pp + ip
        rp -= pp
        payment_plan.append({"n": i, "C": round(installment, 2), "IP": round(ip, 2), "PP": round(pp, 2), "RP": round(rp, 2)})

    return tabulate(payment_plan, headers="keys", tablefmt="heavy_grid")


def calculate_equal_installment_changeable_ip_repayment_plan(borrowed_amount, r1, r2,  n1, n2):
    """
    Calculate the equal installment changeable ip repayment plan with overtime changeable interest rate.

    Args:
        borrowed_amount (float): the total amount borrowed
        n1 (int): The number of the first repayment period
        n2 (int): The number of the second repayment period
        r1 (float): The interest rate for the first period (e.g., 0.1 for 10%)
        r2 (float): The interest rate for the second period (e.g., 0.08 for 8%)

    Returns:
    str: A formatted table of the repayment plan.

    The table includes:
        - n: Period number
        - C: Installment amount
        - IP: Interest portion of the installment
        - PP: Principal portion of the installment
        - RP: Remaining principal after the installment

     Example:
        # >>> print(calculate_equal_principal_portion_changeable_ip_repayment_plan(31700, 0.1, 0.08, 4, 2))
        ┏━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┓
        ┃   n ┃        C ┃      IP ┃      PP ┃       RP ┃
        ┣━━━━━╋━━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
        ┃   1 ┃ 10000    ┃ 3170    ┃ 6830    ┃ 24870    ┃
        ┣━━━━━╋━━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
        ┃   2 ┃ 10000    ┃ 2487    ┃ 7513    ┃ 17357    ┃
        ┣━━━━━╋━━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
        ┃   3 ┃  9734.72 ┃ 1388.56 ┃ 8346.16 ┃  9010.84 ┃
        ┣━━━━━╋━━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━━┫
        ┃   4 ┃  9734.72 ┃  720.87 ┃ 9013.85 ┃    -3.01 ┃
        ┗━━━━━┻━━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━┛

    """

    payment_plan = []
    annuity_factor =  calculate_present_value_annuity_factor_end_year_payment(r1, n1)
    installment = borrowed_amount / annuity_factor

    rp = borrowed_amount

    for i in range(1, n1 + 1):
        ip = rp * r1
        pp = installment - ip
        rp -= pp
        payment_plan.append(
            {"n": i, "C": round(installment, 2), "IP": round(ip, 2), "PP": round(pp, 2), "RP": round(rp, 2)})

        if i == n2:
            break

    annuity_factor =  calculate_present_value_annuity_factor_end_year_payment(r2, n2)
    installment = rp / annuity_factor

    for i in range(n2 + 1, n1 + 1):

        ip = rp * r2
        pp = installment - ip
        rp -= pp
        payment_plan.append(
            {"n": i, "C": round(installment, 2), "IP": round(ip, 2), "PP": round(pp, 2), "RP": round(rp, 2)})

    return tabulate(payment_plan, headers="keys", tablefmt="heavy_grid")



# print(calculate_annuity_factor(0.08, 2))
# print(calculate_equal_installment_repayment_plan(31700, 0.1, 4))
# print(calculate_equal_principal_portion_repayment_plan(31700, 0.1, 4))
# print(calculate_equal_principal_portion_changeable_ip_repayment_plan(31700, 0.1, 0.08, 4, 2))
# print(calculate_equal_installment_changeable_ip_repayment_plan(31700, 0.1, 0.08, 4, 2))