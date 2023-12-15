from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=250)
    sinopsis = models.TextField()
    tags = models.CharField(max_length=350)
    time_duration = models.CharField(max_length=10)
    background_url = models.TextField()
    director = models.CharField(max_length=250)
    release_date = models.DateField()
    is_hd = models.BooleanField()
    is_tv_show = models.BooleanField()
    is_movie = models.BooleanField()
    # un contenido tiene muchos actors n <-> n
    actors = models.ManyToManyField("actor.Actor", blank=True)
    
    # -> str indica que la funcion retorna un string
    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "content"
