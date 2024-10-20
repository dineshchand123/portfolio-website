from django.db import models

# Create your models here.
#models vaneko tyo chij ho jasle database lai define gerxa
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date= models.DateField()

    # database ma jasle entry garyo tesko name dekhauna ko lagi
    def __str__(self):
        return self.name