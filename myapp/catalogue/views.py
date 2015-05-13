from django.contrib import messages
from django.core.paginator import InvalidPage
from django.utils.http import urlquote
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_class, get_model
from oscar.apps.catalogue.signals import product_viewed
from oscar.apps.catalogue.views import ProductCategoryView
Product = get_model('catalogue', 'product')
Category = get_model('catalogue', 'category')
ProductCategory = get_model('catalogue', 'ProductCategory')


class BothCategoryView(TemplateView):
    template_name = 'catalogue/browse.html'
    context_object_name = "products"
    def get_products(self):
        if 'pk' in self.kwargs and 'pk1' in self.kwargs:
            self.first_categoryproduct = ProductCategory.objects.filter(category_id=self.kwargs['pk'])
            self.second_categoryproduct = ProductCategory.objects.filter(category_id=self.kwargs['pk1'])
            self.product_ids = set(firstproduct.product_id for firstproduct in self.first_categoryproduct)
            return [Product.objects.filter(id=item.product_id)[0] for item in self.second_categoryproduct if item.product_id in self.product_ids]
            
        
        self.id0=Category.objects.filter(slug=self.kwargs['category_slug'])[0].id
        self.id1=Category.objects.filter(slug=self.kwargs['category_slug1'])[0].id     
        self.first_categoryproduct = ProductCategory.objects.filter(category_id=self.id0)
        self.second_categoryproduct = ProductCategory.objects.filter(category_id=self.id1)
        self.product_ids = set(firstproduct.product_id for firstproduct in self.first_categoryproduct)
        return [Product.objects.filter(id=item.product_id)[0] for item in self.second_categoryproduct if item.product_id in self.product_ids]
            
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BothCategoryView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['products'] = self.get_products()
        return context

