from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("university", views.UniversityViewSet)
router.register("courses", views.CourseViewSet)
router.register("university-courses", views.UniversityCourseViewSet)

urlpatterns = router.urls