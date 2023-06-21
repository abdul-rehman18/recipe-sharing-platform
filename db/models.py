from django.db import models


class Recipes(models.Model):
    RecipeID = models.AutoField(primary_key=True)
    RecipeName = models.CharField(max_length=255)
    Ingredients = models.TextField()
    PreparationSteps = models.TextField()
    DietaryInformation = models.CharField(max_length=255)
    CategoryID = models.IntegerField()

    def __str__(self):
        return self.RecipeName
    class Meta:
        db_table = 'Recipes' 


class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.CategoryName
    
    class Meta:
        db_table = 'Category'

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)


    def __str__(self):
        return self.Username
    class Meta:
        db_table = 'Users'
