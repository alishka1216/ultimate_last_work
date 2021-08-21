from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from webapp.views import (
    AnnouncementView,
    AnnouncementCreate,
    AnnouncementUpdate,
    AnnouncementDelete,
    AnnouncementList,
    Moderate
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnnouncementList.as_view(), name='announcement-list'),
    path('ad/<int:pk>/', AnnouncementView.as_view(), name='announcement-view'),
    path('ad/add/', AnnouncementCreate.as_view(), name='announcement-add'),
    path('ad/update/<int:pk>/', AnnouncementUpdate.as_view(), name='announcement-update'),
    path('ad/delete/<int:pk>/', AnnouncementDelete.as_view(), name='announcement-delete'),
    path('moderated/', Moderate.as_view(), name='moderate-list'),
    path('accounts/', include('accounts.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
