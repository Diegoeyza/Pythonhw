import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'es': 'ASIGN',
    'lista': 'LISTA'
}

tokens = [
    'ELEMENT',
    'ID'
] + list(reserved.values())

t_ASIGN = r'es'
t_LISTA = r'lista'
t_ignore = ' \t'

element_values = {
    'tierra': 'tierra',
    'agua': 'agua',
    'aire': 'aire',
    'fuego': 'fuego',
    'barro': 'barro'
}

elements = list(element_values.values())

# Token functions
def t_ELEMENT(t):
    r'tierra|agua|aire|fuego|barro'
    t.value = element_values[t.value]
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print(":(")
    t.lexer.skip(1)

precedence = ()
variables = {}

def p_resultado(t):
    'resultado : s'
    print(t[1])

def p_lista(t):
    'resultado : LISTA'
    print_all_combinations()

def p_asignacion(t):
    'resultado : ID ASIGN s'
    variables[t[1]] = t[3]

def p_expr_element(t):
    's : ELEMENT'
    t[0] = t[1]

def p_expr_id(t):
    's : ID'
    try:
        t[0] = variables[t[1]]
    except LookupError:
        print(f"Variable indefinida '{t[1]}'")
        t[0] = ''

def p_expr_combination(t):
    '''s : s s'''
    t[0] = combine_elements(t[1], t[2])+"\n"

def p_error(t):
    print(":'(")

def combine_elements(e1, e2):
    combinations = {
        ('tierra', 'agua'): 'barro',
        ('agua', 'aire'): 'lluvia',
        ('aire', 'fuego'): 'humo',
        ('fuego', 'tierra'): 'lava',
        ('tierra', 'aire'): 'polvo',
        ('agua', 'fuego'): 'vapor',
        ('barro', 'agua'): 'musgo',
        ('barro', 'aire'): 'geiser',
        ('barro', 'fuego'): 'arcilla',
        ('barro', 'tierra'): 'piedra',
    }
    if (e1, e2) in combinations:
        return combinations[(e1, e2)]
    elif (e2, e1) in combinations:
        return combinations[(e2, e1)]
    else:
        return f"Estos elementos no pueden ser combinados :(\n"

def print_all_combinations():
    combinations = {
        ('tierra', 'agua'): 'barro',
        ('agua', 'aire'): 'lluvia',
        ('aire', 'fuego'): 'humo',
        ('fuego', 'tierra'): 'lava',
        ('tierra', 'aire'): 'polvo',
        ('agua', 'fuego'): 'vapor',
        ('barro', 'agua'): 'musgo',
        ('barro', 'aire'): 'geiser',
        ('barro', 'fuego'): 'arcilla',
        ('barro', 'tierra'): 'piedra',
    }
    print("\nTodas las combinaciones posibles son:")
    printed_pairs = set()
    for e1 in elements:
        for e2 in elements:
            if e1 != e2 and (e2, e1) not in printed_pairs and ("no pueden ser combinados" not in combine_elements(e1, e2)):
                result = combine_elements(e1, e2)
                print(f"{e1} + {e2} = {result}")
                printed_pairs.add((e1, e2))
    print("\n")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
