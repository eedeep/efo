

class ImagessRouter(object):
    """A router to control all database operations on models in
    the imagess application"""

    def db_for_read(self, model, **hints):
        "Point all operations on imagess models to 'imagess'"
        if model._meta.app_label == 'imagess':
            return 'legacy'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on imagess models to 'imagess'"
        if model._meta.app_label == 'imagess':
            return 'legacy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in imagess is involved"
        if obj1._meta.app_label == 'imagess' or obj2._meta.app_label == 'imagess':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the imagess app only appears on the 'imagess' db"
        if db == 'legacy':
            return model._meta.app_label == 'imagess'
        elif model._meta.app_label == 'imagess':
            return False
        return None