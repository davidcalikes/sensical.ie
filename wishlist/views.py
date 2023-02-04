from django.shortcuts import render

from .models import wishlist
from products.models import Product
from django.contrib.auth.models import User


class wishlistView(TemplateView):

    template_name = 'wishlist.html'

    def post(self, request, pk):
        product = self.request.POST.get('name')
        current_user = request.user
        product_wish = wishlist(userid_id=current_user.id, product_id=product)
        book.save()
        return
