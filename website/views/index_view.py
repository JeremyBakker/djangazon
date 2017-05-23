from django.shortcuts import render
from website.models.order_model import Order

from website.models.product_model import Product

def index(request):
	try:
		order = Order.objects.get(user=request.user)
	except:
		order = 'fail'
	template_name = 'index.html'
	products = Product.objects.all().order_by('-id')[:20]
	product_dict_list = list()
	for product in products:
		product_dict = dict()
		product_dict["title"] = product.title
		product_dict["id"] = product.id
		product_dict_list.append(product_dict)
	print("product_dict", product_dict)
	return render(request, template_name, {'order':order, 'product_dict_list'\
		: product_dict_list})