from django.db import models


class Beer(models.Model):
    """This class represents the beer model."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    country = models.CharField(max_length=255, blank=False)
    image_url = models.CharField(max_length=255, blank=False, default="/static/images/missing.png")
    date_created = models.DateTimeField(blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Beer: {}".format(self.name)


class Snack(models.Model):
    """This class represents the snack model."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    country = models.CharField(max_length=255, blank=False)
    image_url = models.CharField(max_length=255, blank=False, default="/static/images/media/missing.png")
    date_created = models.DateTimeField(blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Snack: {}".format(self.name)
