# Generated by Django 3.0 on 2022-01-12 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0003_auto_20220109_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=1000)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v0.Advertisement')),
            ],
        ),
    ]
