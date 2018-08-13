from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
	subject_name = models.CharField(max_length=50)
	paper_id = models.CharField(max_length=8)

	def __str__(self):
		return self.subject_name


class Teacher(models.Model):
	teacher_name = models.CharField(max_length=30)
	teacher_dept = models.CharField(max_length=20)

    def __str__(self):
		return self.teacher_name


class TeacherSubjectMapping(models.Model):
	teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.teacher_name}-{self.subject_name}"


class Section(models.Model):
	section_name = models.CharField(max_length=3)
	year = models.IntegerField(validators=[
		MaxValueValidator(4),
		MinValueValidator(1)
		])
	branch = models.CharField(max_length=20)
	shift = models.IntegerField(validators=[
		MaxValueValidator(2),
		MinValueValidator(1)
		])
	subjects = models.ManyToManyField(TeacherSubjectMapping)

	def __str__(self):
		return self.section_name