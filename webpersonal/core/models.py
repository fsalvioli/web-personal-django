from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    descripcion=models.TextField()
    #image=models.ImageField(upload_to='project/')
    link=models.URLField(blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_created_at(self):
        return self.create_at.strftime("%d/%m/%Y")  # Formatea la fecha como desees

    get_created_at.short_description = 'Fecha de Creación'