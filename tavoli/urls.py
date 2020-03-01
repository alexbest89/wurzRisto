from django.urls import path
from . import views

urlpatterns = [
    path('', views.TavoliListView.as_view(), name='tavolii'),
    path('<int:pk>', views.Conto_Tavolo.specifica_tavolo, name='detailTav'),
    path('insert/<int:pk>/<int:tav>', views.Conto_Tavolo.insert, name='insertProdotto'),
    path('delete/<int:pk>/<int:tav>', views.Conto_Tavolo.delete, name='deleteProdotto'),
    path('deleteAll/<int:tav>', views.Conto_Tavolo.deleteAll, name='deleteAll'),
    path('scontrino/<int:tav>/<str:tipoPag>', views.Conto_Tavolo.scontrino, name='scontrinoo'),
    path('new', views.table_new, name='new_table'),
]
