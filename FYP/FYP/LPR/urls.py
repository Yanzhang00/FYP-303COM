from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Important: The generic class-based detail view expects to be passed a parameter named pk. 
# If you're writing your own function view you can use whatever parameter name you like, 
# or indeed pass the information in an unnamed argument.

urlpatterns = [
    path('', views.index, name='index'),
    path('VehiclesIndex/', views.VehiclesIndex, name='VehiclesIndex'),
    path('analysis/', views.analysis, name='analysis'),
    path('recognition/', views.recognition, name='recognition'),
    path('vehicleExit/', views.vehicleExit, name='vehicleExit'),
    path('ownerEnter/', views.ownerEnter, name='ownerEnter'),
    path('visitorEnter/', views.visitorEnter, name='visitorEnter'),
    path('owners/', views.OwnerListView.as_view(), name='owners'),
    path('owner/<int:pk>', views.OwnerDetailView.as_view(), name='owner-detail'),
    path('owner/create/', views.OwnerCreate.as_view(), name='owner-create'),
    path('owner/<int:pk>/update/', views.OwnerUpdate.as_view(), name='owner-update'),
    path('owner/<int:pk>/delete', views.OwnerDelete.as_view(), name='owner-delete'),
    path('visitors/', views.VisitorListView.as_view(), name="visitors"),
    path('visitor/<int:pk>', views.VisitorDetailView.as_view(), name="visitor-detail"),
    path('visitor/create/', views.VisitorCreate.as_view(), name='visitor-create'),
    path('visitor/<int:pk>/update/', views.VisitorUpdate.as_view(), name='visitor-update'),
    path('visitor/<int:pk>/delete', views.VisitorDelete.as_view(), name='visitor-delete'),
    path('vehicles/', views.VehicleListView.as_view(), name="vehicles"),
    path('vehicle/<int:pk>', views.VehicleDetailView.as_view(), name="vehicle-detail"),
    path('vehicle/<int:pk>/create/', views.VehicleCreate.as_view(), name='vehicle-create'),
    path('vehicle/<int:pk>/update/', views.VehicleUpdate.as_view(), name='vehicle-update'),
    path('vehicle/<int:pk>/delete', views.VehicleDelete.as_view(), name='vehicle-delete'),
    path('recognitionEnterForm/', views.recognitionEnterForm, name="recognitionEnterForm"),
    path('recognitionExitForm/', views.recognitionExitForm, name="recognitionExitForm"),
]

# For static files like CSS, JS, image
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# For media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)