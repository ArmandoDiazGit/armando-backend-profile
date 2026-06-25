from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    taglines = models.JSONField(default=list)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()

    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.name


class Bio(models.Model):
    paragraphs = models.JSONField(default=list)

    class Meta:
        verbose_name_plural = "Bio"

    def __str__(self):
        return f"Bio ({len(self.paragraphs)} paragraphs)"


class Skill(models.Model):
    LANGUAGES = "languages"
    FRAMEWORKS = "frameworks"
    TOOLS = "tools"
    CATEGORY_CHOICES = [
        (LANGUAGES, "Languages"),
        (FRAMEWORKS, "Frameworks & Libraries"),
        (TOOLS, "Tools & Technologies"),
    ]

    name = models.CharField(max_length=100)
    level = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class TimelineItem(models.Model):
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.year} — {self.title}"


class CodeQuote(models.Model):
    code = models.TextField()

    class Meta:
        verbose_name_plural = "Code Quotes"

    def __str__(self):
        return self.code[:50]


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech = models.JSONField(default=list)
    code_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
