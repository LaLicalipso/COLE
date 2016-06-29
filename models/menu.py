# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################


#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'El payaso plin plin'
response.meta.description = 'Free and open source full-stack enterprise framework for agile development of fast, scalable, secure and portable database-driven web-based applications. Written and programmable in Python'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2007-2010'


##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Inicio'), False, URL('default','index'), []),
    
    (T('Altas'), False, URL('Altas','index'), [
    (T('Alumnos'), False, URL('Altas','alumnos')),
    (T('Cursos'), False, URL('Altas','cursos')),
    (T('Materias'), False, URL('Altas','Materias'))
    ]),
    
    (T('Listados'), False, URL('Listas','index'), [
    (T('Alumnos'), False, URL('Listas','alumnos')),
    (T('Cursos'), False, URL('Listas','cursos')),
    (T('Materias'), False, URL('Listas','materias')),
    (T('Profesores'), False, URL('Listas','profesores'))
    ]),
    
    (T('Buscar'), False, URL('Buscar','index'), [    
    ]),
    
    
    (T('Calificar'), False, URL('Calificar','index'), [    
    ]),
    
    (T('Administrador'), False, URL('Admin','asignarPermiso'), [    
    ])
    
    ]
##########################################
## this is here to provide shortcuts
## during development. remove in production
##
## mind that plugins may also affect menu
##########################################

#########################################
## Make your own menus
##########################################




##########################################
## this is here to provide shortcuts to some resources
## during development. remove in production
##
## mind that plugins may also affect menu
##########################################
