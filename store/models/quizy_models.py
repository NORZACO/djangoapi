from django.db import models
from django.urls import reverse


# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=255)
    picture = models.ImageField(
        upload_to="quiz_pictures/",
        default="https://i.pinimg.com/originals/0d/cf/e6/0dcfe624b9b7285ac51d8ba5fd002d71.jpg",
    )
    answer = models.CharField(max_length=255)
    description = models.TextField(default="No description")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("quiz-detail", kwargs={"pk": self.pk})
    
    # not sure if this is needed
    def get_update_url(self):
        return reverse("quiz-update", kwargs={"pk": self.pk})
    
    # not sure if this is needed
    def get_delete_url(self):
        return reverse("quiz-delete", kwargs={"pk": self.pk})
    
