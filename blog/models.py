from django.db import models
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=20)
 
	def __str__(self):  return self.name
 

class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images')
	body = models.TextField(blank=False)
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category',related_name='posts')
	hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
	tags = TaggableManager()

 
	def __str__(self):
		return self.title
	class Meta:
		ordering = ('-created_on', )

	def get_absolute_url(self):
		return reverse('blog_detail', args=[str(self.pk)])

	objects = models.Manager()  # The default manager.
	published = PublishedManager()

class Comment(models.Model):
	author  = models.EmailField(max_length=60)
	body	= models.CharField(max_length=400)
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post',on_delete=models.CASCADE)
		