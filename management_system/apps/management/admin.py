from django.contrib import admin

from management.models import (
    Department, Employee, Group,
    Location, Opportunity, Position,
    Project, Skill, Team, Technology
)

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Location)
admin.site.register(Opportunity)
admin.site.register(Position)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Team)
admin.site.register(Technology)
