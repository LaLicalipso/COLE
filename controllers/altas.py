# coding: utf8
@auth.requires(auth.has_membership(role='admin')or(auth.has_membership(role="Preceptores")))

def index(): return dict(message="Bienvenido")



def Materias():
    form= SQLFORM(db.materias)
    if form.accepts(request.vars,session):
        response.flash='Materia ingresada a la base'
    elif form.errors:
        response.flash='Hay uno o mas errores en la tabla'
    else:
        response.flash='complete el formulario'
    titulo = T(' Alta de Materias ')
    return dict(form = form,titulo = titulo)


def alumnos():
    form= SQLFORM(db.alumnos)
    if form.accepts(request.vars,session):
        response.flash='Alumno ingresado a la base'
    elif form.errors:
        response.flash='Hay uno o mas errores en la tabla'
    else:
        response.flash='complete el formulario'
    titulo = ' Alta de Alumnos '
    return dict(form = form,titulo = titulo)
    
@auth.requires(auth.has_membership(role='admin')or(auth.has_membership(role="Preceptores")))
@auth.requires_login()
def cursos():
    form= SQLFORM(db.cursos)
    if form.accepts(request.vars,session):
        response.flash='Curso ingresado a la base'
    elif form.errors:
        response.flash='Hay uno o mas errores en la tabla'
    else:
        response.flash='complete el formulario'
    titulo = ' Ingreso de Cursos '
    return dict(form = form,titulo = titulo)
