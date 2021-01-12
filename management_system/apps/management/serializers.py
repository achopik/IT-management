from management.models import (
    Department, Employee, Group,
    Location, Opportunity, Position,
    PositionStatus, Project, Skill,
    Team, Technology,
)

from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_opportunity(value):
        print("In project serializer", value)
        if not value:
            raise serializers.ValidationError("Opportunity can't be blank")
        if (
            Position.objects.filter(
                opportunity=value, status=PositionStatus.ACTIVE
            ).exists()
        ):
            raise serializers.ValidationError("Not all positions are secured!")
        return value

    class Meta:
        model = Project
        fields = "__all__"


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


"""
Read-only serializers with nested relations
"""


class SkillReadOnlySerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(read_only=True)

    class Meta:
        model = Skill
        fields = "__all__"


class GroupReadOnlySerializer(serializers.ModelSerializer):
    lead = EmployeeSerializer(read_only=True)

    class Meta:
        model = Group
        fields = "__all__"


class TeamReadOnlySerializer(GroupReadOnlySerializer):
    utilization_target = TechnologySerializer(read_only=True)

    class Meta:
        model = Team
        fields = "__all__"


class EmployeeReadOnlySerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    main_technology = TechnologySerializer(read_only=True)
    technology_skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = "__all__"


class PositionReadOnlySerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    assignment = EmployeeSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    supervisor = EmployeeSerializer(read_only=True)

    class Meta:
        model = Position
        fields = "__all__"


class DepartmentReadOnlySerializer(serializers.ModelSerializer):
    resource_manager = EmployeeSerializer(read_only=True)
    head = EmployeeSerializer(read_only=True)

    class Meta:
        model = Department
        fields = "__all__"


class ProjectReadOnlySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    account_manager = EmployeeSerializer(read_only=True)
    project_manager = EmployeeSerializer(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class OpportunityReadOnlySerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    staffing_location = LocationSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Opportunity
        fields = "__all__"
