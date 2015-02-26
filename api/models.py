from django.db import models

STATUS_CHOICES = (
    ('Requested', 'Requested'), 
    ('Approved', 'Approved'), 
    ('Ordered', 'Ordered'), 
    ('Available', 'Available'), 
    ('Out', 'Out'), 
    ('Overdue', 'Overdue'),     
)

class Book(models.Model):

    title = models.TextField(max_length="255", db_index=True)
    motivation = models.TextField(help_text="A motivation for why this book would be a good addition to the library")
    description = models.TextField(help_text="A description of what this book is about")
    
    purchase_url = models.URLField(help_text="The url, including http:// where we can purchase this book from")
    price = models.PositiveIntegerField(null=True)

    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    @property 
    def status(self):
        return BookRegistry.objects.all().order_by('-updated')[1]




class BookRegistry(models.Model):

    book = models.ForeignKey(Book)

    action = models.CharField(max_length=20, db_index=True, default = "Requested", choices=STATUS_CHOICES)

    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)
    


from signals import *
