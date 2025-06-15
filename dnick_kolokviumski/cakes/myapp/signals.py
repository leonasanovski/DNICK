from random import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from myapp.models import Baker, Cake


#Кога се брише пекарот, неговите торти по случаен избор се додаваат на останатите пекари.
@receiver(pre_delete, sender=Baker)
def deletingBaker(sender, instance, **kwargs):
    baker_cakes = Cake.objects.filter(baker=instance)
    all_other_bakers = Baker.objects.exclude(id=instance.id).all()
    for cake in baker_cakes:
        random_baker = random.choice(all_other_bakers)
        cake.baker = random_baker
        cake.save()
