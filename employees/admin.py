from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("username", "email",)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role', 'skype_id', 'avatar')}),
        ('Personal score', {'fields': ('last_month_score', 'current_month_score', 'level', 'total_score')}),
        ('Permissions', {'fields': ('groups',
                                    'user_permissions',
                                    'is_superuser',
                                    'is_staff',
                                    'is_active',)}),
        ('History', {'fields': ('date_joined', 'last_login')})
    )
admin.site.register(Employee, EmployeeAdmin)