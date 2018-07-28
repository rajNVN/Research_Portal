from django.contrib import admin

# Register your models here.
from students.models import *

admin.site.register(STUDENT)
admin.site.register(LANGUAGE)
admin.site.register(K_LANGUAGES)
admin.site.register(P_STUDENT)
admin.site.register(R_STUDENT)
admin.site.register(INTEREST)
admin.site.register(SCORE)

