### Personal Information
Gabriel Davidson\
2338642\
gadavidson@chapman.edu\
CPSC-354 => Assignment 2

## calculator_cfg.py
This calculator can handle the following operators:\
`x + y` `x - y` `x * y` `x / y` `x^y` `logx(y)`

### Implementation
### >`LarkCalculator`
>This is the class object that performs evaluation.
> #### Methods
>`Calculator.evaluate(ast: AST) -> float`\
This method is the public access to evaluation. Recursively evaluates the AST until all branches reach the base case "num". Returns a float.

### >`LarkCalculator.LarkCalcTransformer`\
> This is the class object that inherits Lark.Transformer and defines operation implementation.
> #### Methods
> `LarkCalculator.LarkCalcTransformer.num(items: list[...]) -> tuple['num', float]`\
> Implementation for numbers. Base case for AST evaluation.
> 
> `LarkCalculator.LarkCalcTransformer.neg(items: list[...]) -> tuple['neg', str]`\
> Implementation for negative numbers.
> 
> `LarkCalculator.LarkCalcTransformer.plus(items: list[...]) -> tuple['plus', str, str]`\
> Implementation for addition (`x + y`)
> 
> `LarkCalculator.LarkCalcTransformer.minus(items: list[...]) -> tuple['minus', str, str]`\
> Implementation for subtraction (`x - y`)
> 
> `LarkCalculator.LarkCalcTransformer.times(items: list[...]) -> tuple['times', str, str]`\
> Implementation for multiplication (`x * y`)
> 
> `LarkCalculator.LarkCalcTransformer.divide(items: list[...]) -> tuple['divide', str, str]`\
> Implementation for division (`x / y`)
> 
> `LarkCalculator.LarkCalcTransformer.exponent(items: list[...]) -> tuple['exponent', str, str]`\
> Implementation for exponentiation (`x ^ y`)
> 
> `LarkCalculator.LarkCalcTransformer.log(items: list[...]) -> tuple['log', str, str]`\
> Implementation for logarithms (`log x base y`)

### References
Alexander Kurz for grammar.lark file.