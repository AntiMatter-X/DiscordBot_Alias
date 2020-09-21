# https://qiita.com/thtitech/items/91e2456c989ca969850d

class Formula:
    def __init__(self, text):
        self.text = text.replace(" ", "")
        self.pos = 0

    def __bool__(self):
        return self.pos < len(self.text)

    def fetch(self):
        return self and self.text[self.pos] or " "

    def pop(self):
        self.pos += 1
        return self.text[self.pos - 1]


def calculate(formula):
    return expr(Formula(formula))

def expr(formula):
    value = term(formula)
    while formula.fetch() in "+-":
        op = formula.pop()
        if op == "+": value += term(formula)
        elif op == "-": value -= term(formula)
    return value


def term(formula):
    value = factor(formula)
    while formula.fetch() in "*/":
        op = formula.pop()
        if op == "*": value *= factor(formula)
        elif op == "/": value /= factor(formula)
    return value

def factor(formula):
    if formula.fetch() == "(":
        formula.pop()
        value = expr(formula)
        if not formula or formula.pop() != ")": raise IllegalExpressionException()
    else: value = number(formula)
    return value

def number(formula):
    value = ""
    while formula.fetch() in "0123456789.":
        value += formula.pop()
    return ("." in value and float or int)(value)
