from django.contrib import admin
from .models import Contact, Courses, Trainer, Register, Payments, Attendance

# Register your models here.
admin.site.register(Contact)
admin.site.register(Courses)
admin.site.register(Trainer)
admin.site.register(Register)
admin.site.register(Payments)
admin.site.register(Attendance)
