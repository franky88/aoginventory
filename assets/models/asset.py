from django.db import models
from .employee import Employee
from .basetime import BaseTime
from django.contrib.auth.models import User


class AssetType(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class AssetStatus(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Asset(models.Model):
    asset_id = models.CharField(max_length=12, blank=True)
    name = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    serial = models.CharField(max_length=100, unique=True, blank=True)
    descriptions = models.TextField(blank=True)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated', '-created')

    def __str__(self):
        return self.name
    

class AssetAsignmentStatus(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class AssetAsignment(BaseTime):
    assign_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assets = models.ForeignKey(Asset, on_delete=models.CASCADE)
    status = models.ForeignKey(AssetAsignmentStatus, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.assign_to.full_name