# Generated by Django 4.1.4 on 2023-01-16 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=70)),
                ('slug', models.CharField(max_length=70)),
                ('views', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.expressions.Case, to='blog.blogcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
