# Generated by Django 4.2.2 on 2023-06-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_remove_recipes_categoryid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='RecipeID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
