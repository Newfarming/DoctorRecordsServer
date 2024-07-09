"""WXProgram URL Configuration for amniocentesisAppoint
second-level interface(functions): send_sms_code, submit_form
"""


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from .views import UserAdd, UserEdit, UserList, UserDelete, DepartAdd, DepartEdit, DepartDelete, DepartList, \
#     ActivityList, ActivityEdit, ActivityDelete, ActivityAdd, UserLogin, User_Info, UserDetails, DepartDetails, \
#     ActivityDetails, PermissionList
from .views import UserLogin, User_Info, MedInsAdd, MedInsList, MedInsEdit, MedInsDelete, MedInsDetails


urlpatterns = [
    # path("user/add", UserAdd.as_view(), name="user_add")
    # path("user/login", UserLogin.as_view(), name="UserLogin"),
    # path("user/info", User_Info.as_view(), name="UserInfo"),
    # path("user/list", UserList.as_view(), name="user_list"),
    # path("depart/list", DepartList.as_view(), name="UserInfo"),
    # path("user/add", UserAdd.as_view(), name="user_add"),
    # path("user/edit", UserEdit.as_view(), name="user_edit"),
    # path("user/list", UserList.as_view(), name="user_list"),
    # path("user/delete", UserDelete.as_view(), name="user_delete"),
    path("user/login", UserLogin.as_view(), name="UserLogin"),
    path("user/info", User_Info.as_view(), name="UserInfo"),
    # path("user/details", UserDetails.as_view(), name="UserDetails"),
    path("med_ins/add", MedInsAdd.as_view(), name="depart_add"),
    path("med_ins/edit", MedInsEdit.as_view(), name="depart_edit"),
    # path("depart/list", DepartList.as_view(), name="depart_list"),
    path("med_ins/delete", MedInsDelete.as_view(), name="depart_delete"),
    # path("depart/details", DepartDetails.as_view(), name="depart_details"),
    # path('saveimage/', UploadImg.as_view(), name="save_image"),
    # path('home', HomePage.as_view(), name="save_image"),
    # path('upload/', UpLoadInfo.as_view(), name="depart_details"),
] + static(settings.MEDIA_URL, document_root=(settings.DOCTOR_RECORDS_SERVER_APP_MEDIA_ROOT+'/'))
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)