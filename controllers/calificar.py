@auth.requires_login()
def index(): return dict(message="Bienvenido")

@auth.requires(auth.has_membership(role='admin')or(auth.has_membership(role="Profesores")))
@auth.requires_login()
def calificar():
    
    tabla = SQLTABLE(db.materias.select(db.materias.ALL))#db.materias.ALL, distinct=True    auth.user.id==
    materias = SQLTABLE(tabla)
    titulo = T(' Ingreso de Calificaciones ')
    return dict(form = materias,titulo = titulo)

@auth.requires(auth.has_membership(role="Profesores"))
def ingresoNotas():
    
    listado = SQLFORM(db.calificacion)
    if form.accepts(request.vars,session):
        response.flash='Calificacion registrada'
    elif form.errors:
        response.flash='Hay uno o mas errores en la tabla'
    else:
        response.flash='complete el formulario'
    titulo = T(' Listado de alumnos ')
    return dict(listado = listado, titulo = titulo)
