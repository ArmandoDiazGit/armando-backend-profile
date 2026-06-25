from django.core.management.base import BaseCommand
from api.models import PersonalInfo, Bio, Skill, TimelineItem, CodeQuote, Project


class Command(BaseCommand):
    help = "Seeds the database with profile data matching the frontend Data.js"

    def handle(self, *args, **options):
        self._seed_personal_info()
        self._seed_bio()
        self._seed_skills()
        self._seed_timeline()
        self._seed_code_quote()
        self._seed_projects()
        self.stdout.write(self.style.SUCCESS("All data seeded successfully."))

    def _seed_personal_info(self):
        if PersonalInfo.objects.exists():
            self.stdout.write("  PersonalInfo already exists, skipping.")
            return
        PersonalInfo.objects.create(
            name="Armando Diaz",
            title="Software Engineer",
            specialty="TypeScript | Scalable Web Applications",
            taglines=[
                "I build scalable, user-friendly web interfaces with TypeScript.",
                "I craft performant and accessible web applications.",
                "I turn complex problems into simple, elegant solutions.",
            ],
            email="amandomcmlxxxix@gmail.com",
            github="https://github.com/ArmandoDiazGit",
            linkedin="https://www.linkedin.com/in/armando-diaz-750041204/",
        )
        self.stdout.write("  PersonalInfo created.")

    def _seed_bio(self):
        if Bio.objects.exists():
            self.stdout.write("  Bio already exists, skipping.")
            return
        Bio.objects.create(
            paragraphs=[
                "Hi, I'm Armando Diaz — a Software Engineer specializing in TypeScript and building modern web applications. I enjoy creating scalable, responsive, and user-focused experiences that solve real problems and feel seamless to use.",
                "My background includes working with TypeScript, Angular, React, RxJS, NgRx, REST APIs, HTML5, and CSS3. I've contributed to everything from enterprise dashboards to interactive tools, with a strong focus on clean code, maintainability, and usability.",
                "I'm especially interested in building interfaces that are both functional and intuitive. For me, great engineering is about turning complex ideas into simple, effective, and well-designed solutions.",
                "Outside of coding, I enjoy learning new technologies, exploring modern development practices, and building side projects that continue to sharpen my skills.",
            ]
        )
        self.stdout.write("  Bio created.")

    def _seed_skills(self):
        if Skill.objects.exists():
            self.stdout.write("  Skills already exist, skipping.")
            return
        languages = [
            ("JavaScript", 80),
            ("TypeScript", 80),
            ("HTML5", 80),
            ("CSS3", 80),
            ("Python", 60),
        ]
        frameworks = [
            ("Angular", 80),
            ("React", 80),
            ("Angular Material", 80),
            ("RxJS", 80),
            ("NgRx", 80),
            ("FastAPI", 70),
        ]
        tools = [
            ("Git", 95),
            ("VS Code", 95),
            ("npm", 90),
            ("REST APIs", 95),
            ("GitHub", 95),
            ("Bitbucket", 90),
            ("AWS", 90),
            ("CI/CD", 90),
            ("Figma", 90),
        ]
        for name, level in languages:
            Skill.objects.create(name=name, level=level, category=Skill.LANGUAGES)
        for name, level in frameworks:
            Skill.objects.create(name=name, level=level, category=Skill.FRAMEWORKS)
        for name, level in tools:
            Skill.objects.create(name=name, level=level, category=Skill.TOOLS)
        self.stdout.write("  Skills created.")

    def _seed_timeline(self):
        if TimelineItem.objects.exists():
            self.stdout.write("  TimelineItem already exists, skipping.")
            return
        items = [
            ("2020", "Started Coding", "Began my journey with web development, learning HTML, CSS, and JavaScript.", 0),
            ("2021 - Current", "Started Freelance Career", "Started building websites for small businesses as a freelance developer.", 1),
            ("2022", "First Internship", "Landed my first internship as a developer, building enterprise dashboards with Angular and TypeScript.", 2),
            ("2023", "Full Developer", "Transitioned from intern to a full-time developer, taking on more complex projects and responsibilities.", 3),
            ("2024 - 2025", "Software Engineer", "Promoted to Software Engineer, building scalable applications with modern tech stacks.", 4),
        ]
        for year, title, description, order in items:
            TimelineItem.objects.create(year=year, title=title, description=description, order=order)
        self.stdout.write("  TimelineItem created.")

    def _seed_code_quote(self):
        if CodeQuote.objects.exists():
            self.stdout.write("  CodeQuote already exists, skipping.")
            return
        CodeQuote.objects.create(
            code="""const build = {
  philosophy: "simple > complex",
  focus: ["clean", "maintainable", "scalable"],
  mindset: "elegant solutions"
};"""
        )
        self.stdout.write("  CodeQuote created.")

    def _seed_projects(self):
        if Project.objects.exists():
            self.stdout.write("  Project already exists, skipping.")
            return
        projects = [
            {
                "title": "My Angular Todo App",
                "description": "A lightweight todo application that lets users add, edit, complete, and delete tasks through a clean and responsive interface, helping users stay organized and productive.",
                "tech": ["Angular", "TypeScript", "Angular Material"],
                "code_url": "https://github.com/ArmandoDiazGit/My-angular-todo-list",
                "live_url": "https://armandodiazgit.github.io/My-angular-todo-list/",
                "preview_url": None,
            },
            {
                "title": "Precision Auto Works app",
                "description": "A modern, responsive landing page for an auto repair service shop. Built as a front-end demo to showcase a clean, professional brand presence for an automotive repair business.",
                "tech": ["React", "JavaScript", "CSS3", "REST APIs"],
                "code_url": "https://github.com/ArmandoDiazGit/Precision-Auto-works-app",
                "live_url": "https://precision-auto-works-app.vercel.app/",
                "preview_url": "https://res.cloudinary.com/dmccknd2i/video/upload/v1780539975/Screen_Recording_2026-06-03_at_10.23.44_PM_jet7z0.mov",
            },
            {
                "title": "Movie Database App",
                "description": "Comprehensive movie search and discovery platform with detailed information, ratings, and watchlist features.",
                "tech": ["React", "JavaScript", "RxJS", "REST APIs"],
                "code_url": "https://github.com/ArmandoDiazGit/ReactMovieApp",
                "live_url": None,
                "preview_url": "https://res.cloudinary.com/dmccknd2i/video/upload/v1775440711/Screen_Recording_2026-04-05_at_9.44.33_PM_ynloy3.mov",
            },
            {
                "title": "Weather App",
                "description": "Real-time weather application with location-based forecasts, interactive maps, and detailed meteorological data.",
                "tech": ["Angular", "JavaScript", "CSS3", "Weather API"],
                "code_url": "https://github.com/placeholder/weather-app",
                "live_url": "https://weather-app-five-mocha-21.vercel.app",
                "preview_url": "https://res.cloudinary.com/dmccknd2i/video/upload/v1775369451/Screen_Recording_2026-04-05_at_2.07.08_AM_szer9m.mov",
            },
            {
                "title": "My-Spa-Website",
                "description": "Elegant single-page application for a spa business with booking system, service showcase, and customer testimonials.",
                "tech": ["React", "JavaScript", "Talwind CSS", "CSS3"],
                "code_url": "https://github.com/ArmandoDiazGit/My-spa-website",
                "live_url": "https://my-spa-website-pi.vercel.app/",
                "preview_url": "https://res.cloudinary.com/dmccknd2i/video/upload/v1775441190/Screen_Recording_2026-04-05_at_10.04.09_PM_tgcl7l.mov",
            },
        ]
        for proj in projects:
            Project.objects.create(**proj)
        self.stdout.write("  Projects created.")
