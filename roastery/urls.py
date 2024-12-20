from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("origin/<str:continent_name>/", views.origin_products,
         name="origin_products"),
    path("product/<int:product_id>/", views.product_detail,
         name="product_detail"),
    path("manage/", views.manage_products, name="manage_products"),
    path("create/", views.create_product, name="create_product"),
    path('products/', views.products_list, name='products'),
    path("update/<int:product_id>/", views.update_product,
         name="update_product"),
    path("delete-product/<int:product_id>/", views.delete_product,
         name="delete_product"),
    path("denied", views.custom_permission_denied_view, name="denied"),
]
