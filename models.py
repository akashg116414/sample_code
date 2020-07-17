from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    flag = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "categories"

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    flag = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "subcategory"

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    subcategory = models.ForeignKey("subcategory", on_delete=models.DO_NOTHING)
    flag = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "items"

class Rating(models.Model):
    rating = models.IntegerField()
    items = models.ForeignKey("Items", on_delete=models.DO_NOTHING)
    flag = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "subcategory"


