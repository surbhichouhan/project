import re
from django.db.models.query_utils import PathInfo
from .models import Internship
from django.shortcuts import render
from .models import  UserProfile, Experience, Education, Application ,UploadImage  #to be added
from django.http import JsonResponse , HttpResponse
from .serializers import *
from . serializers import UserProfileSerializer, ExperienceSerializer, EducationSerializer, ApplicationSerializer, UploadImageSerializer  #to be added
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from Internship import serializers

# from project.Internship import serializers

# from project.Internship import serializers


@csrf_exempt
def get_post(request):
    if request.method =='GET':
        interships = Internship.objects.all().order_by('postedDate')[::-1]
        serializer = InternshipSerializer(interships, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = InternshipSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status = 400)



@csrf_exempt
def put_delete(request, id):
    try:
        internship = Internship.objects.get(id=id)
        
        
    except:
        return HttpResponse(status =404)

    if request.method =='GET':
        serializer = InternshipSerializer(internship)
        return JsonResponse(serializer.data)
    if request.method =='PUT':
        
        data = JSONParser().parse(request)
        serializer = InternshipSerializer(internship, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method =='DELETE':
        internship.delete()
        return HttpResponse(status=204)


# to be added

# ======================= for user profile ===========================

# for put delete and get for particular
@csrf_exempt
def user_profile1(request,id):
    try:
        userProfile = UserProfile.objects.get(id=id)
        # experience = Experience.objects.get(id=userProfile.experience)
        # userProfile.experience = experience
        # userProfile.save()
        
        
    except:
        return HttpResponse(status =404)

    if request.method =='GET':
        serializer = UserProfileSerializer(userProfile)

        return JsonResponse(serializer.data)
    if request.method =='PUT':
        
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(userProfile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method =='DELETE':
        userProfile.delete()
        return HttpResponse(status=204)

# for get and post 
@csrf_exempt
# def allProfile(request):
#     if request.method =='GET':
#         allUsers = UserProfile.objects.all()
#         # print(allUsers)
#         serializer = UserProfileSerializer(allUsers, many=True)
#         # print(serializer)
#         return JsonResponse(serializer.data, safe=False)
#         # return HttpResponse(allUsers)
#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serializer = UserProfileSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data , status=201)
#         return JsonResponse(serializer.errors, status = 400)






# ============================== for application ==============================
# for put delete and get for particular
@csrf_exempt
def application1(request,id):
    try:
        application = Application.objects.get(id=id)

    except:
        return HttpResponse(status =404)

    if request.method =='GET':
        serializer = ApplicationSerializer(application)

        return JsonResponse(serializer.data)
    if request.method =='PUT':
        
        data = JSONParser().parse(request)
        serializer = ApplicationSerializer(application, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method =='DELETE':
        application.delete()
        return HttpResponse(status=204)

# for get and post 
@csrf_exempt
def allApplication(request):
    if request.method  =='GET':
        applications = Application.objects.all().order_by('applyDate')
        # print(allUsers)
        serializer = ApplicationSerializer(applications, many=True)
        # print(serializer)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = ApplicationSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status = 400)

# =============================for Experience==============================
# for put delete and get for particular
@csrf_exempt
def experience1(request,id):
    try:
        experience = Experience.objects.get(id=id)

    except:
        return HttpResponse(status =404)

    if request.method =='GET':
        serializer = ExperienceSerializer(experience)

        return JsonResponse(serializer.data)
    if request.method =='PUT':
        
        data = JSONParser().parse(request)
        serializer = ExperienceSerializer(experience, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method =='DELETE':
        experience.delete()
        return HttpResponse(status=204)

# for get and post 
@csrf_exempt
def allExperience(request):
    if request.method =='GET':
        experiences = Experience.objects.all()
        # print(allUsers)
        serializer = ExperienceSerializer(experiences, many=True)
        # print(serializer)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = ExperienceSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status = 400)


# =============================for Education==============================
# for put delete and get for particular
@csrf_exempt
def education1(request,id):
    try:
        education = Education.objects.get(id=id)

    except:
        return HttpResponse(status =404)

    if request.method =='GET':
        serializer = EducationSerializer(education)

        return JsonResponse(serializer.data)
    if request.method =='PUT':
        
        data = JSONParser().parse(request)
        serializer = EducationSerializer(education, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method =='DELETE':
        education.delete()
        return HttpResponse(status=204)

# for get and post 
@csrf_exempt
def allEducation(request):
    if request.method =='GET':
        educations = Education.objects.all()
        # print(allUsers)
        serializer = EducationSerializer(educations, many=True)
        # print(serializer)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = EducationSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status = 400)

def getExperience(request, userId):
    experiences = Experience.objects.filter(userProfile=userId)
    serializer = ExperienceSerializer(experiences, many=True)
    # print(experiences)
    return JsonResponse(serializer.data, safe=False)
# def check(request):
#     users = UserProfile.objects.all()

    # return render(request,'check.html', {'users':users})
# @csrf_exempt
# def upload_img(request, userId):
#     try:
#         userExist = UserProfile.objects.get(id = userId)  
#     except:
#         return HttpResponse(status = 404)
#     try:
#         user = UploadImage.objects.get(userId = userId)
#         # print(user)
#         if request.method == "DELETE":
#             user.delete()
#             # print("success inside")
#             return HttpResponse(status=204)
#         # print("success")
        
#         if request.method =='PUT':
#             data = JSONParser().parse(request)
#             serializer = UploadImageSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status =400)
    
        
#     except:

#         if request.method == 'POST':
#             # request = request.replace('\', ',')
#             data = JSONParser().parse(request)
#             userId = data['userId']
#             serializer = UploadImageSerializer(data = data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data , status=201)
#             return JsonResponse(serializer.errors, status = 400)

    
    

@csrf_exempt
def upload_img(request):
    data = JSONParser().parse(request)
    # print(data)
    Id = data['userId']
    # print(userId)
    # print(UploadImage.objects.get(userId = Id))
    if request.method == 'POST':
        # request = request.replace('\', ',')
        serializer = UploadImageSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status = 400)

    try:
        user = UploadImage.objects.get(userId = Id)
        # print(user)
        
        
    except:
        return HttpResponse(status = 404)
    if request.method =='PUT':            
        serializer = UploadImageSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)
    if request.method == 'GET':
        serializer = UploadImageSerializer(user)
        return JsonResponse(serializer.data)
    if request.method == "DELETE":
        user.delete()
        # print("success inside")
        return HttpResponse(status=204)
        # print("success")
        # print(user)
    

def userProfileFilter(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        
        try:
            location =  data['location'].lower()
        except:
            location = ""
        try:
            skill = data['skill']
        except:
            skill =""
        try:
            page_no = data['page_no']
        except:
            page_no = 1

        users = UserProfile.objects.all()
        print(users)
        result_users = []
        if location and skill:
            for user in users:
                if location in user.address.lower():
                    # if skill.lower() in user.skills.lower():
                    #     result_users.append(user)

                    # if skills are more than one
                    user_skills = list(map(lambda s : s.lower().strip(), user.skills.split(',')))
                    print("user skills", user_skills)
                    are_skills = [sk.lower().strip() in user_skills for sk in skill.split(',')]
                    if all(are_skills):
                        result_users.append(user)


                    # are_skills = [sk in user.skills for sk in skill.split(' ')]

        elif location:
            for user in users:
                if location in user.address.lower():
                    result_users.append(user)
        elif skill:
            for user in users:
                # if skill.lower() in user.skills.lower():
                #     result_users.append(user)

                # if skills are more than one
                user_skills = list(map(lambda s : s.lower().strip(), user.skills.split(',')))
                print("user skills", user_skills)
                are_skills = [sk.lower().strip() in user_skills for sk in skill.split(',')]
                if all(are_skills):
                    result_users.append(user)
        start = (page_no-1) *20 
        end = (page_no *20) +1
        # print("result uses", result_users)
        # final_list_ids = [user.id for user in result_users[start:end]]
        # print("final lits of ids", final_list_ids)
        # final_list = UserProfile.objects.filter(id__in = final_list_ids)
        # print("final list ", final_list)
        final_list = result_users[start:end]

        serializer = UserProfileSerializer(final_list, many=True)
        return JsonResponse(serializer.data, safe=False)

def userMobile(request, mobile):
    try:
        user = UserProfile.objects.get(phone_no=mobile)
    except:
        return HttpResponse(status =404)
    if request.method =='GET'    :
        serializer = UserProfileSerializer(user)
        return JsonResponse(serializer.data)

def userInernships(request, userId):
    
    
    if request.method =='GET':
        applications = Application.objects.filter(userProfile=userId).order_by("applyDate")[::-1]
        # serializer = ApplicationSerializer(applications)
        allUserInternships =[]
        dates = []
        for application in applications:
            dates.append(application.applyDate)
            internship = Internship.objects.get(id = application.internship.id)
            allUserInternships.append(internship)
        print("internships : ", allUserInternships)
        print("dates : ",dates)
        serializer = InternshipSerializer(allUserInternships,many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status = 404)

def internshipFilter(request):
    if request.method =='GET':
        print("wElcome")
        data = JSONParser().parse(request)
        try:
            location =  data['location'].lower().strip()
        except:
            location = ""
        try:
            skill = data['skill']
        except:
            skill =""
        try:
            duration = data['duration']
        except:
            duration = 0
        allInterships =[]
        # internships  = Internship.objects.all()
        if location and skill and duration:
            internships  = Internship.objects.filter(time_duration = duration)
            for internship in internships:
                if location.lower() == internship.location.lower():
                    intern_skills = list(map(lambda s : s.lower().strip(), internship.skills.split(',')))
                    print("internSkill", intern_skills)
                    are_skills = [sk.lower().strip() in intern_skills for sk in skill.split(',')]
                    print("are Skills ",are_skills)
                    if all(are_skills):
                        allInterships.append(internship)
        elif location and duration: 
            internships  = Internship.objects.filter(time_duration = duration) 
            for internship in internships:
                if location.lower() == internship.location.lower():
                    allInterships.append(internship)
        elif location and skill:
            internships = Internship.objects.all()
            for internship in internships:
                if location.lower() == internship.location.lower():
                    intern_skills = list(map(lambda s : s.lower().strip(), internship.skills.split(',')))
                    print("internSkill", intern_skills)
                    are_skills = [sk.lower().strip() in intern_skills for sk in skill.split(',')]
                    print("are skill", are_skills)
                    if all(are_skills):
                        allInterships.append(internship)
        elif skill and duration:
            internships  = Internship.objects.filter(time_duration = duration) 
            for internship in internships:
                intern_skills = list(map(lambda s : s.lower().strip(), internship.skills.split(',')))
                print("internSkill", intern_skills)
                are_skills = [sk.lower().strip() in intern_skills for sk in skill.split(',')]
                print("are skill", are_skills)
                if all(are_skills):
                    allInterships.append(internship)
        elif duration:
            internships  = Internship.objects.filter(time_duration = duration) 
            allInterships = internships
            # =================
            # internships = Internship.objects.all()
            # for internship in internships:
            #     if internship.time_duration == duration:
            #         allInterships.append(internship)
        elif location:
            internships = Internship.objects.all()
            for internship in internships:
                if location.lower() == internship.location.lower():
                    allInterships.append(internship)
        else:
            internships = Internship.objects.all()
            for internship in internships:
                intern_skills = list(map(lambda s : s.lower().strip(), internship.skills.split(',')))
                print("internSkill", intern_skills)
                are_skills = [sk.lower().strip() in intern_skills for sk in skill.split(',')]
                print("are Skill", are_skills)
                if all(are_skills):
                    allInterships.append(internship)
        # if want to filter here
        # allInterships.sort(key=lambda internship: internship.date, reverse=True)


        serializer = InternshipSerializer(allInterships, many=True)
        return JsonResponse(serializer.data, safe=False)

def allAppliedInternships(request):
    if request.method =="GET":
        applications = Application.objects.all().order_by('applyDate')[::-1]
        allAppliedInternshipsList = []
        dates = []
        for application in applications:
            dates.append(application.applyDate)
            # print("appication",application)
            # print("date: ",application.applyDate)
            # print("user : ",application.userProfile)
            # print("application internship = ", application.internship.id)
        
            internship = Internship.objects.get(id=application.internship.id)
            allAppliedInternshipsList.append(internship)
        
        print("all internships :",allAppliedInternshipsList)
        print("all Dates :", dates)
        # return HttpResponse("done")
        serializer = InternshipSerializer(allAppliedInternshipsList, many=True)
        

        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status = 404)

def allUserForOneInternship(request,internship_id):
    if request.method =="GET":
        applications = Application.objects.filter(internship = internship_id)
        print(applications)
        users = []
        if applications:
            for application in applications:
                user = UserProfile.objects.get(id = application.userProfile.id)
                users.append(user)
            print(users)
            serializer = UserProfileSerializer(users, many = True)
            return JsonResponse(serializer.data, safe=False)
        

    return HttpResponse(status= 404)

# 
def career_objective(request):
    data = JSONParser().parse(request)
    userId = data['id']
    candidate = UserProfile.objects.get(id=userId)
    if request.method == "POST":
        objective = data['career objective']
        # update content of career objective
        candidate.career_objective=objective
        candidate.save()
        serializer = UserProfileSerializer(candidate)
        return JsonResponse(serializer.data, status=200)

    if request.method =="DELETE":
        # delete content of career objective
        candidate.career_objective=""
        candidate.save()

def demo(request):
    if request.method =='GET':
        interships = Demo.objects.all()
        serializer = DemoSerializer(interships, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method =='POST':
        data = JSONParser().parse(request)
        serializer = DemoSerializer(data = data)
        print("line 73")
        if serializer.is_valid():
            serializer.save()
            print("line 76")
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status = 400)

class DemoView(APIView):
    def post(self,request):
        # data = JSONParser().parse(request)
        # parser_classes=(MultiPartParser)
        # parser_classes = (FileUploadParser,)
        serializer = DemoSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    def get(self,request):
        data=Demo.objects.all()
        serializer=DemoSerializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)    


class AllProfile(APIView):
    def post(self,request):
        # data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    def get(self,request):
        profiles=UserProfile.objects.all()
        serializer=UserProfileSerializer(profiles,many=True)
        return JsonResponse(serializer.data,safe=False)    
            

            



                    

            


    



    
    



        