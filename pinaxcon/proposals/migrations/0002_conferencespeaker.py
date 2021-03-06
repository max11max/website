# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_speakers', '0007_auto_20170810_1651'),
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceSpeaker',
            fields=[
                ('speakerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='symposion_speakers.SpeakerBase')),
                ('twitter_username', models.CharField(blank=True, help_text='Your Twitter account', max_length=15)),
                ('first_time', models.BooleanField(help_text='')),
                ('experience', models.TextField(blank=True, help_text="List any past speaking experience you have.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", verbose_name='Past speaking experience')),
                ('experience_html', models.TextField(blank=True)),
                ('travel_assistance', models.BooleanField(help_text='Check this field if you require travel assistance to get to North Bay Python in Petaluma, California.')),
                ('lodging_assistance', models.BooleanField(help_text='Check this field if you require lodging assistance in Petaluma, California during North Bay Python.')),
                ('home_city', models.CharField(blank=True, help_text='Which city (and state, and country) will you be traveling from to get to North Bay Python?', max_length=127)),
                ('minority_group', models.CharField(blank=True, help_text='If you are a member of one or more groups that are underrepresented in the tech industry, you may list these here. Your response is optional.', max_length=256, verbose_name='Diversity statement')),
                ('code_of_conduct', models.BooleanField(help_text="I have read and, in the event that my proposal is accepted, agree that I will comply with the <a href='/code-of-conduct'>Code of Conduct</a>.")),
            ],
            bases=('symposion_speakers.speakerbase',),
        ),
    ]
