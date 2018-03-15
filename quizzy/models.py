from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Pub(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.ForeignKey(City)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=128)
    postcode = models.CharField(max_length=128)
    url = models.URLField(blank=True)
    telephone = models.CharField(max_length=128, blank=True)
    picture = models.ImageField(upload_to='pub_images', default='defaultpub.jpg')

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pub, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'pubs'

    def __str__(self):
        return self.name


class Quiz(models.Model):
    pub = models.ForeignKey(Pub)
    categories = models.TextField(blank=True)
    WEEKDAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )
    weekday = models.CharField(max_length=128, choices=WEEKDAYS, default='Friday')
    time = models.CharField(max_length=12, blank=True)
    prize = models.TextField(blank=True)
    entry_fee = models.PositiveIntegerField(default=0, null=True, blank=True)
    upVotes = models.PositiveIntegerField(default=0)
    downVotes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return self.weekday


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', default='defaultuser.png')
    favorites = models.ManyToManyField(Quiz, related_name='favorites')
    ratedquizzes = models.ManyToManyField(Quiz, related_name='ratedquizzes')

    def __str__(self):
        return self.user.username
