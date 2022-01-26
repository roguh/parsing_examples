# Chomsky Hierarchy Type 2, artificial language, context-free.
# LALR algorithm (has limited lookahead) is used for parsing.

# External library
from lark import Lark, Tree, lark

# Use Transformer in production to turn Trees into useful values
# from lark import Transformer

START_TOKEN_NAME = "start"


parser: lark.Lark = Lark.open(
    "./calculator.lark",
    rel_to=__file__,
    # Use the faster LALR parsing algorithm
    # Lark also comes with the Earley parser for context-free languages
    parser="lalr",
    start=START_TOKEN_NAME,
)


def parse(string: str) -> str:
    tree: Tree = parser.parse(string)
    return tree.pretty()
