from django.db import models


class Apps(models.Model):

    LINEOFBUSINESS = (
			('CoreBanking', 'CoreBanking'),
			('WebPayment', 'WebPayment'),
            ('ATH', 'ATH'),
			) 
    CRITIC = (
			('HIGH', 'HIGH'),
			('Normal', 'Normal'),           
			)  

    PATCH =	(
            ('A', 'A'),
			('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),           
			)               

    mne = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    lob = models.CharField(max_length=200, null=True, choices=LINEOFBUSINESS)    
    critic = models.CharField(max_length=200, null=True, choices=CRITIC) 
    Patch_group = models.CharField(max_length=200, null=True, choices=PATCH)

    def __str__(self):
        return self.mne



class Server(models.Model):

    OS = (
			('UNIX', 'UNIX'),
            ('Windows', 'Windows'),
			)              

    ip = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    app = models.ForeignKey(Apps, on_delete= models.CASCADE)
    os = models.CharField(max_length=200, null=True, choices=OS)    
   

    def __str__(self):
        return self.ip


class Contacts(models.Model):        

    supervisor = models.CharField(max_length=100)
    contacto_val = models.CharField(max_length=100)
    contacto_oncall = models.CharField(max_length=100)         
    app = models.ForeignKey(Apps, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.supervisor

class F5(models.Model):

    f5_url = models.URLField(max_length=200)
    app = models.ForeignKey(Apps, null=True, on_delete= models.SET_NULL)
    f5_partitions = models.TextField()

    def __str__(self):
        return self.f5_url 



# Create your models here.
