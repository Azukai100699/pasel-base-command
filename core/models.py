from django.db import models

class Sphere(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CountyHub(models.Model):
    STATUS_CHOICES = [
        ('inactive', 'OFFLINE / PENDING'),
        ('active', 'OPERATIONAL'),
        ('maintenance', 'SYSTEM MAINTENANCE'),
    ]
    sphere = models.ForeignKey(Sphere, on_delete=models.CASCADE)
    county_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inactive')
    coordinates = models.CharField(max_length=50, blank=True)

    @property
    def progress_percentage(self):
        projects = self.projects.all()
        if not projects: return 0
        total = sum(p.completion_rate for p in projects)
        return round(total / projects.count())

    def __str__(self):
        return self.county_name

class Project(models.Model):
    PROJECT_STATUS = [
        ('planned', 'PROPOSED'),
        ('active', 'IN PROGRESS'),
        ('completed', 'DEPLOYED'),
    ]
    hub = models.ForeignKey(CountyHub, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='planned')
    last_updated = models.DateTimeField(auto_now=True)

    @property
    def completion_rate(self):
        tasks = self.tasks.all()
        if not tasks: return 0
        completed = tasks.filter(is_completed=True).count()
        return round((completed / tasks.count()) * 100)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_gallery/')
    caption = models.CharField(max_length=200, blank=True)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

class SlideshowImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideshow/')
    order = models.IntegerField(default=0)

class Director(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    statement = models.TextField()
    photo = models.ImageField(upload_to='directors/', blank=True, null=True)