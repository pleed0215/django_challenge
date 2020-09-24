from django.db import models
from core.models import CoreModel

class Person(CoreModel):

  """ Person Model """

  KIND_ACTOR = "actor"
  KIND_DIRECTOR = "director"
  KIND_WRITER = "writer"

  KIND_CHOICES = (
    (KIND_ACTOR, "Actor"),
    (KIND_DIRECTOR, "Director"),
    (KIND_WRITER, "Writer")
  )

  name = models.CharField(max_length=120)
  photo = models.ImageField(null=True, blank=True, upload_to="portraits")
  kind = models.CharField(max_length=15, choices=KIND_CHOICES)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "People"