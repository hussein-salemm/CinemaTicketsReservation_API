from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 1
    path("django/jsonresponsenomodel/", views.no_rest_no_model),
    # 2
    path("django/jsonresponsefrommodel/", views.no_rest_from_model),
    # 3.1 GET POST from rest framework function base view @api_view
    path("rest/fbv/", views.FBV_List),
    # 3.2 GET PUT DELETE from rest framework function base view @api_view (send parameter int (pk))
    path("rest/fbv/<int:pk>", views.FBV_pk),
    # 4.1 GET Post from rest framework class based view APIView
    path("rest/cbv/", views.CBV_List.as_view()),
    # 4.2 GET PUT DELETE from rest framework class based view APIView (send parameter int (pk))
    path("rest/cbv/<int:pk>", views.CBV_pk.as_view()),
    # 5
    # 5.1 GET POST from rest framework class based view APIView Mixins
    path("rest/mixins/", views.mixins_list.as_view()),
    # 5.2 GET PUT DELETE from rest framework class based view Mixins (send parameter int (pk))
    path("rest/mixins/<int:pk>", views.mixins_pk.as_view()),
    
    
]
