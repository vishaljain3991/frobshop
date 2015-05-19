from oscar.apps.checkout.app import CheckoutApplication as BaseCheckoutApplication
from oscar.core.loading import get_class

class CheckoutApplication(BaseCheckoutApplication):
    payment_details_view = get_class('checkout.views', 'PaymentDetailsView')


application = CheckoutApplication()
