
class ObjectListFilterMiddleware(object):
    """
    Further filters the results of an object list
    depending on the GET values found, posted by the
    _object_list_filter.html template
    """
    def process_request(self, request):
        # ipdb.set_trace()
        pass