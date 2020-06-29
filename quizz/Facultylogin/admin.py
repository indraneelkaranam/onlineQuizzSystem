from django.contrib import admin
from .models import FacultyList
from .models import Subjects, CSE, ECE, EEE, APTITUDE, GK

admin.site.register(FacultyList)
admin.site.register(Subjects)
admin.site.register(CSE)
admin.site.register(ECE)
admin.site.register(EEE)
admin.site.register(APTITUDE)
admin.site.register(GK)
