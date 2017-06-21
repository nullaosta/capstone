"""DataPanino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from analytics.views import home
from rest_framework import routers
from accounts.api import UserViewSet
from analytics.api import EconomicSnapshotViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snapshots', EconomicSnapshotViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^$', home, name='home'),
    url(r'^detail/(?P<slug>\w+)/$', home, name='home'),  # URL parameter capturing using a kwarg

    # url(r'^templates/about', about, name='about'),
    # url(r'^templates/login', login, name='login'),
    # url(r'^templates/contact', contact, name='contact'),
    # url(r'^templates/user_views', user, name='user')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)