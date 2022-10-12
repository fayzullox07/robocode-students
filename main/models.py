from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField("Nomi", max_length=35)
    url = models.CharField("Manzil (URL)", max_length=25)
    img = models.ImageField(upload_to="product-imagae/")
    desc = models.CharField("Haqida", max_length=30)
    like = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Project_detail", kwargs={"pk": self.pk})


  