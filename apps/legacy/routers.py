

class LegacyRouter(object):
    """A router to control all database operations on models in
    the legacy application"""

    def db_for_read(self, model, **hints):
        "Point all operations on legacy models to 'legacy'"
        if model._meta.app_label == 'legacy':
            return 'legacy'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on legacy models to 'legacy'"
        if model._meta.app_label == 'legacy':
            return 'legacy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in legacy is involved"
        if obj1._meta.app_label == 'legacy' or obj2._meta.app_label == 'legacy':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the legacy app only appears on the 'legacy' db"
        if db == 'legacy':
            return model._meta.app_label == 'legacy'
        elif model._meta.app_label == 'legacy':
            return False
        return None