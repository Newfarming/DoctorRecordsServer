"""WXProgram URL Configuration
first-level interface(apps): amniocentesisAppoint, multidisciplinaryConsultation, addPatient
"""


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("DoctorRecordsServerApp/", include(("DoctorRecordsServerApp.urls", "DoctorRecordsServerApp"), namespace="DoctorRecordsServerApp")),
    path("mz_queue/", include(("QueuingrRegistrationApp.urls", "QueuingrRegistrationApp"), namespace="QueuingrRegistrationApp")),
]
