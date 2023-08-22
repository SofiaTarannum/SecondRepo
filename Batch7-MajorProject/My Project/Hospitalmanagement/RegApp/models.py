from django.db import models
from datetime import date

# Create your models here.
#class file:
#   name:str
class Files(models.Model):
    file=models.FileField(null=True)
class vaccine:
    sid:int
    vid:int
    vacname:str
class revisit:
    id:int
    cname:str
    dob:str
    age:int
    gender:str
    cbloodgrp:str
    fname:str
    faadhno:int
    mname:str
    maadhno:int
    phone:int
    mail:str
    address:str
    selecttype:int
    rid:int
    status:int
    aid:int
    vacid:int
    vacname:str
    cdate:date
    billissue:int
    vreportissue:int
class bill:
    sid:int
    rid:int
    aid:int
    cname:str
    cdate:str
    dob:str
    age:int
    fname:str
    mname:str
    phone:int
    mail:str
    docfee:int
    room:int
    medcost:int
    charges:int
    vaccost:int
    total:int
    ddate:str
    billfile:str
    vacbill:str
    report:str
    vacreport:str
    print:int
    printvac:int
    mailsent:int
    reportsent:int
    vacid:int
    vacname:str
    vacmailsent:int


class jobadd:
    jid:int
    jname:str

class blood11:
    sno:int
    daadhno:int
    dname:str
    mail:str
    phone:int
    bloodgrp:str
    age:int
    dob:str
    gender:str


class job11:
    sno:int
    aname:str
    appaadhar:int
    email:str
    mobile:int
    gender:str
    dob:str
    age:int
    address:str
    city:str
    pin:int
    state:str
    file:str