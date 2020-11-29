from flask import jsonify, request

from main.app import app

from main.models.product import ProductModel
from main.schemas.product import ProductSchema


@app.route('/products', methods=['GET'])
def get_products():
    """ Get products information
        Query parameters:
            - page: the wanted page (default = 1)
            - items_per_page: number of items per page (default = 6)
    """
    page = int(request.args.get('page', 1))
    items_per_page = int(request.args.get('items_per_page', 6))
    products = ProductModel.query.paginate(page, items_per_page)

    return jsonify(total_items=len(products.items),
                   items=ProductSchema(many=True).dump(products.items)), 200
