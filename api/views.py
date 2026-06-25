from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import PersonalInfo, Bio, Skill, TimelineItem, CodeQuote, Project
from .serializers import ProfileSerializer


@api_view(["GET"])
def profile(request):
    personal_info = PersonalInfo.objects.first()
    bio = Bio.objects.first()
    code_quote = CodeQuote.objects.first()

    if not all([personal_info, bio, code_quote]):
        return Response(
            {"error": "Profile data has not been seeded yet. Run `python manage.py seed_data`."},
            status=status.HTTP_404_NOT_FOUND,
        )

    data = {
        "personalInfo": personal_info,
        "bio": bio,
        "skills": Skill.objects.all(),
        "timeline": TimelineItem.objects.all(),
        "codeQuote": code_quote,
        "projects": Project.objects.all(),
    }

    serializer = ProfileSerializer(data)
    return Response(serializer.data)
