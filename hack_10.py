"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def mayuscula(letra):
    result = letra.upper()
    return result

def conv(letra):
    letra = letra.replace('o','0')
    letra = letra.replace('i','1')
    letra = letra.replace('a','@')
    return letra

def fn_hack_10():
    result = "fooziman"
    result = list(result)
    result = map(conv, result)
    result = list(result)
    result = map(mayuscula, result)
    result = list(result)
    return result  