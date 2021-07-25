from .models import Demo, Internship, UserProfile, Application, Experience, Education, UploadImage
from rest_framework import serializers


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        # fields = ['id','position','company_name', 'description', 'no_of_openings', 'start_date', 'stipend', 'location','time_duration', 'skills', 'required'] 
        fields = "__all__"




class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        # fields = ['id', 'user', 'internship', 'date']
        fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        # fields = ['id','type', 'profile', 'organization', 'start_date', 
        # 'end_date', 'location', 'description', 'currently_working']
        fields = "__all__"
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        # fields = ['id','institute_name', 'degree', 'start_year', 'end_year',
        #  'percentage', 'stream']
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    # experiences = serializers.RelatedField(many=True)
    # experience = serializers.RelatedField(many=True, read_only=True)
    # experience = ExperienceSerializer(many=True, read_only=True)
    

    class Meta:
        model = UserProfile 
        # fields = ['id','full_name', 'email', 'image','skills',
        # 'education', 'experience','phone_no', 'address']
        
        fields = "__all__"

    

# class UserProfileSerializer(serializers.ModelSerializer):
#     experience = ExperienceSerializer(many=True)

#     class Meta:
#         model = UserProfile 
#         fields = ['id','full_name', 'email', 'image','skills',
#         'education', 'experience','phone_no', 'address']

#     def create(self, validated_data):
#         experience_data = validated_data.pop('experience')
#         userProfile = UserProfile.objects.create(**validated_data)
#         for ex_data in experience_data:
#             Experience.objects.create(userProfile = userProfile, **ex_data)
#         return userProfile

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = "__all__"

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = "__all__"