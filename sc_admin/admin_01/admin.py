from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin
from django.contrib import admin


class ChecklistItemsAdmin(ModelAdmin):
    list_display = ('id', 'task', 'description', 'is_completed', 'name')
    list_filter = ['task', 'is_completed']
    search_fields = ['name', 'description']
    ordering = ['task', 'name']
    actions = ['make_not_completed']

    def make_not_completed(self, request, queryset):
        queryset.update(is_completed=False)

    make_not_completed.short_description = "Mark selected items as not completed"


class CollaborationMembersAdmin(ModelAdmin):
    list_display = ('id', 'user', 'collaboration', 'role')
    list_filter = ['collaboration']
    search_fields = ['user__username', 'collaboration__name']
    ordering = ['collaboration', 'user']
    actions = ['make_admin']

    def make_admin(self, request, queryset):
        queryset.update(role='admin')

    make_admin.short_description = "Make selected users admin of collaboration"


class CollaborationsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'admin', 'goal', 'description', 'is_public')
    list_filter = ['is_public']
    search_fields = ['name', 'description']
    ordering = ['name']
    actions = ['make_public']

    def make_public(self, request, queryset):
        queryset.update(is_public=True)

    make_public.short_description = "Make selected collaborations public"


class GoalMembersAdmin(ModelAdmin):
    list_display = ('id', 'user', 'goal', 'status', 'progress', 'start_date', 'end_date')
    list_filter = ['goal']
    search_fields = ['user__username', 'goal__name']
    ordering = ['goal', 'user']
    actions = ['make_not_started']

    def make_not_started(self, request, queryset):
        queryset.update(status='not_started')

    make_not_started.short_description = "Mark selected goals as not started"


class GoalTypesAdmin(ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'description', 'image_url')
    list_filter = ['name']
    search_fields = ['name', 'description']
    ordering = ['name']
    actions = ['make_default']

    def make_default(self, request, queryset):
        queryset.update(is_default=True)

    make_default.short_description = "Make selected types default"


class GoalsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'type', 'duration', 'is_public')
    list_filter = ['type', 'is_public']
    search_fields = ['name', 'description']
    ordering = ['type', 'name']
    actions = ['make_public']

    def make_public(self, request, queryset):
        queryset.update(is_public=True)

    make_public.short_description = "Make selected goals public"


class ProjectMembersAdmin(ModelAdmin):
    list_display = ('id', 'project', 'user', 'goal', 'status', 'progress', 'start_date', 'end_date', 'is_approved')
    list_filter = ['project']
    search_fields = ['user__username', 'project__name']
    ordering = ['project', 'user']
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        queryset.update(is_approved=True)

    make_approved.short_description = "Mark selected users as approved"


class ProjectsAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'goal', 'collab', 'start_date', 'end_date', 'status', 'progress', 'no_of_members_done')
    list_filter = ['goal']
    search_fields = ['name', 'description']
    ordering = ['goal', 'name']
    actions = ['make_in_progress']

    def make_in_progress(self, request, queryset):
        queryset.update(status='in_progress')

    make_in_progress.short_description = "Mark selected projects as in progress"


class ResourcesAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'collaboration', 'url', 'visible', 'uploader', 'type')
    list_filter = ['collaboration']
    search_fields = ['name', 'url']
    ordering = ['collaboration', 'name']
    actions = ['make_visible']

    def make_visible(self, request, queryset):
        queryset.update(visible=True)

    make_visible.short_description = "Make selected resources visible"


class TaskMembersAdmin(ModelAdmin):
    list_display = ('id', 'project', 'task', 'user', 'status', 'start_date', 'end_date', 'no_of_approvals', 'is_approved')
    list_filter = ['project']
    search_fields = ['user__username', 'project__name']
    ordering = ['project', 'user']
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        queryset.update(is_approved=True)

    make_approved.short_description = "Mark selected users as approved"


class TasksAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'goal', 'project', 'start_date', 'end_date', 'status')
    list_filter = ['goal']
    search_fields = ['name', 'description']
    ordering = ['goal', 'name']
    actions = ['make_in_progress']

    def make_in_progress(self, request, queryset):
        queryset.update(status='in_progress')

    make_in_progress.short_description = "Mark selected tasks as in progress"


class UserChecklistItemsAdmin(ModelAdmin):
    list_display = ('id', 'user', 'checklist_item', 'is_completed')
    list_filter = ['user']
    search_fields = ['user__username', 'checklist_item__name']
    ordering = ['user', 'checklist_item']
    actions = ['make_not_completed']

    def make_not_completed(self, request, queryset):
        queryset.update(is_completed=False)

    make_not_completed.short_description = "Mark selected items as not completed"


# class UsersAdmin(BaseUserAdmin):
#     list_display = ('id', 'email', 'first_name', 'last_name', 'username', 'password', 'skills', 'profile_picture')
#     list_filter = ['username']
#     search_fields = ['username', 'email']
#     ordering = ['username']
#     actions = ['make_admin']

#     def make_admin(self, request, queryset):
#         queryset.update(is_superuser=True)

#     make_admin.short_description = "Make selected users admin"


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User


admin.site.unregister(User)
@admin.register(User)

@admin.register(User)
class UsersAdmin(BaseUserAdmin, ModelAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name',  'bio', 'profile_picture', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    actions = ['make_admin']

    def make_admin(self, request, queryset):
        queryset.update(is_superuser=True)

    make_admin.short_description = "Make selected users admin"

    # Define the fields displayed in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_picture', 'skills')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define the fields for the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'bio', 'profile_picture', 'skills', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(Collaboration, CollaborationsAdmin)
admin.site.register(Goal, GoalsAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Task, TasksAdmin)
admin.site.register(ChecklistItem, ChecklistItemsAdmin)
admin.site.register(UserChecklistItem, UserChecklistItemsAdmin)
admin.site.register(Resource, ResourcesAdmin)
admin.site.register(GoalType,  GoalTypesAdmin)
admin.site.register(ProjectMember, ProjectMembersAdmin)
# admin.site.register(TaskMembers, TaskMembersAdmin)
admin.site.register(CollaborationMember, CollaborationMembersAdmin)


