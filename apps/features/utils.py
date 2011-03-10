from django.core.exceptions import ObjectDoesNotExist

from features.models import Feature, FeatureSet, SiteFeatureArea
from articles.models import Article

def get_features(area):
    # Get the right feature_set
    try:
        site_feature_area = SiteFeatureArea.site_objects.get(area=area)
        feature_set = FeatureSet.objects.get(site_feature_area=site_feature_area)
    except ObjectDoesNotExist:
        """
        We don't have a corresponding feature_area, or a
        feature_set, so we don't return any features
        """
        return [] # return nothing
    else:
        """
        With the right feature_set, try to build a list of features
        """
        feature_filter_kwargs = {
            'active': True,
            'feature_set': feature_set,}
        features = Feature.objects.filter(**feature_filter_kwargs).order_by("order")
        
        """
        We can't traverse the generic relation easily to further filter on
        content_object__is_published, so we need to do it now
        """
        try:
            # filter out the unpublished features
            return [feature for feature in features if feature.content_object.is_published == True]
        except AttributeError:
            """
            If we're here then somehow an unfeatureable object is being featured.
            Something is wrong :(
            """
            return [] # return nothing