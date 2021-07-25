# from functools import partialmethod
from django.urls import path
from . import  views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('AllInternships',views.get_post),
    path('Internship/<int:id>', views.put_delete),
    path('UserProfile/<int:id>', views.user_profile1),
    # path('AllProfile', views.allProfile),
    path('AllProfile',views.AllProfile.as_view()),
    path('Education/<int:id>',views.education1),
    path('Experience/<int:id>',views.experience1),
    path("AllApplications", views.allApplication),
    path("Application/<int:id>", views.application1),
    path("AllExperiences",views.allExperience),
    path("AllEducations", views.allEducation),
    path("GetExperience/<int:userId>", views.getExperience),
    path("UploadImage", views.upload_img),

    path("userProfileFilter", views.userProfileFilter),
    path("UserGet/<int:mobile>", views.userMobile),
    path("AllUserInternships/<int:userId>", views.userInernships),
    # path('AllAppliedInternships', views.allAppliedInternships),
    path('InternshipFilter', views.internshipFilter),
    # all users for one internship
    path('InternshipUsers/<int:internship_id>', views.allUserForOneInternship),
    path("CareerObjective", views.career_objective),
    path("demo", views.DemoView.as_view()),

    

    # path('', views.check),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)