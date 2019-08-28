from .models import Link 
#Con esto podres rescatar el enlace y pasando la clave del diccionario (la clave es la 'key') muestra el url que los saca de la base de datos 
def ctx_dict(resquest):
    #aca se crea el diccionario
    ctx = {}
    #aca creamos la variable para que obtenga todos los objetos de la base de datos, en este caso los enlaces 
    links = Link.objects.all()
    #aca hacemos un for i en la variable donde estan todos estos enlaces 
    for link in links:
        #y a cada iteración se le asigna a la clave (que es la key que predefinimos en el admin) y la relacionamos con un enlace
        ctx[link.key] = link.url 
    return ctx