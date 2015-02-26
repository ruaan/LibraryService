from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Book, BookRegistry, STATUS_CHOICES

@receiver(post_save, sender=Book, dispatch_uid='api.books.create_registry_handler')
def create_registry_handler(sender, **kwargs):
	
	if kwargs.get("created"):
		book = kwargs.get("instance")
		BookRegistry.objects.create(book=book, action='Requested')
