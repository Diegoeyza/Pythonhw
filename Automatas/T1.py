import ply.lex as lex
import ply.yacc as yacc #interprete sintáctico

reserved={
    "mas":"SU",  #suma
    "menos":"RE",
    "es":"ASIGN"

}

tokens=["N","ID"]+list(reserved.values())

t_SU=r"mas"
t_RE=r"menos"
t_ASIGN=r"es"

def t_N(t):
    r"[0,9]+"
    t.value=int(t.value)
    return t

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type=reserved.get(t.value,"ID")
    return t
t_ignore=" \t"  #tabulación

def t_error(t):
    print(":(")
    t.lexer.skip(1)

presedence=(("Left","SU","RE"),)

def p_resultado(t):
    "resultado: s"
    print(t[1])

def p_asignación

def p_expr_op(t):
    '''s : s SU s
     / s RE s'''
     if t[2]=="mas":
        t[0]=t[1]+t[3]
    elif t[2]=="menos":
        t[0]=t[1]-t[3]

lexer=lex.lex()
data=input()
lexer.input(data)

#hasta aquí es la parte léxica

while True:
    tok=lexer.token()
    if not tok:
        break
    print(tok)