def get(self, request, *args, **kwargs):
        # Fetch the category; return 404 or redirect as needed
        self.category = self.get_category()[0]
        self.category1 =  self.get_category()[1]

        try:
            self.search_handler = self.get_search_handler(
                request.GET, request.get_full_path(), self.get_categories())
        except InvalidPage:
            messages.error(request, _('The given page number was invalid.'))
            return redirect(self.category.get_absolute_url())

        return super(BothCategoryView, self).get(request, *args, **kwargs)

    def get_category(self):
        if 'pk' in self.kwargs and 'pk1' in self.kwargs:
            # Usual way to reach a category page. We just look at the primary
            # key in case the slug changed. If it did, get() will redirect
            # appropriately
            filters = {'pk': self.kwargs['pk']}
            filters1 = {'pk1': self.kwargs['pk1']}
        else:
            # For SEO reasons, we allow chopping off bits of the URL. If that
            # happened, no primary key will be available.
            filters = {'slug': self.kwargs['category_slug']}
            filters1 = {'slug1': self.kwargs['category_slug1']}
           
        return get_object_or_404(Category, **filters) + get_object_or_404(Category, **filters1)

    def redirect_if_necessary(self, current_path, category):
        if self.enforce_paths:
            # Categories are fetched by primary key to allow slug changes.
            # If the slug has changed, issue a redirect.
            expected_path = category.get_absolute_url()
            if expected_path != urlquote(current_path):
                return HttpResponsePermanentRedirect(expected_path)

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    def get_categories(self):
        """
        Return a list of the current category and its ancestors
        """
        return self.category.get_descendants_and_self() + self.category1.get_descendants_and_self()

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category

        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        context.update(search_context)
        return context
