class AcademicoGlobalRouter(object):

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'academicoglobal':
            return 'ProyeccionSocial'
        return None

    """def db_for_write(self, model, **hints):
        if model._meta.app_label == 'liquidaciones':
            return 'academicoacademico'
        return None"""