from django.db import models
from django.utils.text import slugify


class WriteUp(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField()
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    description = models.CharField()
    link = models.URLField()
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="images/projects/")


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
