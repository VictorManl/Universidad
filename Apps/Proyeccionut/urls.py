from django.urls import path
from django .contrib.auth.decorators import login_required
from .views import DocenteBuscar, InicioConvenio, \
    crearC, reporteExcel, proyeccionReporte, editarC, CrearProyecto, verProyecto, \
    Login,proyeccionInicio, index, editarProyecto,docente,Reporte,crearEstudiante
from Apps.usuarios.views import Login,logoutUsuario


urlpatterns = [

    path('', Login.as_view(), name = 'login'),
    path('logout', login_required(logoutUsuario),name = "Cerrar"),

    #Reporte
    path('Inicio_Reporte',Reporte.as_view(),name = "ReporteGeneral"),

    #Convenios
    path('Inicio', index.as_view(), name = 'inicio'),
    path('Inicio/Convenios',login_required(InicioConvenio.as_view()), name = 'inicioConvenio'),
    path('Convenio/Crearconvenio',login_required(crearC.as_view()), name = 'crearConvenio'),
    path('Convenio/ListaReporte', reporteExcel.as_view(), name = 'Reporte'),
    path('Convenio/Lista/Editar/<int:pk>', login_required(editarC.as_view()), name = 'editarConvenio'),
    

    #ProyeccionSocial
    path('Inicio/Proyectos',login_required(proyeccionInicio.as_view()), name="inicioProyeccion"),
    path('Proyecto/agregar_docente/', DocenteBuscar, name="agregarDocente"),
    path('Proyecto/Crear_proyecto',login_required(CrearProyecto.as_view()), name = "crearProyecto"),
    path('Proyeccion/Lista/Reporte',login_required(proyeccionReporte.as_view()), name = 'ReporteProyeccion'),
    path('Proyeccion/ver_proyecto/<int:pk>',login_required(verProyecto.as_view()), name = "verProyecto"),
    path("Proyecto/editar/<int:pk>",editarProyecto.as_view(), name="editarProyecto"),

    #Estudiante
    path('Proyecto/ver_proyecto/agregar_estudiante',crearEstudiante.as_view(),name="crearEstudiante"),

]
