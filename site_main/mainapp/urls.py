from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.products, name='products'),
    path("product/new/", views.new_product, name='new_product'),
    path("product/<int:kp>/edit/", views.edit_product, name='edit_product'),
    path("product/<int:kp>/delete/", views.del_product, name='del_product'),
    path("recipes/", views.recipes, name='recipes'),
    path("recipe/new/", views.new_recipe, name='new_recipe'),
    path("recipe/<int:kr>/edit/", views.edit_recipe, name='edit_recipe'),
    path("recipe/<int:kr>/delete/", views.del_recipe, name='del_recipe'),
    path("product_types/", views.product_types, name='product_types'),
    path("product_type/new/", views.new_product_type, name='new_product_type'),
    path("product_type/<int:kt>/edit/", views.edit_product_type, name='edit_product_type'),
    path("product_type/<int:kt>/delete/", views.del_product_type, name='del_product_type'),
    path("dishes/", views.dishes, name='dishes'),
    path("dish/new/", views.new_dish, name='new_dish'),
    path("dish/<int:dk>", views.dish, name='dish'),
    path("dish/<int:dk>/delete/", views.del_dish, name='del_dish'),
    path("dish/<int:dk>/edit/", views.edit_dish, name='edit_dish'),
    path("register/", views.register_user, name='register'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("", views.index, name="index"),
    path('aboutme/', views.about_me, name='about_me'),
]
