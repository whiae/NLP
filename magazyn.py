import ply.yacc as yacc
import ply.lex as lex

tokens = (
    'NUMBER',
    'OPERATE',
    'SIZE',
    'KIND',
    'COLOR',
    'MATERIAL'
)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OPERATE(t):
    r'Store | Release'
    return t

def t_SIZE(t):
    r'tiny | small | big | large'
    if t.value == 'tiny':
        t.value = 1
    elif t.value == 'small':
        t.value = 2
    elif t.value == 'big':
        t.value = 3
    elif t.value == 'large':
        t.value = 4
    return t

def t_COLOR(t):
    r'(black | white | red | green | blue)'
    if t.value == 'black':
        t.value = 1
    elif t.value == 'white':
        t.value = 2
    elif t.value == 'red':
        t.value = 3
    elif t.value == 'green':
        t.value = 4
    elif t.value == 'blue':
        t.value = 5
    return t

def t_MATERIAL(t):
    r'metal | plastic | paper'
    if t.value == 'metal':
        t.value = 1
    elif t.value == 'plastic':
        t.value = 2
    elif t.value == 'paper':
        t.value = 3
    return t

def t_KIND(t):
    r'box(es)? | container(s)?'
    if t.value[0] == 'b':
        t.value = 1
    else:
        t.value = 2
    return t

#ERROR HANDLING
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'


#MAIN PARSER RULE
def p_command(p):
    'command : OPERATE NUMBER article'
    index = p[3]
    if p[1] == 'Store':
        tab[index] += p[2]
        print('I am storing ' + str(p[2]) + ' new articles indexed as ' + str(index) + '.')
        print('Number of articles in warehouse: ' + str(tab[index]))
    elif p[1] == 'Release':
        if p[2] > tab[index]:
            print('I do not have as many articles as you want.')
        else:
            tab[index] -= p[2]
            print('I am releasing ' + str(p[2]) + ' articles indexed as ' + str(index) + '.')
            print('Number of articles in warehouse: ' + str(tab[index]))

#PARSER RULES
def p_attribute_color(p):
    'attribute : COLOR'
    p[0] = p[1]

def p_attribute_material(p):
    'attribute : MATERIAL'
    p[0] = 10 * p[1]

def p_attribute_size(p):
    'attribute : SIZE'
    p[0] = 100 * p[1]

def p_article_kind(p):
    'article : KIND'
    p[0] = 1000 * p[1]

def p_article_attribute(p):
    'article : attribute article'
    p[0] = p[1] + p[2]

#ERROR HANDLING
def p_error(p):
    print("Syntax error in input!")


#MAIN LOOP
tab = []
for index in range(3000):
    tab.append(0)

lexer = lex.lex()
parser = yacc.yacc()


while True:
    s = input('What can i do for you? \n')
    if s == 'Bye' or s == 'bye':
        print('Goodbye!')
        break
    parser.parse(s)