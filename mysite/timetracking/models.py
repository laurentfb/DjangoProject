from django.db import models

class Customer(models.Model):
    customer_code = models.CharField(max_length=15, primary_key=True)
    customer_name = models.CharField(max_length=250)
    customer_active = models.BooleanField()

    def __str__(self):
        return self.customer_name


class Project(models.Model):
    project_code = models.CharField(max_length=15, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_active = models.BooleanField()

    def __str__(self):
        return self.project_name+' (customer : '+str(self.customer)+')'


class Tracking(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    work_date = models.DateField(auto_now=True)
    saved_date = models.DateTimeField(auto_now=True)
    work_load = models.IntegerField()   # Temps en heures (entiers)
    tracking_status = models.SmallIntegerField()    # Status Anticipé, Réel, Supprimé

    @property
    def __str__(self):
        return str(self.project)+ ' - '+str(self.work_load)+' hours on '+str(self.work_date)
