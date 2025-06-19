import sys

import ast
import operator as op


# supported operators
operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
    ast.USub: op.neg
}


def eval_expr(expr):
    """
    Safe eval function, only allows basic mathematical operations
    """
    return calculate(ast.parse(expr, mode='eval').body)


def calculate(node):
    print(f'Node: {node}')
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = calculate(node.left)
        right = calculate(node.right)
        print(f'left: {left}, right: {right}, op: {type(node.op)}')
        return operators[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](calculate(node.operand))
    else:
        raise TypeError(node)


if __name__ == '__main__':
    try:
        with open('calculator/expression.txt', 'r') as f:
            expression = f.read().strip()
    except FileNotFoundError:
        print('calculator/expression.txt not found.')
        print('Usage: Please create calculator/expression.txt with the expression to evaluate')
        sys.exit(1)

    result = eval_expr(expression)
    print(result)
