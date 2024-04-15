from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('add/',views.add,name='add'),
  path('addValue/' , views.addValue, name="addValue"),
  path('deleteValue/<int:id>/' , views.delete , name='delete'),
  path('update/<int:id>/' , views.update , name="update"),
  path('update/updateValue/<int:id>/' , views.updateValue , name="updateValue")

]