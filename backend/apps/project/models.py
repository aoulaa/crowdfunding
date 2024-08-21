from datetime import timedelta
from django.db import models
from django.utils import timezone

from core.models import BaseModel
from users.models import User

choice = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('returned', 'Returned')
)

class Category(BaseModel):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Categories"


class Tag(BaseModel):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Tags"

def default_end_date():
    return timezone.now() + timedelta(days=14)

class Project(BaseModel):
    title = models.CharField(max_length=50)
    details = models.TextField(max_length=2000)
    target = models.PositiveIntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=default_end_date)
    creation_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="projects")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="projects")
    

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Projects"

class ProjectImage(BaseModel):
    path = models.ImageField(upload_to='project', verbose_name='Image')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.path)

    class Meta:
        verbose_name_plural = "Project Images"


class ProjectVideo(BaseModel):
    path = models.FileField(upload_to='project', verbose_name='Video')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="videos")

    def __str__(self):
        return str(self.path)

    class Meta:
        verbose_name_plural = "Project Videos"


class Investment(BaseModel):
    amount = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name="investments")
    investor = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, related_name="investments")
    status = models.CharField(max_length=10, choices=choice, default='pending')

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = "Investments"

class Transaction(BaseModel):
    amount = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    investor = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = "Transactions"



class RewardsEarned(BaseModel):
    investor = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    investment = models.ForeignKey(Investment, on_delete=models.DO_NOTHING, default=None)
    amount = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = "Rewards Earned"
