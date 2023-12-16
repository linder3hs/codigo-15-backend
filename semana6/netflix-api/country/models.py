from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    dial_code = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    emoji = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} {self.emoji}"

    class Meta:
        db_table = "country"
