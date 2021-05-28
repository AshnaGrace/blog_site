from django.urls import path

from blogapp import views

urlpatterns=[
    path('',views.fun,name="fun"),
    # path('updateb/',views.update,name='updateb'),
path('update/<int:id>',views.update,name='update'),
path('updateview/<int:pk>',views.TaskU.as_view(),name='updateview'),
path('detail/<int:pk>',views.TaskD.as_view(),name='detail'),
path('taskdelete/<int:pk>',views.Taskd.as_view(),name='taskdelete'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>',views.delete,name='delete')
    ]
