from django.contrib import admin

from .models import EventUser
from .models import User
# Register your models here.

@admin.action(description="Сделать админом")
def make_user_superser(modeladmin, request, queryset):
    queryset.update(is_active=True, is_superuser=True, is_staff=True)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'surname', 'email', 'is_staff')
    list_filter = ['is_staff']
    search_fields = ["name", "username", "surname"]
    actions = [make_user_superser]
    
@admin.register(EventUser)
class EventUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'is_staff', 'username']
    
    def username(self, instance):
        try:
            user = User.objects.get(id=instance.user_id)
            return user.username
        except User.DoesNotExist:
            return '-'
