class ProyectoRouter(object):
    router_app_labels = {'auth','contenttypes','sessions','admin'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return 'academicoacademico'
        return None
