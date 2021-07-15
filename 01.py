import re
import urllib.request


szlif = []
sources = ['https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa', 'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-1.htm',
           'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-2.htm', 'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-3.htm',
           'https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-4.htm']

for i in range(5):
    response = urllib.request.urlopen("https://www.ceneo.pl/Narzedzia_i_warsztat;szukaj-szlifierka+k%C4%85towa;0020-30-0-0-{}.htm".format(i))
    page_source = response.read()
    szlif += re.findall(r'data-source-tag="">([A-Za-z0-9 ]+)</a>', str(page_source))

szlif_list = list(set(szlif))

for i in range(len(szlif_list)):
    print(szlif_list[i])