import re


# Disclaimer: I know that the following function is really unreadable
# but I had a bet to write it in 1 line so bear with my beautiful and readle masterpiece :)
def get_first_derivative(equation, var):
    # Actual functionality is the following:
    # 1.Splits the equation by '-' and '+'
    # 2.Extracts every monomial and passes it to the differentiate function
    # 3.Does the above for every monomial and returns the concatenation of the results
    # P.S: I will leave the original code to make the refactoring easier :P

    return (str(0)) if len([diffenrentiate(x, var) for x in re.split('- | +', equation) if x != '+'
                            and x != '-'
                            and not re.match('^[0-9]$', x)]) == 0 \
        else ('+'.join([diffenrentiate(x, var) for x in re.split('- | +', equation) if x != '+'
                        and x != '-'
                        and not re.match('^[0-9]$', x)]))

    # LEgacy and readable code below:
    # monomials = re.split('- | +', equation)
    # res = [diffenrentiate(x, var) for x in monomials if x != '+' and x != '-' and not re.match('^[0-9]$', x)]
    # if len(res) == 0:
    #     return '0'
    # return '+'.join(res)

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

print(get_first_derivative('1 +2*x^2', 'x'))