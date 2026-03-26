from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Received On")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} • {self.created_at.strftime('%b %d, %Y')}"