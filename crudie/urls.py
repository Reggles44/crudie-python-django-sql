from crudie import views

urlpatterns = [
    path('create/', views.Create.as_view()),
    path('read/', views.Read.as_view()),
    path('update/', views.Update.as_view()),
    path('delete/', views.Delete.as_view()),
]
