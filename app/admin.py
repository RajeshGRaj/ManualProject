from django.contrib import admin

from app.forms import FeedbackForm
from .models import *
# Register your models here.

class AdminTopics(admin.ModelAdmin):
    list_display = ("id","topic",)
admin.site.register(Topics, AdminTopics)

class AdminWhats(admin.ModelAdmin):
    list_display = ("id", "topic", "what",)
admin.site.register(Whats, AdminWhats)

class AdminWhens(admin.ModelAdmin):
    list_display = ("id", "topic", "when",)
admin.site.register(Whens, AdminWhens)

class AdminWhys(admin.ModelAdmin):
    list_display = ("id", "topic", "why",)
admin.site.register(Whys, AdminWhys)

class AdminHows(admin.ModelAdmin):
    list_display = ("id", "topic", "how",)
admin.site.register(Hows, AdminHows)

class AdminTypes(admin.ModelAdmin):
    list_display = ("id", "topic", "types",)
admin.site.register(Typses, AdminTypes)

class AdminFeedback(admin.ModelAdmin):
    list_display = ('id', 'name', 'feedback',)
admin.site.register(Feedback, AdminFeedback)
