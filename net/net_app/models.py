from django.db import models
class ShowManager(models.Manager):
 def basic_validator(self, postData):
    errors = {}
    # add keys and values to errors dictionary for each invalid field
    if len(postData['title']) < 5:
        errors["title"] = "Blog name should be at least 5 characters"
    if len(postData['network']) < 10:
        errors["network"] = "Blog description should be at least 10 characters"
    return errors
class Show(models.Model):
    title=models.TextField()
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()

def show_db():
    return Show.objects.all()
def create_shows(title,network,release_date,description):
    return Show.objects.create(title=title,network=network,release_date=release_date,description=description)
def get_show_id(id):
    return Show.objects.get(title=id).id
def some_show(num):
    return Show.objects.get(id=num)
def update(id,title,network,release_date,description):
    
    show=Show.objects.get(id=id)
    show.title=title
    show.network=network
    show.release_date=release_date
    show.description=description
    show.save()
def delete(id):
    show = Show.objects.get(id=id)
    show.delete()