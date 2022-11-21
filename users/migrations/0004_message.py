# Generated by Django 3.2.4 on 2022-11-21 03:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221116_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('email', models.EmailField(max_length=200, null=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
    ]
