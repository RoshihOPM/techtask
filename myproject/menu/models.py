from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=200, null=True, blank=True)
    named_url = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url or not self.named_url:
            self.url = f'{self.title}'
            self.named_url = f'{self.title}_url'
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=MenuItem)
def update_url(sender, instance, **kwargs):
    instance.url = f'{instance.title}'
    instance.named_url = f'{instance.title}_url'
