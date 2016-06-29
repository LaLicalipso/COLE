# coding: utf8
# intente algo como
def asignarPermiso():
    listado = db(db.auth_user.registration_key == 'pending').select(db.auth_user.id,db.auth_user.dni, db.auth_user.first_name, db.auth_user.last_name, db.auth_user.email,db.auth_user.registration_key)

    tabla = SQLTABLE((listado),
    headers={'auth_user.id':'ID', 
                 'auth_user.dni':'DNI', 
                 'auth_user.first_name':'Nombre',
                 'auth_user.last_name':'Apellido',
                 'auth_user.email':'E-mail',
                 'auth_user.registration_key':'Estado'},
                 linkto ='editar')
    form=SQLFORM(db.auth_membership)
    if form.accepts(request.vars,session):
        response.flash='Se asigno membresia'
    return dict (form = form, tabla = tabla)

def editar():
    id = request.args[1]
    query = db(db.auth_user.id == id).select(db.auth_user.last_name,db.auth_user.first_name,db.auth_user.registration_key)
    form = SQLFORM(db.auth_user, id, fields = ['last_name','first_name','registration_key'] )
    if form.accepts(request.vars,session):
        response.flash = 'Listo!'
        redirect(URL(r=request, f='asignarPermiso'))
    elif form.errors:
        response.flash = 'Hay uno o mas errores'
    return dict(form = form)
