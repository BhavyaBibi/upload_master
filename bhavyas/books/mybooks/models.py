from django.db import models
class books(models.Model):

    cover=models.ImageField(upload_to='books/cover/',null=True,blank=True)
    title=models.CharField(max_length=128)
    author=models.CharField(max_length=128)
    pdf=models.FileField(upload_to='books/pdf')