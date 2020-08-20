# Generated by Django 3.1 on 2020-08-17 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название тега')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
