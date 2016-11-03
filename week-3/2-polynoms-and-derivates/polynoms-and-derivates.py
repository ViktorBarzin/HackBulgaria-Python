import re


def get_first_derivative(equation, var):
    monomials = re.split('- | +', equation)
    res = [differentiate(x, var) for x in monomials if x != '+' and x != '-' and not re.match('^[0-9]$', x)]
    if len(res) == 0:
        return '0'
    print(res)
    return '+'.join(res)


def differentiate(monomial, variable):
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

# print(get_first_derivative('4 + y + y^1 + y^3 + 2*y^3 + 3*y^2 + 6*y^4', 'y'))
# print(get_first_derivative('4*x^3', 'x'))