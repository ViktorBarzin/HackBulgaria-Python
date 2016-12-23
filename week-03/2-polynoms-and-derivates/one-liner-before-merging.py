import re


def get_first_derivative(equation, var='x'):
    # prepare_answer(1,'2',2)
    return (str(0)) if \
        len([0 if var not in x else
             # prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:])
             #                    if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0
             #                    else 1), var, 1)

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
                        # str(prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1)
                        #                , var
                        #                , 1))
                        # (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1) + '*' + var + '^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 != 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1) + '*' + var) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) > 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * 1)
                        str(((str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1)) + '*') if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) > 2 else '') + var + ('^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1)) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 > 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1)) + '*' + var)


                        # str(((str(power) + '*') if power > 2 else '') + var + ('^' + str(power - 1)) if power - 1 > 1 else '1')
                        # power = int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1)

    if '*' not in x
    else
                        # prepare_answer(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:])
                        #     if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0
                        #     else 1), var, int(x[:x.find('*')]))

                        (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])) + '*' + var + '^' + str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) - 1 != 1 else str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])) + '*' + var) if int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) > 1 else (str(int(str(re.findall('[' + var + ']+.[0-9]+', x)[0][2:]) if len(re.findall('[' + var + ']+.[0-9]+', x)) > 0 else 1) * int(x[:x.find('*')])))
                        for x in re.split('- | +', equation)
                        if x != '+' and x != '-' and not re.match('^[0-9]$', x)]))

# def prepare_answer(power, variable, coeff):
#     # coeff += 10
#     # power += 10
#     print(coeff,power)
#     # raise TypeError()
#     if power > 1:
#         return (str(power * coeff) + '*' + variable + '^' + str(power - 1) if power - 1 != 1 else str(power * coeff) + '*' + variable)
#     return (str(power * coeff))


# print(get_first_derivative('1 + y + y^2 + 2*y^3 + 3*y^2 + 6*y^4', 'y'))
print(get_first_derivative('x', 'x'))
# todo: check what inside mechnism broke and finish replacing the last prepare_answer func and del '\n'
# s