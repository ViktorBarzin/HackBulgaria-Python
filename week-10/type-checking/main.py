import sys

class Function:
    def __init__(self, str):
        # print(str.split())
        commands = str.split()
        name = commands[0]
        parameter = commands[2]
        output = commands[4]

        self.name = name
        self.parameter = parameter
        self.output = output

    def __str__(self):
        return '{0}'.format(self.name)

    def __repr__(self):
        return self.__str__()

    def composition(self, function):
        return self.output == function.parameter


def main():
    inpt = list(sys.stdin)
    composition = inpt[-1]

    functions = [x.replace('\n', '') for x in inpt[:-2:] if x != '']
    # print(functions)
    # print(functions)
    parsed_functions = []
    function_names = []
    for f in functions:
        new_func = Function(f)
        parsed_functions.append(new_func)
        function_names.append(new_func.name)

    # print(parsed_functions)

    method_calls = composition.replace('.', '').split()
    # print(method_calls)

    for i in range(len(method_calls) - 1):
        if not parsed_functions[function_names.index(method_calls[i])].composition(parsed_functions[function_names.index(method_calls[i + 1])]):
            # print('this is not a valid composition')

            print('False')
            return

    print('True')
    # print("everything's OK and this is a valid composition.")

if __name__ == '__main__':
    main()
