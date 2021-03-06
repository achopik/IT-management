# flake8: noqa
from rest_framework.routers import DefaultRouter

from management.views import (
    DepartmentViewSet, EmployeeViewSet, GroupViewSet,
    LocationViewSet, OpportunityViewSet, PositionViewSet,
    ProjectViewSet, SkillViewSet, TeamViewSet, TechnologyViewSet,
    DomainOpportunityViewSet,
)


router = DefaultRouter()
router.register("department", DepartmentViewSet)
router.register("employee", EmployeeViewSet)
router.register("group", GroupViewSet)
router.register("location", LocationViewSet)
router.register("opportunity", OpportunityViewSet)
router.register("position", PositionViewSet)
router.register("project", ProjectViewSet)
router.register("skill", SkillViewSet)
router.register("team", TeamViewSet)
router.register("technology", TechnologyViewSet)

router.register("domain-statistics", DomainOpportunityViewSet, basename="domain-statistics")


urlpatterns = router.urls
