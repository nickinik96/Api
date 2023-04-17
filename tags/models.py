from django.db import models
from  django.contrib.contenttypes.models import ContentType
from  django.contrib.contenttypes.fields import GenericForeignKey



#from store.models import Product
# Create your models here.
class Tag (models.Model):
    label = models.CharField(max_length = 255)

class TaggedItems (models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    # product = models.ForeignKey(Product ) 
    # Don't use this becuase in this case we have Tags just for products 
    # and we cann't use Tags for outher object (e.g. articals, )
    
    # Create Generic Relationship:
    # In Django, a generic relationship is a way to create a foreign key 
    # relationship to any model, without knowing the model at the time of 
    # creating the relationship. A generic relationship is useful in 
    # cases where we want to associate a model with multiple other models, 
    # but we don't know in advance which models will be associated with it.
    
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()

