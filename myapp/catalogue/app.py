from oscar.apps.catalogue.app import BaseCatalogueApplication as CoreBaseCatalogueApplication, ReviewsApplication
from oscar.core.loading import get_class
from django.conf.urls import url, include
class BaseCatalogueApplication(CoreBaseCatalogueApplication):
    cross_view = get_class('catalogue.views', 'BothCategoryView')
        
    def get_urls(self):
        urlpatterns = super(BaseCatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^$', self.catalogue_view.as_view(), name='index'),
            url(r'^(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/(?P<category_slug1>[\w-]+(/[\w-]+)*)_(?P<pk1>\d+)/$', self.cross_view.as_view()),
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                self.detail_view.as_view(), name='detail'),
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                self.category_view.as_view(), name='category'),
            # Fallback URL if a user chops of the last part of the URL
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)/$',
                self.category_view.as_view()),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range'),
            ]
        return self.post_process_urls(urlpatterns)
     


class CatalogueApplication(BaseCatalogueApplication, ReviewsApplication):
    """
    Composite class combining Products with Reviews
    """


application = CatalogueApplication()
