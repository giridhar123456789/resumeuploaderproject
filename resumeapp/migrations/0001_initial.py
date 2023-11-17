# Generated by Django 4.2.7 on 2023-11-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Island'), ('Andhra pradesh', 'Andhra pradesh'), ('Arunachal pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('telangana', 'telangana'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('West bengal', 'West bengal'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Jammu & kashmir', 'Jammu & kashmir'), ('karnataka', 'karnataka'), ('madhya pradesh', 'madhya pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]