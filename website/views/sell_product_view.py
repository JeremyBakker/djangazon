from django.shortcuts import render
from website.forms import ProductForm
from website.models.product_model import Product

from datetime import datetime

def sell_product(request):
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        form_data = request.POST

        p = Product(
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            quantity = form_data['quantity'],
            product_category_id = form_data['product_category'],
            date_added = datetime.now(),
        )
        p.save()
        template_name = 'success/product_added_to_sell_links.html'
        return render(request, template_name, {'posted_object': 'Your Product added to Sell', 'posted_object_identifier': p.title})
