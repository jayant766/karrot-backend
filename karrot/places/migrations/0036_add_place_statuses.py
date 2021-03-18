# Generated by Django 3.1.7 on 2021-03-18 10:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0043_auto_20200717_1325'),
        ('places', '0035_add_standard_place_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('name_is_translatable', models.BooleanField(default=True)),
                ('colour', models.CharField(max_length=6)),
                ('has_activities', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('inactive', 'inactive'), ('active', 'active'), ('archived', 'archived')], default='active', max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_statuses', to='groups.group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='place',
            name='status_next',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.placestatus'),
        ),
    ]
