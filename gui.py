from flask import Flask, render_template, request, session
from antlr4 import *
import antlr4 as antlr4
from decafLexer import decafLexer
from decafListener import decafListener
from decafParser import decafParser
import tables as visitor
import inter as inter

app  = Flask(__name__)
app.secret_key = "el topo mayor"


@app.route('/')
def home():
    errors = []
    return render_template("home.html")

@app.route('/', methods = ["POST"])
def get_code():
    errors = []
    code = ""
    code = request.form["codigo"]
    session.code = code
    print("errores", errors)
    if code!= " ":
        text = antlr4.InputStream(code)
        lexer = decafLexer(text)
        stream = CommonTokenStream(lexer)
        parser = decafParser(stream)
        tree = parser.program()
        printer = decafListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        x = visitor.myDecafVisitor()
        x.visit(tree)
        errors = x.ERRORS
        interm = inter.Inter(x.total_scopes)
        interm.visit(tree)
        intercode = interm.line.split("\n")
    else:
        errors = []
    return render_template("home.html", errors = errors, code = code, intercode = intercode)



if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug = True)