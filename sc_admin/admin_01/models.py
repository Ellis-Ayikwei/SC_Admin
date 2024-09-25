from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class ChecklistItem(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    task = models.ForeignKey('Task', models.DO_NOTHING)
    description = models.CharField(max_length=255)
    is_completed = models.IntegerField()
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_items'

    def __str__(self):
        return f'ChecklistItem: {self.name}'


class CollaborationMember(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    collaboration = models.ForeignKey('Collaboration', models.DO_NOTHING)
    role = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'collaboration_members'

    def __str__(self):
        return f'CollaborationMember: {self.user} - {self.collaboration}'


class Collaboration(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    admin = models.ForeignKey('User', models.DO_NOTHING)
    goal = models.ForeignKey('Goal', models.DO_NOTHING)
    description = models.CharField(max_length=250, blank=True, null=True)
    is_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'collaborations'

    def __str__(self):
        return f'Collaboration: {self.name}'


class GoalMember(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    goal = models.ForeignKey('Goal', models.DO_NOTHING)
    status = models.CharField(max_length=7)
    progress = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal_members'

    def __str__(self):
        return f'GoalMember: {self.user} - {self.goal}'


class GoalType(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    image_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal_types'

    def __str__(self):
        return f'GoalType: {self.name}'


class Goal(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    duration = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    type = models.ForeignKey(GoalType, models.DO_NOTHING, db_column='type')

    class Meta:
        managed = False
        db_table = 'goals'

    def __str__(self):
        return f'Goal: {self.name}'


class ProjectMember(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    goal = models.ForeignKey(Goal, models.DO_NOTHING)
    status = models.CharField(max_length=7)
    progress = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_members'

    def __str__(self):
        return f'ProjectMember: {self.user} - {self.project}'


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    goal = models.ForeignKey(Goal, models.DO_NOTHING)
    collab = models.ForeignKey(Collaboration, models.DO_NOTHING)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=7)
    progress = models.IntegerField(blank=True, null=True)
    no_of_members_done = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'

    def __str__(self):
        return f'Project: {self.name}'


class Resource(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    collaboration = models.ForeignKey(Collaboration, models.DO_NOTHING)
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=250)
    visible = models.IntegerField()
    uploader = models.ForeignKey('User', models.DO_NOTHING, db_column='uploader')
    type = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'resources'

    def __str__(self):
        return f'Resource: {self.name}'


class TaskMembers(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    task = models.ForeignKey('Task', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    status = models.CharField(max_length=7)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    no_of_approvals = models.IntegerField(blank=True, null=True)
    is_approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_members'

    def __str__(self):
        return f'TaskMember: {self.user} - {self.task}'


class Task(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    goal = models.ForeignKey(Goal, models.DO_NOTHING)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tasks'

    def __str__(self):
        return f'Task: {self.name}'


class UserChecklistItem(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    checklist_item = models.ForeignKey(ChecklistItem, models.DO_NOTHING)
    is_completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_checklist_items'

    def __str__(self):
        return f'UserChecklistItem: {self.user} - {self.checklist_item}'


class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=60, default=uuid.uuid4, editable=False)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    skills = models.JSONField(blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
   

    class Meta(AbstractUser.Meta):
        managed = True
        db_table = 'users'
    
    def __str__(self):
        return f'User: {self.username} - {self.first_name} {self.last_name}'


