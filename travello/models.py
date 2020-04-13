from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    # def __init__(self, na, de, pr, im, of, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.name = na
    #     self.desc = de
    #     self.price = pr
    #     self.img = im
    #     self.offer = of
