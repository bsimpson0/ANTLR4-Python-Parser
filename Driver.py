import sys
from antlr4 import *
from OperatorsLexer import OperatorsLexer
from OperatorsParser import OperatorsParser
from antlr4.tree.Trees import Trees
import graphviz


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = OperatorsLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = OperatorsParser(tokens)
    tree = parser.program()


    print(tree.toStringTree(tree, recog=parser))



if __name__ == '__main__':
    main(sys.argv)

