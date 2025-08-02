from django.urls import path
from .views import SignupView, LoginView, ProductListCreateView, PlaceOrderView, OrderHistoryView,product_list_view, signup_view, login_view, order_history_view, logout_view

urlpatterns = [
    path('signup/', SignupView.as_view(),name='signup'),
    path('login/', LoginView.as_view(),name='login'),
    path('products/', ProductListCreateView.as_view(),name='product-list-create'),
    path('orders/place/', PlaceOrderView.as_view(),name='place-order'),
    path('orders/history/', OrderHistoryView.as_view(),name='order-history'),
    path('products/', product_list_view, name='product_list'),
   
   path('signupf/', signup_view, name='signup-page'),
   path('', login_view, name='login-page'),
   path('product/', product_list_view, name='product-list-page'),
   path('orders/history/', order_history_view, name='order-history-page'),
   path('logout', logout_view, name='logout-page'),

]