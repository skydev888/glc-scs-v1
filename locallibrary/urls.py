from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('usersapp/', include('usersapp.urls')),  # 追加:ユーザー登録アプリ
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# # Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
#
#
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]
#
#
#
# # Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
