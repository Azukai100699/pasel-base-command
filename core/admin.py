from django.contrib import admin
from .models import Sphere, CountyHub, Project, Task, ProjectImage, Director, SlideshowImage

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'hub', 'status', 'completion_rate')
    inlines = [TaskInline, ProjectImageInline]

admin.site.register(Sphere)
admin.site.register(CountyHub)
admin.site.register(Director)
admin.site.register(SlideshowImage)