import uuid
#from datetime import datetime

def generar_codigo_curso():
    #año = datetime.now().year
    codigo = uuid.uuid4().hex[:6].upper()  # algo como 'A3F91C'
    #return f"CAP-{año}-{codigo}"
    return f"CAP-{codigo}"

#print(generar_codigo_curso())