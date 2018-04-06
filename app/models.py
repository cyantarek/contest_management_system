from django.db import models
from django.contrib.auth.models import User


class Contest(models.Model):
	name = models.CharField(max_length=100)
	contest_date = models.DateTimeField()

	def __str__(self):
		return self.name

class Member(models.Model):
	is_judge = models.BooleanField(default=False)
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	recovery_id = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)
	is_participant = models.BooleanField(default=False)
	user_id = models.CharField(max_length=8, default='')
	contest = models.ManyToManyField(Contest)
	point = models.FloatField(default=0)
	date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.first_name + self.last_name

class Question(models.Model):
	body = models.TextField()
	name = models.CharField(max_length=100)
	input = models.TextField()
	output = models.TextField()
	samples = models.TextField()
	point = models.IntegerField()
	correct_ans = models.TextField()
	judge = models.ForeignKey(Member, on_delete=models.CASCADE)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)

class Solution(models.Model):
	body = models.TextField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	participant = models.ForeignKey(Member, on_delete=models.CASCADE)
