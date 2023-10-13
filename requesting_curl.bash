

# create product
$ curl -X POST http://127.0.0.1:8000/api/v1/products/create  -d price=2.00 -d name='Men Glass' -d description='Good for you and your family'

# delete product
$ curl -X DELETE http://127.0.0.1:8000/api/v1/products/delete/<product_id>/


# update product

