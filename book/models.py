from django.db import models



STATUS_TYPE = (
    ('available', 'available'),
    ('unavailable', 'unavailable'),
)
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='book', blank=False, null=False)
    status = models.CharField(max_length=50, choices=STATUS_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title

    #ordering
    class Meta:
        ordering = ['-created']
