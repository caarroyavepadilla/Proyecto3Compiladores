import sys
from antlr4 import *
import antlr4 as antlr4
from decafLexer import decafLexer
from decafListener import decafListener
from decafParser import decafParser
from decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees
import tables as visitor
import typeSystem as tables
import inter as inter
import arm


def main():
    program = open('test.txt', 'r+')
    text = program.read()
    program.close()
    text = antlr4.InputStream(text)
    lexer = decafLexer(text)
    stream = CommonTokenStream(lexer)
    parser = decafParser(stream)
    tree = parser.program()
    printer = decafListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    x = visitor.myDecafVisitor()
    x.visit(tree)
    interm = inter.Inter(x.total_scopes)
    interm.visit(tree)
    arm.compose_arm(interm.line, x.total_scopes)
if __name__ == '__main__':
    main()