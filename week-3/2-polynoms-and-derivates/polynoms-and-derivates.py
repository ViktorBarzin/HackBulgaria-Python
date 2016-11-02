import re


def get_first_derivative(equation, var):
    monomials = re.split('- | +', equation)
    res = [diffenrentiate(x, var) for x in monomials if x != '+' and x != '-' and not re.match('[0-9]$', x)]
    if len(res) == 0:
        return str(0)
    return '+'.join(res)


def diffenrentiate(monomial, variable):
    if variable not in monomial:
        return '0'
    if len(re.findall('[' + variable + ']+.[0-9]+', monomial)) > 0:
        power = int(str(re.findall('[' + variable + ']+.[0-9]+', monomial)[0][2:]))
    else:
        power = 1

    if '*' not in monomial:
        if power > 1:
            if power - 1 != 1:
                return str(power) + '*' + variable + '^' + str(power - 1)
            return str(power) + '*' + variable
        return str(power)
    else:
        coeff = int(monomial[:monomial.find('*')])
        if power > 1:
            if power - 1 != 1:
                return str(power * coeff) + '*' + variable + '^' + str(power - 1)
            return str(power * coeff) + '*' + variable
        return str(power * coeff)
