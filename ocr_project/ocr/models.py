from django.db import models


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    extracted_text = models.TextField(blank=True)
    processing_time = models.FloatField(null=True, blank=True)
    text_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"