from lark import Lark, Transformer
import math
import sys


class LarkCalculator:
    class LarkCalcTransformer(Transformer):
        def num(self, items):
            return 'num', float(items[0])

        def neg(self, items):
            return 'neg', items[0]

        def plus(self, items):
            return 'plus', items[0], items[1]

        def minus(self, items):
            return 'minus', items[0], items[1]

        def times(self, items):
            return 'times', items[0], items[1]

        def divide(self, items):
            return 'divide', items[0], items[1]

        def exponent(self, items):
            return 'exponent', items[0], items[1]

        def log(self, items):
            return 'log', items[0], items[1]

    def evaluate(self, ast):
        if ast[0] == 'num':
            return ast[1]
        elif ast[0] == 'neg':
            return -self.evaluate(ast[1])
        elif ast[0] == 'plus':
            return self.evaluate(ast[1]) + self.evaluate(ast[2])
        elif ast[0] == 'minus':
            return self.evaluate(ast[1]) - self.evaluate(ast[2])
        elif ast[0] == 'times':
            return self.evaluate(ast[1]) * self.evaluate(ast[2])
        elif ast[0] == 'divide':
            return self.evaluate(ast[1]) / self.evaluate(ast[2])
        elif ast[0] == 'exponent':
            return self.evaluate(ast[1]) ** self.evaluate(ast[2])
        elif ast[0] == 'log':
            return math.log(self.evaluate(ast[1]), self.evaluate(ast[2]))
        else:
            raise Exception(f"Could not evaluate {ast}")


if __name__ == "__main__":
    with open("grammar.lark", "r") as g:
        grammar = g.read()

    parser = Lark(grammar, parser='lalr')

    calculator = LarkCalculator()
    calc_transformer = LarkCalculator.LarkCalcTransformer()

    expr = sys.argv[1]

    parse_tree = parser.parse(expr)
    abstract_syntax_tree = calc_transformer.transform(parse_tree)

    result = calculator.evaluate(abstract_syntax_tree)
    print(result)


