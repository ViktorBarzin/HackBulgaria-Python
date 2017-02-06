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
    method_calls = composition.replace('.','').split()
    # print(method_calls)
    # print(functions)
    functions_sorted_by_call =[]

    # put functions in call order
    for call in method_calls:
        functions_sorted_by_call.append([x for x in functions if call in x][0])

    function_parameter_output = [x.replace('::', ' ').replace('->', ' ').split()[1::] for x in functions_sorted_by_call]
    # print(function_parameter_output)
    final_parameter_output_list = []

    for param in function_parameter_output:
        final_parameter_output_list.extend(list(reversed(param)))
    final_parameter_output_list = final_parameter_output_list[1:-1:]

    #:print(final_parameter_output_list)
    # check if valid ocmposition:
    for i in range(0, len(final_parameter_output_list), 2):
        #print(final_parameter_output_list[i]==final_parameter_output_list[i+1])
        if not final_parameter_output_list[i]==final_parameter_output_list[i+1]:
            print('False')
            return
    # print(final_parameter_output_list)
    print('True')
if __name__ == '__main__':
    main()

