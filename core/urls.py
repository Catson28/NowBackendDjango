from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include  # Importa a função include para incluir as rotas da aplicação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.authentication.urls')),
    path('',include('apps.users.urls')),
    path('api/services/', include('apps.service.urls')),
    path('api/categories/', include('apps.category.urls')),
    path('api/customers/', include('apps.customer.urls')),
    path('api/employee/', include('apps.employee.urls')),
    path('api/images/', include('apps.image.urls')),
    path('api/payment/', include('apps.payment.urls')),
    path('api/subcategories/', include('apps.subcategory.urls')),
    path('api/poli/', include('apps.polimorph.urls')),
    path('api/finance/', include('apps.finance.urls')),
    path('api/reports/', include('apps.reports.urls')),
    path('api/sales/', include('apps.sales.urls')),
    path('api/person/', include('apps.person.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)