from django.urls import path
from django .contrib.auth.decorators import login_required
from .views import InicioConvenio, crearC, reporteExcel, proyeccionReporte, editarC, CrearProyecto, verProyecto, Login,proyeccionInicio, index, editarProyecto
from Apps.usuarios.views import Login,logoutUsuario


urlpatterns = [

    path('', Login.as_view(), name = 'login'),
    path('logout', login_required(logoutUsuario),name = "Cerrar"),


    #Convenios
    path('Inicio', index.as_view(), name = 'inicio'),
    path('Inicio/Convenios',login_required(InicioConvenio.as_view()), name = 'inicioConvenio'),
    path('Convenio/Crearconvenio',login_required(crearC.as_view()), name = 'crearConvenio'),
    path('Convenio/ListaReporte', reporteExcel.as_view(), name = 'Reporte'),
    path('Convenio/Lista/Editar/<int:pk>', login_required(editarC.as_view()), name = 'editarConvenio'),
    

    #ProyeccionSocial
    path("Inicio/Proyectos",login_required(proyeccionInicio.as_view()), name="inicioProyeccion"),
    path('Proyeccion/Crear_proyecto',login_required(CrearProyecto.as_view()), name = "crearProyecto"),
    path('Proyeccion/Lista/Reporte',login_required(proyeccionReporte.as_view()), name = 'ReporteProyeccion'),
    path('Proyeccion/ver_proyecto/<int:pk>',login_required(verProyecto.as_view()), name = "verProyecto"),
    path("Proyeccion/ver_proyecto/editar/<int:pk>",login_required(editarProyecto.as_view()), name="editarProyecto")
    
] 
