from django.db import models
from django.urls import reverse


# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="articles"
    )
    tags = models.ManyToManyField("TagArticle", blank=True, related_name="tags")
    husband = models.OneToOneField(
        "Husband", on_delete=models.SET_NULL, null=True, blank=True, related_name="wife"
    )

    objects = models.Manager()
    published = PublishManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"article_slug": self.slug})

    class Meta:
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    def __str__(self):
        return self.name


class TagArticle(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})

    def __str__(self):
        return self.tag


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
