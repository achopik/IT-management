from rest_framework import mixins, viewsets

from management.models import (
    Department, Employee, Group, Location, Opportunity,
    Position, Project, Skill, Team, Technology
)
from management.serializers import (
    DepartmentReadOnlySerializer, DepartmentSerializer,
    EmployeeReadOnlySerializer, EmployeeSerializer,
    GroupReadOnlySerializer, GroupSerializer,
    LocationSerializer, OpportunityReadOnlySerializer,
    OpportunitySerializer, PositionReadOnlySerializer,
    PositionSerializer, ProjectReadOnlySerializer,
    ProjectSerializer, SkillReadOnlySerializer,
    SkillSerializer, TeamReadOnlySerializer,
    TeamSerializer, TechnologySerializer
)


# Classes that should be inherited


class CreateRetrieveUpdateViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    pass


# Custom classes


class LocationViewSet(CreateRetrieveUpdateViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TechnologyViewSet(CreateRetrieveUpdateViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class SkillViewSet(CreateRetrieveUpdateViewSet):
    queryset = Skill.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return SkillReadOnlySerializer
        return SkillSerializer


class GroupViewSet(CreateRetrieveUpdateViewSet):
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return GroupReadOnlySerializer
        return GroupSerializer


class TeamViewSet(CreateRetrieveUpdateViewSet):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return TeamReadOnlySerializer
        return TeamSerializer


class DepartmentViewSet(CreateRetrieveUpdateViewSet):
    queryset = Department.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return DepartmentReadOnlySerializer
        return DepartmentSerializer


class PositionViewSet(CreateRetrieveUpdateViewSet):
    queryset = Position.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return PositionReadOnlySerializer
        return PositionSerializer


class EmployeeViewSet(CreateRetrieveUpdateViewSet, mixins.ListModelMixin):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return EmployeeReadOnlySerializer
        return EmployeeSerializer


class ProjectViewSet(CreateRetrieveUpdateViewSet, mixins.ListModelMixin):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return ProjectReadOnlySerializer
        return ProjectSerializer


class OpportunityViewSet(CreateRetrieveUpdateViewSet, mixins.ListModelMixin):
    queryset = Opportunity.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return OpportunityReadOnlySerializer
        return OpportunitySerializer
