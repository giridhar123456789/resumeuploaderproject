from django.db import models

STATE_CHOICE = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Island'),
    ('Andhra pradesh','Andhra pradesh'),
    ('Arunachal pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('telangana','telangana'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('West bengal','West bengal'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Jammu & kashmir','Jammu & kashmir'),
    ('karnataka','karnataka'),
    ('madhya pradesh','madhya pradesh'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
)
# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE ,max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)
