
from summon.models import Summon,Reminder
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response

def print_summon(modeladmin,request,queryset):
    print("coming in print_summon ")
    value=""
    for obj in queryset:
        value=obj
    return render_to_response('summon.html',{'SummonName': obj})   
print_summon.short_description="print summon"


def send_reminder(modeladmin,request,queryset):
    print("coming in print_summon ")
    for obj in queryset:
        print(obj);
    return HttpResponse("Welcome to home ")   
send_reminder.short_description="send reminder"


def add_penality(modeladmin,request,queryset):
    print("coming in print_summon ")
    for obj in queryset:
        print(obj);
    return HttpResponse("Welcome to home ")   
add_penality.short_description="add penality"

def enter_receipt_patial(modeladmin,request,queryset):
    print("coming in enter_receipt_patial ")
    queryset.update(status='RECEIVED_PARTIALLY')
   
enter_receipt_patial.short_description="enter receipt:RECEIVED_PARTIALLY"

def enter_receipt_fully(modeladmin,request,queryset):
    print("coming in enter_receipt_fully ")
    queryset.update(status='RECEIVED')
enter_receipt_fully.short_description="enter receipt:RECEVIED"


class SummonAdmin(admin.ModelAdmin):
    list_display=('sno','partyName','incaseOf','status','isDue',)
    ordering=('-sno',)
    list_filter=('sno','partyName','incaseOf','status')
    search_fields=['sno','partyName',]
    actions=[print_summon,enter_receipt_patial,enter_receipt_fully,add_penality]
    #fields = ('sno', 'partyName', 'incaseOf','status')
    fieldsets=(
        (None,{
            'fields': ('sno','partyName','incaseOf','address'
                       ,'dateofIssue','completionDataAndTime'
                       ,'status')
        }),
        ('options',{
            'classes': ('collapse',),
            'fields': ('option1','option2','option3','option4')
        }),
    )
admin.site.register(Summon,SummonAdmin);
admin.site.register(Reminder);
