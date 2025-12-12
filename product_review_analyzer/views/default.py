from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home', renderer='product_review_analyzer:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'product-review-analyzer'}
