from django.db import models

class dojos(models.Model):
 name = models.CharField(max_length=255)
 city = models.CharField(max_length=255)
 state = models.CharField(max_length=2)
 desc=models.TextField(default="old dojo")
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
class ninjas(models.Model):
 first_name = models.CharField(max_length=255)
 last_name = models.CharField(max_length=255)
 author = models.ForeignKey(dojos, related_name="ninjas", on_delete = models.CASCADE)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
def dojos_db(dojo_name,dojo_city,dojo_state):
    dojos.objects.create(name=dojo_name,city=dojo_city,state=dojo_state,desc="old dojo")
def ninjas_db(ninja_first_name,ninja_last_name,ninja_author):
    ninjas.objects.create(first_name=ninja_first_name,last_name=ninja_last_name,author=dojos.objects.get(name=ninja_author))
def show_dojos():
    return dojos.objects.all()
def Delete(id):
    d=dojos.objects.get(id=id)
    d.delete()