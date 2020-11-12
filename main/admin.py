from django.contrib import admin
from main.models import Post, Contact, WorkExperience, Certificate, Project

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'posted_date')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'workplace')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_date')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Project, ProjectAdmin)