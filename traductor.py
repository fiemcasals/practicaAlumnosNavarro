
# pip install deep-translator  #llamamos a la libreria para la traduccion...

# from deep_translator import GoogleTranslator   #inportamo la libreria. 



# Creamos el traductor...
# translator = GoogleTranslator(source='en', target='es')  # llamamos a  las fuente source (español) y target (ingles).

# Traducimos una frase.
traducido = translator.translate("Good morning, how are you?")
print(traducido)  # -> "Buenos días, ¿cómo estás?"

# creo una funcion para traducir de manera automatica...
def traducir(texto: str, de: str = 'en', a: str = 'es') -> str: # dentro de la funcion tenemos. texto: la cadena que queremos traducir
 # de: idioma origen , a: idioma destino(español).

    traductor = GoogleTranslator(source=de, target=a)
    return traductor.translate(texto) # retornamos en texto lo que traduzcas.

# Uso:
print(traducir("What time is it?"))  # ¿Qué hora es?
