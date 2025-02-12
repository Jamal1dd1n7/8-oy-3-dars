from django.urls import path
from .views import *


urlpatterns = [
    # Book
    path('books/', IndexView.as_view()),
    path('books/<int:pk>', IndexView.as_view()),
    # --------------------------------------------------------------------------------------------------

    # Book Shop
    path('bookshops/', BookShopView.as_view()),
    path('bookshops/<int:pk>', BookShopView.as_view()),
]
