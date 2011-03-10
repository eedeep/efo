

class StagingRouter(object):
    """A router to control all database operations on models in
    the Staging application"""

    def db_for_read(self, model, **hints):
        "Point all operations on Staging models to 'Staging'"
        if model._meta.app_label == 'staging':
            return 'staging'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on Staging models to 'Staging'"
        if model._meta.app_label == 'staging':
            return 'staging'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in Staging is involved"
        if obj1._meta.app_label == 'staging' or obj2._meta.app_label == 'staging':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the Staging app only appears on the 'Staging' db"
        if db == 'staging':
            return model._meta.app_label == 'staging'
        elif model._meta.app_label == 'staging':
            return False
        return None