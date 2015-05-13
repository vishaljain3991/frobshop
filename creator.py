from oscar.apps.catalogue.categories import create_from_breadcrumbs

categories = (
    'Marble > Ganesh',
    
)
for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)
