# Generated by Django 3.1.4 on 2020-12-06 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=150)),
                ('picture', models.CharField(max_length=350)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_books.category')),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'book',
                'ordering': ['book_name'],
            },
        ),
    ]
