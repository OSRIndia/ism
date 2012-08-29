from ctypes.wintypes import BOOLEAN
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime



# Create your models here.
class Summon(models.Model):
    SUMMON_STATUS=(
        (u'SENT',u'SENT'),
        (u'RECEIVED_PARTIALLY',u'RECEIVED_PARTIALLY'),
        (u'RECEIVED',u'RECEIVED'),
    )
    sNo=models.AutoField(primary_key=True)
    partyName=models.CharField(max_length=100,blank=False); 
    incaseOf=models.CharField(max_length=100,blank=False);
    address1=models.CharField(max_length=200,blank=False);
    city=models.CharField(max_length=200,blank=False);
    IssueDate=models.DateField();
    DueDate=models.DateField()
    status=models.CharField(max_length=20,choices=SUMMON_STATUS
                            ,default='SENT');
    telephone1=models.DateField(blank=True,null=True);
    telephone2=models.DateField(blank=True,null=True);
    reminder1=models.DateField(blank=True,null=True);
    reminder2=models.DateField(blank=True,null=True);
    p1=models.DateField(blank=True,null=True);
    p2=models.DateField(blank=True,null=True);
    option1=models.CharField(max_length=20, blank=True,null=True)
    option2=models.CharField(max_length=20, blank=True,null=True)
    option3=models.CharField(max_length=20, blank=True,null=True)
    option4=models.CharField(max_length=20, blank=True,null=True)
    def isDue(self):
        if(self.status!="RECEIVED"):
            print("DueDate:",self.DueDate)
            if(timezone.now().date()>self.DueDate):
                return  True;
        return False
    isDue.admin_order_field='DueDate'
    isDue.boolean=True
    isDue.short_description='is due  ?'
    
    def __unicode__(self):
        return self.sNo.__str__()
  

    
     
    
