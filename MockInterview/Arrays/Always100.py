def evaluate_expression(expression):
    # Evaluate the expression and return the result
    return eval(expression)

def generate_expressions(numbers, current_expression, index, target, results):
    if index == len(numbers):
        if evaluate_expression(current_expression) == target:
            results.append(current_expression)
        return

    # Add the current number to the expression
    generate_expressions(numbers, current_expression + numbers[index], index + 1, target, results)

    # Add the current number with a '+' operator
    generate_expressions(numbers, current_expression + '+' + numbers[index], index + 1, target, results)

    # Add the current number with a '-' operator
    generate_expressions(numbers, current_expression + '-' + numbers[index], index + 1, target, results)

def find_expressions_to_100():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    target = 100
    results = []
    generate_expressions(numbers, numbers[0], 1, target, results)
    return results

def main():
    results = find_expressions_to_100()
    for result in results:
        print(result)

if __name__ == '__main__':
    main()