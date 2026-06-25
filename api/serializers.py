from rest_framework import serializers
from .models import PersonalInfo, Bio, Skill, TimelineItem, CodeQuote, Project


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ["name", "title", "specialty", "taglines", "email", "github", "linkedin"]


class BioSerializer(serializers.ModelSerializer):
    full = serializers.JSONField(source="paragraphs")

    class Meta:
        model = Bio
        fields = ["full"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "level"]


class TimelineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineItem
        fields = ["year", "title", "description"]


class CodeQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeQuote
        fields = ["code"]


class ProjectSerializer(serializers.ModelSerializer):
    codeUrl = serializers.URLField(source="code_url")
    liveUrl = serializers.URLField(source="live_url", allow_null=True)
    previewUrl = serializers.URLField(source="preview_url", allow_null=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "tech", "codeUrl", "liveUrl", "previewUrl"]


class ProfileSerializer(serializers.Serializer):
    personalInfo = PersonalInfoSerializer()
    bio = BioSerializer()
    skills = serializers.SerializerMethodField()
    timeline = TimelineItemSerializer(many=True)
    codeQuote = CodeQuoteSerializer()
    projects = ProjectSerializer(many=True)

    def get_skills(self, obj):
        return {
            "languages": SkillSerializer(Skill.objects.filter(category=Skill.LANGUAGES), many=True).data,
            "frameworks": SkillSerializer(Skill.objects.filter(category=Skill.FRAMEWORKS), many=True).data,
            "tools": SkillSerializer(Skill.objects.filter(category=Skill.TOOLS), many=True).data,
        }
