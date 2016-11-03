import re


def get_first_derivative(equation, var='x'):
    return (str(0)) if \
        len([0 if var not in x else
             # prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:])
             #                    if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0
             #                    else 1), var, 1)
            # A-3, B-3
             (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1) + '*' + var + '^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 != 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1) + '*' + var) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:])
                                if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0
                                else 1) > 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1)
             if '*' not in x
             else
             # prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:])
             #                         if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0
             #                         else 1), var, int(x[:x.find('*')]))

             (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])) + '*' + var + '^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 != 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])) + '*' + var)
             if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) > 1
             else  (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])))


             for x in re.split('- | +', equation)
             if x != '+' and x != '-' and not re.match('^[0-9]$', x)]) == 0 \
        else ('+'.join([0
                        if var not in x
                        else
                        # todo: fix a bug
                        # prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1)
                        #                , var
                        #                , 1)
                        # (str(power * coeff) + '*' + variable + '^' + str(power - 1) if power - 1 != 1 else str(power * coeff) + '*' + variable) if power > 1 else str(power * coeff)
                        (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1) + '*' + var + '^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 != 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1) + '*' + var) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) > 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1)
                        # power = int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1)

    if '*' not in x
    else
                        # prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:])
                        #     if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0
                        #     else 1), var, int(x[:x.find('*')]))

                        (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])) + '*' + var + '^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 != 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])) + '*' + var) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) > 1 else (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])))
                        for x in re.split('- | +', equation)
                        if x != '+' and x != '-' and not re.match('^[0-9]$', x)]))

def prepare_answer(power, variable, coeff):
    # power += 10
    if power > 1:
        return (str(power * coeff) + '*' + variable + '^' + str(power - 1) if power - 1 != 1 else str(power * coeff) + '*' + variable)
    return (str(power * coeff))


print(get_first_derivative('4 + y + y^1 + y^3 + 2*y^3 + 3*y^2 + 6*y^4', 'y'))