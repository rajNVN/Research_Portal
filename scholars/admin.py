from django.contrib import admin

# Register your models here.
from scholars.models import SCHOLAR, PAPER, MASTERS, COUNSEL, RESULT, REGISTER  # , Profile

admin.site.register(SCHOLAR)
admin.site.register(PAPER)
admin.site.register(COUNSEL)
admin.site.register(MASTERS)
admin.site.register(RESULT)
#admin.site.register(Profile)
admin.site.register(REGISTER)