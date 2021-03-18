# Generated by Django 3.1.7 on 2021-03-18 09:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0043_auto_20200717_1325'),
        ('places', '0033_auto_20190130_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('name_is_translatable', models.BooleanField(default=True)),
                ('icon', models.CharField(max_length=32)),
                ('status', models.CharField(choices=[('active', 'active'), ('archived', 'archived')], default='active', max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_types', to='groups.group')),
            ],
            options={
                'unique_together': {('group', 'name')},
            },
        ),
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.placetype'),
        ),
    ]
