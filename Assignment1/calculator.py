import re
import sys
import math

# For this assignment, I had chatgpt help me learn how to create a regex expression to tokenize all the characters
# in the expression. I


class Calculator:
    def __init__(self):
        # This expression will tokenize the usual suspects, as well as '/^' as the root operator
        self.complete_token_pattern = r"\d+\.?\d*|/\^|[+\-*/^()]"
        self.digit_token_pattern = r"\d+\.?\d*"

        # Implementing operations
        self.operations = {
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '^': lambda x, y: math.pow(x, y),
            '/^': lambda x, y: math.pow(x, 1 / y)
        }

        # Tracking which operations are higher priority
        self.operation_priority = {
            '*': 1,
            '/': 1,
            '+': 0,
            '-': 0,
            '^': 2,
            '/^': 2
        }

        self.last_result = 0

    def evaluate(self, expr: str):
        print(f"Evaluating: {expr}")
        self.last_result = self._evaluate(expr)
        return self.last_result

    # Just like normal calculators, can use previous evaluation in union with another expression,
    # as long as the next expression begins with an operator
    def next_evaluate(self, expr: str):
        if any([expr.startswith(oper) for oper in self.operations]):
            return self.evaluate(''.join([str(self.last_result), expr]))
        else:
            raise Exception("Error: next expression must begin with an operator")

    def _evaluate(self, expr: str):
        tokens = self._tokenize(expr)
        return self._parse_eval(tokens)

    # this will tokenize the expression
    def _tokenize(self, expr: str):
        return re.findall(self.complete_token_pattern, expr)

    # iteratively traverse the expression and capture numbers, operators and parentheses
    def _parse_eval(self, tokens: list[str]) -> float:
        values = []
        operators = []

        i = 0
        while i < len(tokens):
            # Find digits
            if re.match(self.digit_token_pattern, tokens[i]):
                values.append(float(tokens[i]))
            # Find parentheses sub expressions
            elif tokens[i] == '(':
                start = i + 1
                opens = 1
                while opens != 0:
                    if i >= len(tokens):
                        raise Exception("Error: Mismatched parentheses")
                    i += 1
                    if tokens[i] == '(':
                        opens += 1
                    elif tokens[i] == ')':
                        opens -= 1
                # Recursively evaluate parentheses expression
                sub_expr = self._evaluate(''.join(tokens[start:i]))
                values.append(sub_expr)
            # Negative number support
            elif tokens[i] == '-' and (i == 0 or tokens[i - 1] in self.operations or tokens[i - 1] == '('):
                i += 1
                if re.match(self.digit_token_pattern, tokens[i]):
                    values.append(-float(tokens[i]))
            # Operators
            elif tokens[i] in self.operations:
                # Only apply operators if the top operator is higher priority than the encountered operator
                while operators and self._get_priority(operators[-1]) >= self._get_priority(tokens[i]):
                    right = values.pop()
                    left = values.pop()
                    operator = operators.pop()
                    values.append(self._apply_operator(left, right, operator))

                # Append operator after check, ensure at least two digits to operate on
                operators.append(tokens[i])

            i += 1

        # Empty remaining operators
        while operators:
            right = values.pop()
            left = values.pop()
            operator = operators.pop()
            values.append(self._apply_operator(left, right, operator))

        return values[0]

    # Get operation priority
    def _get_priority(self, operator: str):
        return self.operation_priority[operator]

    # Apply an operator to 2 digits
    def _apply_operator(self, left, right, operator):
        return self.operations[operator](left, right)


# If no command line expr is given, use this instead
backup_expr = "1+2+(3*4*(5-6^7-8/^9)+10*(11-12))+10*200"
# Example of appended evaluation to previous evaluation result
append_eval_expr = "+10*11-12^3"

if __name__ == "__main__":
    c = Calculator()
    print(sys.argv)
    if len(sys.argv) <= 1:
        print("Result:", c.evaluate(backup_expr))
        print("Next Result:", c.next_evaluate(append_eval_expr))
    else:
        print(c.evaluate(sys.argv[1]))

