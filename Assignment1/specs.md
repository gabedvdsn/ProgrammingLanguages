### Personal Information
Gabriel Davidson\
2338642\
gadavidson@chapman.edu\
CPSC-354 => Assignment 1

## Calculator.py
This calculator can handle the following operators:\
`x + y` `x - y` `x * y` `x / y` `x^y` `x/^y (roots)`

Just like normal calculators, this calculator can handle additional expressions once it has a stored result. This can be called using the `next_evaluate()` method.
For example, calling `evaluate(3*5)` followed by `next_evaluate(+25)` will return `70`. 
### Implementation
>`Calculator`\
>This is the class object that handles all evaluation. I always like to OOP my programming, even though it's not necessarily required in this context.
>#### Fields
>`Calculator.operations: dict[str: lambda(x, y)]` Defines operator implementation as lambda expressions.\
>`Calculator.operation_priority: dict[str: int]` Defines operator priority as ints.\
>`Calculator.complete_token_pattern` Defines the regex string for any acceptable token.\
>`Calculator.digit_token_pattern` Defines the regex string for any digit.

#### Methods

>`Calculator.evaluate(expr: str) -> float`\
This method is the public access to evaluation. Stores the evaluation result and returns a float.

>`Calculator.next_evaluate(expr: str) -> float`\
This method is the public access to next evaluation. Prepends the stored result (default `0`) to the provided expression. The provided expression must begin with an operator. Stores the evaluation result and returns a float.

>`Calculator._evaluate(expr: str) -> float`\
Tokenizes the provided expression. Calls `Calculator._parse_eval(...)`, which may recursively call this method to evaluate sub-expressions within parentheses. Returns a float.

>`Calculator._tokenize(expr: str) -> list[str]`\
Tokenizes the provided expression using `Calculator.complete_token_pattern`.

>`Calculator._parse_eval(tokens: list[str]) -> float`\
Iteratively traverses the `tokens` and captures digits, operators, and sub-expressions within parentheses.
>#### Fields
>`Calculator._parse_eval.values: list[float]`\
>`Calculator._parse_eval.operators: list[str]`
> 
> This method follows the following steps as it traverses `tokens`.
> 1. Match token to digit using `Calculator.digit_token_pattern`. Capture digit to `values`.
> 2. Match token to negative digit by checking for `-` at the start of an expression or directly after an operator using `Calculator.digit_token_pattern`. Capture digit to `values`. 
> 3. Check for parentheses sub-expression. If the token is an opening parentheses:
>    1. Capture entire sub-expression.
>    2. Recursive call to `Calculator._evaluate(sub_expression)`.
>    3. Capture result to `values`.
> 4. Check for operators. If the token is an operator:
>    1. While there are operators in `operators`, and the topmost operator in `operators` is higher priority than the encountered operator:
>       1. Call `Calculator._apply_operator(left, right, oper)`, where `left` and `right` are the two digits at the top of `values`, and `oper` is the topmost operator in `operators`.
>       2. `left`, `right`, and `oper` are popped from their respective lists.
>       3. The result is appended to `values`.
>    2. Add the encountered operator to `operators`.
> 
> After all tokens have been traversed, repeat steps **4.i.a** through **4.i.b** while any operators still exist in `operators`. Returns the final remaining digit in `values`.

>`Calculator._get_priority(operator: str) -> int`\
> Returns the priority of `operator` using `Calculator.operation_priority`.

>`Calculator._apply_operator(left: float, right: float, oper: str) -> float`\
> Returns the result of `oper` on `left` and `right` in the form `oper(left, right)` using `Calculator.operations`.

### References
I used ChatGPT to learn more about writing regex strings and pattern matching.

## Parentheses.py
This script takes in an input string and returns "yes" or "no" based on whether the parentheses are properly balanced.
### Implementation
Since this script was so simple, I did not abstract my functionality into its own class.

#### Methods
>`evaluate(expr: str) -> str`\
> Takes in an expression containing "(" and ")" characters and returns whether the parentheses are properly balanced or not. Returns "yes" if balanced, and "no" if not.

### References
No references.
