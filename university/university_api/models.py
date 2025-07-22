from django.db import models

class University(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100)
    duration_weeks = models.PositiveIntegerField()


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['university', 'course', 'semester'],
                                    name='unique_course_per_university_semester')
        ]


    def __str__(self):
        return f"{self.university.name} - {self.course.title} ({self.semester})"