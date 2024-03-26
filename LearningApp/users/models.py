from django.db import models
from django.contrib.auth.models import User  
from PIL import Image  # aus Pillow Lib importiere die Klasse Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # for profile picture
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profil'
    
    def save(self):
        # Speichere die Bilddatei. Das wäre eh passiert. Aber es soll noch eine Funktionalität ergänzt werden.
        super().save()  

        # Öffne die Bilddatei
        imgage = Image.open(self.image.path)  

        # Check ob Bildgröße der Bedingung enspricht:
        if imgage.height > 300 or imgage.width > 300:
            # Tuple der Max-Größe, kann in Zukunft einfach angepasst werden
            output_size = (300, 300)
            # Mache dieses Bild zu einem Thumbnail
            imgage.thumbnail(output_size)
            # Überschreibe die Bilddatei mit dem Thumbnail
            imgage.save(self.image.path)