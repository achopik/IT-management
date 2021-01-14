from management.models import (
    Department, Employee, Group,
    Location, Opportunity, Position,
    Project, Skill, Team, Technology,
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
    TeamSerializer, TechnologySerializer,
)
from management.services.statistics import (
    count_opportunities_by_priorities,
    get_all_department_stats,
    get_domain_opportunity_stats
)

from rest_framework import mixins, status, viewsets
from rest_framework.views import Response
from rest_framework.decorators import action


"""
Classes to be inherited 
"""


class CreateRetrieveUpdateViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    pass


class SerializerChooseMixin:
    """
    Mixin providing serializer choosing when it's needed,
    Override read_only_serializer and write_serializer class attributes
    """
    read_only_serializer = None
    write_serializer = None

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return self.read_only_serializer
        return self.write_serializer


"""
API endpoints
"""


class LocationViewSet(CreateRetrieveUpdateViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TechnologyViewSet(CreateRetrieveUpdateViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class SkillViewSet(SerializerChooseMixin, CreateRetrieveUpdateViewSet):
    queryset = Skill.objects.all()
    write_serializer = SkillSerializer
    read_only_serializer = SkillReadOnlySerializer


class GroupViewSet(SerializerChooseMixin, CreateRetrieveUpdateViewSet):
    queryset = Group.objects.all()
    write_serializer = GroupSerializer
    read_only_serializer = GroupReadOnlySerializer


class TeamViewSet(SerializerChooseMixin, CreateRetrieveUpdateViewSet):
    queryset = Team.objects.all()
    write_serializer = TeamSerializer
    read_only_serializer = TeamReadOnlySerializer


class DepartmentViewSet(SerializerChooseMixin, CreateRetrieveUpdateViewSet):
    queryset = Department.objects.all()
    write_serializer = DepartmentSerializer
    read_only_serializer = DepartmentReadOnlySerializer

    @action(detail=True)
    def statistics(self, request, pk=None):
        stats = get_all_department_stats(pk)
        return Response({
            **stats},
            status=status.HTTP_200_OK
        )


class PositionViewSet(SerializerChooseMixin, CreateRetrieveUpdateViewSet):
    queryset = Position.objects.all()
    write_serializer = PositionSerializer
    read_only_serializer = PositionReadOnlySerializer


class EmployeeViewSet(
    SerializerChooseMixin,
    mixins.ListModelMixin,
    CreateRetrieveUpdateViewSet
):
    queryset = Employee.objects.all()
    write_serializer = EmployeeSerializer
    read_only_serializer = EmployeeReadOnlySerializer


class ProjectViewSet(
    SerializerChooseMixin,
    mixins.ListModelMixin,
    CreateRetrieveUpdateViewSet
):
    queryset = Project.objects.all()
    write_serializer = ProjectSerializer
    read_only_serializer = ProjectReadOnlySerializer


class OpportunityViewSet(
    SerializerChooseMixin,
    mixins.ListModelMixin,
    CreateRetrieveUpdateViewSet
):
    queryset = Opportunity.objects.all()
    write_serializer = OpportunitySerializer
    read_only_serializer = OpportunityReadOnlySerializer

    @action(detail=False)
    def statistics(self, request):
        stats = count_opportunities_by_priorities()
        return Response({
            **stats},
            status=status.HTTP_200_OK
        )


"""
Statistics endpoints
"""


class DomainOpportunityViewSet(viewsets.GenericViewSet):

    lookup_url_kwarg = 'domain_name'

    def retrieve(self, request, *args, **kwargs):
        stats = get_domain_opportunity_stats(kwargs['domain_name'])
        return Response({
            'statistics': stats},
            status=status.HTTP_200_OK
        )
