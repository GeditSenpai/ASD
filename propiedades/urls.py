from django.urls import path
from . import views
app_name = 'propiedades'

urlpatterns = [
    path('',views.inmobiliaria, name='inmobiliaria'),
    path('departamentos',views.depa, name='depa'),
 	path('nuevacasa',views.nuevacasa, name='nuevacasa'),
 	path('nuevodepa',views.nuevodepa, name='nuevodepa'),
 	path('editarcasa/<int:item_id>/',views.editarcasa, name='editarcasa'),
 	path('editardepa/<int:item_id>/',views.editardepa, name='editardepa'),
  	path('eliminarcasa/<int:item_id>/',views.eliminarcasa, name='eliminarcasa'),
  	path('eliminardepa/<int:item_id>/',views.eliminardepa, name='eliminardepa'),

]
