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
        qs = Product.browsable.base_queryset()
        
        if 'pk' in self.kwargs and 'pk1' in self.kwargs:
            self.first_category = Category.objects.filter(id=self.kwargs['pk'])[0]
            self.second_category = Category.objects.filter(id=self.kwargs['pk1'])[0]
            self.first_categoryproduct = qs.filter(categories__in=[self.first_category,])
            self.second_categoryproduct = qs.filter(categories__in=[self.second_category,])
            return list(set(self.first_categoryproduct) & set(self.second_categoryproduct))
           
            
        
        self.first_category = Category.objects.filter(slug=self.kwargs['category_slug'])[0]
        self.second_category = Category.objects.filter(slug=self.kwargs['category_slug1'])[0]
        self.first_categoryproduct = qs.filter(categories__in=[self.first_category,]).distinct()
        self.second_categoryproduct = qs.filter(categories__in=[self.second_category,]).distinct()
        return list(set(self.first_categoryproduct) & set(self.second_categoryproduct))
            
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BothCategoryView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['products'] = self.get_products()
        return context

