#!/usr/bin/env python3

"""
Hello World Multilinguas

Dependendo da lingua config no ambiente
o programa exibe a mensagem correspondente

Como usar:

Ter a variavel LANG devidmente configrada

    Ex: export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
# Este programa imprime Hello World!
__version__ = "0.0.1"
__author__  = "Luis Garavatti"
__license__ = "Unlicense"

import os

#Coletando o idioma de pelo ambiente, e caso nao tenha variavel definida pegar en_US
current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bounjour, Monde!"
print(msg)