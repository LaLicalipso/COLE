@auth.requires_login()
def index(): return dict(message="Bienvenido")

@auth.requires_login()
def alumnos():
    filas = db().select(db.alumnos.ALL, orderby=db.alumnos.nombre)
    tabla = SQLTABLE((filas),
    headers={'alumnos.id':'ID','alumnos.dni':'DNI','alumnos.nombre':'Apellido (s) y Nombre(s)','alumnos.curso':'Curso','alumnos.sexo':'Sexo','alumnos.fechaIngreso':'Fecha de Ingreso'},linkto = 'editarAlumnos')
    cantidad = 15
    #cantidad = (db(db.alumnos.id > 0).count())
    return dict(tabla = tabla,cantidad = cantidad)
#####
#####
#####    tabla = SQLTABLE((filas),
####   headers={'materias.cupof':'CUPOF','materias.nombre':'Nombre','materias.curso':'Curso','materias.profesor':'Profesor a cargo'},linkto = 'editar')
#####

def materias():
    db.materias.id.readable=False
    query = ((db.materias.id > 0))
    default_sort_order = [db.materias.cupof]
    fields = (db.materias.cupof, db.materias.nombre, db.materias.curso, db.materias.profesor)
    
    headers = {'materias.cupof':   'CUPOF',
                'materias.nombre':   'Nombre',
                'materias.curso':   'Curso',
                'materias.profesor':   'Profesor'}
#agregar lo que quite 
    
    tabla = SQLFORM.grid(query=query, fields=fields, headers=headers, create=False, deletable=False, editable=False, maxtextlength=20, paginate=15, orderby=default_sort_order,)
    
    return dict(tabla = tabla)

#####
#####
#####
#####

@auth.requires_login()
def profesores():
    filas = db(db.auth_user.id > 0 ).select('auth_user.id','auth_user.dni', 'auth_user.last_name', 'auth_user.first_name', 'auth_user.email', 'auth_user.localidad', 'auth_user.telefono',  'auth_user.celular', 'auth_user.fecha_alta', 'auth_user.fecha_baja')#  and auth_membership == 'Profesor'
    tabla = SQLTABLE((filas),
    headers = {'auth_user.id':'ID','auth_user.dni': 'DNI', 'auth_user.last_name':'Nombre', 'auth_user.first_name':'Apellido', 'auth_user.email':'E-Mail',  'auth_user.localidad':'Localidad', 'auth_user.telefono':'Telefono',  'auth_user.celular':'Telefono Particular', 'auth_user.fecha_alta':'Fecha de Ingreso', 'auth_user.fecha_baja':'Fecha de Egreso'}, linkto ='editarProfesores')
    return dict(tabla=tabla)
    
@auth.requires_login()
def cursos():
    filas = db(db.cursos.id > 0).select()
    tabla = SQLTABLE((filas),
    headers = {'cursos.id':'ID','cursos.curso':'Curso','cursos.division':'División','cursos.descripcion':'Descripcion'},linkto = 'editarCursos')
             
    return dict(tabla = tabla)

@auth.requires_login()
def editarAlumnos():
    tabla = T('Alumno')
    id = request.args[1]
    form = SQLFORM(db.alumnos, id, deletable = True)
    if form.accepts(request.vars,session):
        redirect(URL(r=request, f='alumnos'))
        response.flash='Listo!'
    elif form.errors:
        response.flash='Hay uno o mas errores'
    
    return dict(form = form, tabla = tabla)


@auth.requires_login()
def editarProfesores():
    tabla = T('Profesor')
    id = request.args[1]
    form = SQLFORM(db.auth_user, id, fields = ['last_name','first_name','registration_key'] )
    if form.accepts(request.vars,session):
        redirect(URL(r=request, f='profesores'))
        response.flash='Listo!'
    elif form.errors:
        response.flash='Hay uno o mas errores'
    
    return dict(form = form, tabla = tabla)




@auth.requires_login()
def editarCursos():
    tabla = T('Curso')
    id = request.args[1]
    form = SQLFORM(db.cursos, id, deletable = True )
    if form.accepts(request.vars,session):
        redirect(URL(r=request, f='cursos'))
        response.flash='Listo!'
    elif form.errors:
        response.flash='Hay uno o mas errores'
    
    return dict(form = form, tabla = tabla)
