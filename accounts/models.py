from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.team_name}"

class EmployeeDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username= models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    emp_id = models.IntegerField(unique=True)
    # email= models.CharField(max_length=100)
    # password= models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='user_team')

    def __str__(self) -> str:
        return f"{self.user.username, self.emp_id, self.role}"
