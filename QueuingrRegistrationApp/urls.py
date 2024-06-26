"""WXProgram URL Configuration for amniocentesisAppoint
second-level interface(functions): send_sms_code, submit_form
"""


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import MzQueueView, HomePage


urlpatterns = [
    path("mz_queue/list", MzQueueView.as_view(), name="MzQueueView"),
    path('home', HomePage.as_view(), name="save_image"),
] + static(settings.MEDIA_URL, document_root=(settings.DOCTOR_RECORDS_SERVER_APP_MEDIA_ROOT+'/'))
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)