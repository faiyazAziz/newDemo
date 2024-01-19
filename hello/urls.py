from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hello import views


urlpatterns = [
    path('home',views.home),
    path('books',views.BooksView.as_view()),
]

# urlpatterns += format_suffix_patterns(urlpatterns)