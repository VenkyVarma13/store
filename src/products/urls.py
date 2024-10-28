from django.urls import path

app_name = 'products'

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        )

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

