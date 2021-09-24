from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task, SubTask
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class CustomTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'last_update', 'is_complete', 'user', 'priority')


class CustomSubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'last_update', 'is_complete', 'task')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Task, CustomTaskAdmin)
admin.site.register(SubTask, CustomSubTaskAdmin)
