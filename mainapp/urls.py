from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='products'),
   path('catgory<int:pk>/', mainapp.products, name='category'),
   path('catgory<int:pk>/<int:page>/', mainapp.products, name='category_page'),
   path('product<int:pk>/', mainapp.product, name='product')

]

