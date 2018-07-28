from django.contrib import admin

# Register your models here.
from guides.models import UNIVERSITY, GUIDE, BRANCH, GROUP, TOPIC, USERS, DATES

admin.site.register(GUIDE)
admin.site.register(UNIVERSITY)
admin.site.register(BRANCH)
admin.site.register(GROUP)
admin.site.register(TOPIC)
admin.site.register(USERS)
admin.site.register(DATES)
