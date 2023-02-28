from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from student.views import user_login

admin.site.site_header = 'AUNI Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('i18n/', include('django.conf.urls.i18n')),

]


urlpatterns += i18n_patterns(
    path('', include('library.urls')),
)
