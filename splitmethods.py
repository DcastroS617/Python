##funciones para retornar splits de frases xd
Frase = []

##split de un string cualquiera, retorna un arreglo con cada uno de los caracteres.
def split(frase):
    split = []
    for w in frase:
        split.append(w)
    return split

##split que puede tomar un arreglo con filtros o un caracter cualquiera a filtrar, retorna
##un arreglo sin el caracter en la frase
def splice(frase, filter):
    split = []
    for w in frase:
        if(type(filter) is list):
            if w in filter:
                continue
            else:
                split.append(w)
        else:
            if(w != filter):
                split.append(w)
    return split

##filter retorna un arreglo con los caracteres filtrados apartir del filtro de parametros, 
##este tambien toma un arreglo o un caracter de filtro.
def filter(frase, filter):
    response = []
    for w in frase:
        if(type(filter) is list):
            if w in filter:
                response.append(w)
        else:
            if(w == filter):
                response.append(w)
    return response

##Se encarga de unir un arreglo de caracteres para formar una frase.
def join(frase):
    response = ""
    for w in frase:
        response += w
    return response

##Se encarga de unir un arreglo de caracteres para formar una frase más algun
##caracter que el usuario quiera agregar.
def joinconc(frase, concatenate):
    response = ""
    for w in frase:
        response += w + concatenate
    return response

##Se encarga de reemplazar un caracter en una frase.
def replace(frase, letter, replacement):
    response = []
    for w in frase:
        if(w == letter):
            w = replacement
        response.append(w)
    return response

print(join(splice("probando el nuevo metodo", ['a', ' '])))

