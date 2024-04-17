from django.db import models
from django.contrib.auth.models import User  
from PIL import Image  # aus Pillow Lib importiere die Klasse Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # for profile picture
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profil'
    
    def save(self, *args, **kwargs):
        # Speichere die Bilddatei. Das wäre eh passiert. Aber es soll noch eine Funktionalität ergänzt werden.
        super(Profile, self).save(*args, **kwargs)  
        
        # Öffne die Bilddatei
        image = Image.open(self.image.path) 
        # Checke Bilddateityp
        if image.mode in ('JPG'):
        # Konvertiere Image von JPG zu PNG
            image = image.convert('RGB')

    
        # Check ob Bildgröße der Bedingung enspricht:
        if image.height > 100 or image.width > 100:
            # Tuple der Max-Größe, kann in Zukunft einfach angepasst werden
            output_size = (300, 300)
            # Mache dieses Bild zu einem Thumbnail
            image.thumbnail(output_size)
            # Überschreibe die Bilddatei mit dem Thumbnail
            image.save(self.image.path)