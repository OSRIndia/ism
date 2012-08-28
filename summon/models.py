from django.db import models
from ctypes.wintypes import BOOLEAN
import datetime
from django.utils import timezone


# Create your models here.
class Summon(models.Model):
    SUMMON_STATUS=(
         (u'NEW',u'NEW'),
        (u'SENT',u'SENT'),
        (u'RECEIVED_PARTIALLY',u'RECEIVED_PARTIALLY'),
        (u'RECEIVED',u'RECEIVED'),
    )
    sno=models.CharField(max_length=10,null='false');
    partyName=models.CharField(max_length=100,null='false'); 
    incaseOf=models.CharField(max_length=100,null='false');
    address=models.CharField(max_length=200,null='false');
    dateofIssue=models.DateField();
    completionDataAndTime=models.DateField()
    status=models.CharField(max_length=20,choices=SUMMON_STATUS
                            ,default='NEW');
#    telephone1=models.CharField(max_length=10);
#    telephone2=models.CharField(max_length=10);
#    reminder1=models.CharField(max_length=10);
#    reminder2=models.CharField(max_length=10);
#    p1=models.CharField(max_length=10);
#    p2=models.CharField(max_length=10);
    option1=models.CharField(max_length=20)
    option2=models.CharField(max_length=20)
    option3=models.CharField(max_length=20)
    option4=models.CharField(max_length=20)
    def isDue(self):
        if(self.status!="RECEIVED" and  self.status!="NEW"):
            print("completionDataAndTime:",self.completionDataAndTime)
            if(timezone.now().date()>self.completionDataAndTime):
                return  True;
        return False
    isDue.admin_order_field='completionDataAndTime'
    isDue.boolean=True
    isDue.short_description='in due  ?'
    
    def __unicode__(self):
        return self.partyName
  
class Reminder(models.Model):
    summon=models.ForeignKey(Summon);
    isTelephone=models.BooleanField();
    isReminder=models.BooleanField();
    notificationDate=models.DateField();
    def __unicode__(self):
        temp=""+self.summon.sno+" "+self.notificationDate.__str__();
        return temp
    
     
    
