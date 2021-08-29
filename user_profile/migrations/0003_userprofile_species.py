# Generated by Django 3.2.6 on 2021-08-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Species',
            field=models.CharField(choices=[('whale', 'whale'), ('Basking', 'Basking'), ('Shortfin mako', 'Shortfin mako'), ('thresher', 'thresher'), ('Bull', 'Bull'), ('Tiger', 'Tiger'), ('White', 'White'), ('Oceanic Whitetip', 'Oceanic Whitetip'), ('Hammerhead', 'Hammerhead'), ('Nurse', 'Nurse'), ('Blacktip reef', 'Blacktip reef'), ('sand tiger', 'sand tiger'), ('Lemon', 'Lemon'), ('Brownbanded Bamboo', 'Brownbanded Bamboo'), ('Megamouth', 'Megamouth')], default='whale', max_length=30),
        ),
    ]