from django.db import models
from django.contrib import admin


class Quorum(models.Model):
   quorum_name = models.TextField("Quorum/Class")
   quorum_min_date = models.DateField("Minimum date cutoff")
   quorum_max_date = models.DateField("Maximum date cutoff")
   
   @admin.display(
      boolean=True,
      ordering="quorum_min_date",
      description="Minimum Cutoff Date",
   )
   def __str__(self):
      return self.quorum_name

class Stake(models.Model):
   name= models.TextField("Stake")

   def __str__(self):
      return self.name

class Ward(models.Model):
   name = models.TextField("Ward")
   stake = models.ForeignKey(Stake, on_delete=models.CASCADE)
   
   def __str__(self):
      return self.name

class Family(models.Model):
   name = models.TextField("Family")
   address = models.TextField("Address")
   
   def __str__(self):
      return self.name

class Calling(models.Model):
   name = models.TextField("Calling")

   class Meta:
      ordering = ["name"]
   
   
   def __str__(self):
      return self.name

class User(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   birthdate = models.DateField("Birthday")
   quorum = models.ForeignKey(Quorum, on_delete=models.RESTRICT)
   family = models.ForeignKey(Family, on_delete=models.RESTRICT)
   ward = models.ForeignKey(Ward, on_delete=models.RESTRICT)
   callings = models.ManyToManyField(Calling)

   class Meta:
      ordering = ["last_name"]
   
   
   def __str__(self):
      return f'{self.first_name} {self.last_name}'
   

class Event(models.Model):
   title = models.CharField(max_length=50)
   time = models.TimeField()
   date = models.DateField()
   location = models.CharField(max_length=150)
   description = models.TextField()
   attendees = models.ManyToManyField(User)

   class Meta:
      ordering = ["date"]

   
   def __str__(self):
      return self.title

class Assignment(models.Model):
   title = models.CharField(max_length=100)
   owner = models.ForeignKey(User, on_delete=models.CASCADE)
   event = models.ForeignKey(Event, on_delete=models.CASCADE)

 
   def __str__(self):
      return self.title  