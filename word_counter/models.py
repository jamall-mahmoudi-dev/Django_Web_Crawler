from django.db import models

class Mail(models.Model):
    url = models.URLField(max_length=252, blank=False)
    words = models.TextField(max_length=7000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)      
    class Meta:
        ordering = ['-created_at']  
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'

    def __str__(self):
        return f"{self.url} -  {self.created_at}"