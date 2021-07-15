import re
import webbrowser
import speech_recognition as sr
import linecache
import ply.lex as lex
import ply.yacc as yacc
from sub import subs
from sub import polishDel
import os


tokens = (
    'OPEN', 'PATH', 'CLOSE', 'AND', 'LISTEN'
)

# Tokens
t_AND = r'\b([Ii] | [Oo]raz)\b'
t_CLOSE = r'\b([Zz]amknij | [Zz]ako[nń]cz | [Zz]amkn[ąa][cć] | [Zz]ako[nń]czy[cć])\b'
t_OPEN = r'\b([Oo]tw[oó]rz | [Uu]ruchom | [Oo]tw[oó]rzy[cć] | [Uu]ruchomi[cć])\b'
t_PATH = r'\b(' + re.sub(' ','|',linecache.getline('resources/regex.txt', 4)[:-1]) + r')\b'
t_LISTEN = r'^([Hh]alo | [Ss][łl]uchaj)\b'


def t_error(t):
    t.lexer.skip(1)

# Ignored characters
t_ignore = " \t"

# Build the lexer
lexer = lex.lex()

# funkcje otwierające/zamykające
def onWWW(t):
    t = subs(t)
    searchwww = re.search(r'(www\.|http|\.pl|\.com)', t)
    if not searchwww:
        os.system("start " + t)
    else:
        webbrowser.open(t)
    return

def cExe(t):
    searchexe = re.search('\.exe', t)
    if not searchexe:
        t = polishDel(subs(t))
    else:
        t = polishDel(subs(t[:3]))
    os.system("taskkill /F /IM " + t + ".exe" + " >nul")
    return

# parser
def p_statement_open(t):
    'expression : OPEN PATH'
    onWWW(t[2])
    print("Otwieram " + t[2])

def p_statement_close(t):
    'expression : CLOSE PATH'
    cExe(t[2])
    print("Zamykam " + t[2])

#multiple
def p_statement_open_m(t):
    'expression : OPEN PATH AND PATH'
    print("Otwieram " + t[2] + " oraz " + t[4])
    onWWW(t[2])
    onWWW(t[4])

def p_statement_close_m(t):
    'expression : CLOSE PATH AND PATH'
    print("Zamykam " + t[2] + " oraz "+ t[4])
    cExe(t[2])
    cExe(t[4])

#listen
def p_statement_listen(t):
    """expression : LISTEN"""
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Słucham...")
        audio = r.record(source, duration=4)
        try:
            s = r.recognize_google(audio, language='pl-PL')
            print("Powiedziałeś: " + s)
            parser.parse(s)
        except sr.UnknownValueError:
            print("Nie rozumiem, co powiedziałeś!")
        except sr.RequestError as e:
            print("Błąd połączenia z Google; {0}".format(e))


def p_error(t):
    print('Nieznana składnia')


parser = yacc.yacc()

print('-- Witam w programie Ludzka Konsola! --\nAby przejść do trybu głosowego wpisz: Słuchaj\nAby zakończyć wpisz: Koniec\n-------------------')
while True:
    s = input('>> ')
    if s == 'Koniec' or s == 'koniec':
        print('-- Do zobaczenia! --')
        break
    parser.parse(s.lower())
