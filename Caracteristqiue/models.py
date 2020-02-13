
# Create your models here.

from django.db import models

from django.conf import settings
from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL






class Pam(models.Model):

	user                            =models.ForeignKey(User,on_delete=models.CASCADE)
	id_Pt                           =models.IntegerField(primary_key=True)
	Nom_scientifique                =models.CharField(max_length=100)
	nom_vulgaire                    =models.CharField(max_length=100)
	ordre                           =models.CharField(max_length=100)
	famille                         =models.CharField(max_length=100)
	genre                           =models.CharField(max_length=100)
	multiplication                  =models.CharField(max_length=100)
	inflorescence                   =models.CharField(max_length=100)
	type_biologique                 =models.CharField(max_length=100)
	climat                          =models.CharField(max_length=100)
	sol                             =models.CharField(max_length=100)
	temperature                     =models.CharField(max_length=100)
	utilitess                       =models.ManyToManyField('Utilite',verbose_name="Avoir")
	slug                            =models.SlugField(unique=True, max_length=256)

	def __str__(self):
	    return self.Nom_scientifique

	def get_absolute_url(self):
		return reverse("pam_detail", kwargs={"slug": self.slug})



	def _get_unique_slug(self):
	    slug = slugify(self.Nom_scientifique)
	    unique_slug = slug
	    num = 1
	    while Pam.objects.filter(slug=unique_slug).exists():
	        unique_slug = '{}-{}'.format(slug, num)
	        num += 1
	    return unique_slug

	def save(self, *args, **kwargs):
	    if not self.slug:
	        self.slug = self._get_unique_slug()
	    super(Pam, self).save()

class Utilite(models.Model):

	user                             =models.ForeignKey(User,on_delete=models.CASCADE)
	id_Utilite                       =models.IntegerField(primary_key=True)
	maladie                          =models.CharField(max_length=100)
	mode_emploi                      =models.CharField(max_length=100)
	pamss                            =models.ManyToManyField('Pam',verbose_name="Avoir")



	def __str__(self):
	    return self.maladie




class Avoir(models.Model):

	pam             =models.ForeignKey(Pam,on_delete=models.CASCADE)
	utilite          =models.ForeignKey(Utilite,on_delete=models.CASCADE)


