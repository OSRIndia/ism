from django.utils import timezone
from summon.models import Summon
#from summon.reminder import Reminder
from django.contrib import admin
from django.shortcuts import render_to_response
import datetime


def print_summon(modeladmin,request,queryset):
    print("coming in print_summon ")
    for obj in queryset:
        pass;
    return render_to_response('summon.html',{'SummonName': obj})   
print_summon.short_description="print summon"

def add_penalty(modeladmin,request,queryset):
    print("coming in add_penality ")
    msg="Telephone Reminder successfully added."
    for obj in queryset:
        if(obj.p1==None):
            print("coming in add_penality 1")
            obj.p1 =timezone.now().date();
            obj.DueDate=obj.p1+datetime.timedelta(days=7)
            obj.save();  
            return render_to_response('penalty.html',{'SummonName': obj})           
        elif (obj.p2==None):
            print("coming in add_penality 2")
            obj.p2 =timezone.now().date();
            obj.DueDate=obj.p2+datetime.timedelta(days=7);
            obj.save();
            return render_to_response('penalty.html',{'SummonName': obj})
        else:
            msg="Two penalty are already added. CANNOT ADDED MORE"
    modeladmin.message_user(request,"%s"%msg)
add_penalty.short_description="add penalty"

def enter_receipt_patial(modeladmin,request,queryset):
    print("coming in enter_receipt_patial ")
    queryset.update(status='RECEIVED_PARTIALLY')
   
enter_receipt_patial.short_description="enter receipt:RECEIVED_PARTIALLY"

def enter_receipt_fully(modeladmin,request,queryset):
    print("coming in enter_receipt_fully ")
    queryset.update(status='RECEIVED')
enter_receipt_fully.short_description="enter receipt:RECEVIED"

def reminder_telephone(modeladmin,request,queryset):
    print("coming in reminder_telephone ")
    msg="Telephone Reminder successfully added."
    for obj in queryset:
        if(obj.telephone1==None):
            print("coming in reminder_telephone 1")
            obj.telephone1 =timezone.now().date();
            obj.DueDate=obj.telephone1+datetime.timedelta(days=7)
            obj.save();  
            msg="Telephone Reminder 1 successfully added."           
        elif (obj.telephone2==None):
            print("coming in reminder_telephone 2")
            obj.telephone2 =timezone.now().date();
            obj.DueDate=obj.telephone2+datetime.timedelta(days=7);
            obj.save();
            msg="Telephone Reminder 2 successfully added."
        else:
            msg="Two telephonic reminders are already done. CANNOT ADDED MORE"
    modeladmin.message_user(request,"%s"%msg)
reminder_telephone.short_description="Telephone Reminder"

def reminder_letter(modeladmin,request,queryset):
    print("coming in reminder_letter 123")
    msg=""
    length =len(queryset);
    if(length!=1):
        msg="ONLY ONE SUMMON CAN BE SELECTED AT ONE TIME FOR LETTER REMINDER"
    else:
        for obj in queryset:
            pass
        if(obj.reminder1==None):
            print("coming in reminder_telephone 1")
            obj.reminder1 =timezone.now().date();
            obj.DueDate=obj.reminder1+datetime.timedelta(days=7)
            obj.save();  
            return render_to_response('reminder.html',{'SummonName': obj})           
        elif (obj.reminder2==None):
            print("coming in reminder_telephone 2")
            obj.reminder2 =timezone.now().date();
            obj.DueDate=obj.reminder2+datetime.timedelta(days=7);
            obj.save();
            return render_to_response('summon.html',{'SummonName': obj})   
        else:
                msg="Two letter reminders are already done. CANNOT ADDED MORE"
        modeladmin.message_user(request,"%s"%msg)
reminder_letter.short_description="Letter Reminder"



class SummonAdmin(admin.ModelAdmin):
    list_display=('sNo','partyName','incaseOf','status','IssueDate','DueDate','isDue',)
    ordering=('-sNo',)
    list_filter=('sNo','partyName','incaseOf','status')
    search_fields=['sNo','partyName',]
    actions=[print_summon,enter_receipt_patial,enter_receipt_fully,add_penalty,reminder_telephone,reminder_letter]
    #fields = ('sno', 'partyName', 'incaseOf','status')
    fieldsets=(
        (None,{
            'fields': ('partyName','incaseOf','address1','city'
                       ,'IssueDate','DueDate'
                       ,'status')
        }),
        ('options',{
            'classes': ('collapse',),
            'fields': ('option1','option2','option3','option4')
        }),
		('reminder details',{
            'classes': ('collapse',),
            'fields': ('telephone1','telephone2','reminder1','reminder2','p1','p2')
        }),
    )
    
#class ReminderAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        print('coming in save model baby')
#        obj.save() 
#        pass
#admin.site.register(Reminder,ReminderAdmin);

admin.site.register(Summon,SummonAdmin);




