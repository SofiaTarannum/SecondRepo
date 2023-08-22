from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . models import Files, vaccine, revisit, bill, jobadd,blood11, job11
from datetime import date,datetime
from pathlib import Path
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from .models import *
import urllib.parse
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def index(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from vaccines where sid")
    result= query.fetchall()
    vaccines=[]
    for row in result:
        s=vaccine()
        s.sid=row[0]
        s.vid=row[1]
        s.vname=row[2]
    vaccines.append(s)  
    query1 = conn.cursor()
    query1.execute("select * from vaccines")
    result= query1.fetchall()      
    return render(request,'index.html',{"vaccine":vaccines})#{ key:list} 
     

def news(request):
    return render(request,'news-detail.html')

def doctorapp(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        cname=request.POST['cname']
        dob=request.POST['dob']  
        age=request.POST['age']
        gender=request.POST['gender']
        cblood=request.POST['cblood']
        fname=request.POST['fname']
        faadhar=request.POST['faadhar']
        mname=request.POST['mname']  
        maadhar=request.POST['maadhar'] 
        phone=request.POST['phone'] 
        email=request.POST['email'] 
        message=request.POST['message']     
        today=date.today()
        b=str(today)
        mycursor.execute("SELECT MAX(rid) FROM registration")
        result=mycursor.fetchone()
        for i in result:
            y=i+1
        z=str(y)
        
        mycursor.execute("SELECT MAX(aid) FROM registration")
        result=mycursor.fetchone()
        for i in result:
            x=i+1
        aid=str(x)
    
       
        
        mycursor.execute("insert into registration(cname,dob,age,gender,cbloodgrp,fname,faadhno,mname,maadhno,phone,mail,address,selecttype,rid,status,aid,cdate,billissue) values('"+cname+"','"+dob+"','"+age+"','"+gender+"','"+cblood+"','"+fname+"','"+faadhar+"','"+mname+"','"+maadhar+"','"+phone+"','"+email+"','"+message+"','0','"+z+"','0','"+aid+"','"+b+"','0')")
        conn.commit()
        
        return render(request,'rid_success.html',{'r':z})
    else:
        return render(request,'doctorapp.html')


def revisitdc(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        rid=request.POST['rid'] 
        mycursor.execute("select distinct cname, dob, age, gender, cbloodgrp, fname, faadhno, mname, maadhno, phone, mail, address, rid from registration  where rid='"+rid+"' and selecttype='0' ")
        result3=mycursor.fetchall()
        patients=[]
        for row in result3:
            s=revisit()
            s.rid=row[12]
            s.cname=row[0]
            s.dob=row[1]
            s.cbloodgrp=row[4]
            s.faadhno=row[6]
            s.mname=row[7]
            s.maadhno=row[8]
            #s.selecttype=row[12]
            #s.status=row[14]
            s.age=row[2]
            s.gender=row[3]
            s.fname=row[5]
           
            s.address=row[11]
            s.phone=row[9]
            s.mail=row[10]
            patients.append(s)
        
        return render(request,'revisitdetails.html',{"patient":patients})#{ key:list} 
    else:
        return render(request,'revisitdc.html')


def  vac(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        cname=request.POST['cname']
        dob=request.POST['dob']  
        age=request.POST['age']
        gender=request.POST['gender']
        cblood=request.POST['cblood']
        fname=request.POST['fname']
        faadhar=request.POST['faadhar']
        mname=request.POST['mname']  
        maadhar=request.POST['maadhar'] 
        phone=request.POST['phone'] 
        email=request.POST['email'] 
        message=request.POST['message'] 
        vacname=request.POST['vacname'] 
        mycursor.execute("SELECT vid FROM vaccines where vname='"+vacname+"'")
        result8=mycursor.fetchone()
        q=str(result8[0])
        




        today=date.today()
        b=str(today)
        mycursor.execute("SELECT MAX(rid) FROM registration")
        result1=mycursor.fetchone()
        for i in result1:
            y=i+1
        z=str(y)
       
        
        mycursor.execute("SELECT MAX(aid) FROM registration")
        result1=mycursor.fetchone()
        for i in result1:
            x=i+1
        aid=str(x)
        rid=[]
        rid.append(z)
        
        
        
        mycursor.execute("insert into registration(cname,dob,age,gender,cbloodgrp,fname,faadhno,mname,maadhno,phone,mail,address,selecttype,rid,status,aid,vacid,vacname,cdate) values('"+cname+"','"+dob+"','"+age+"','"+gender+"','"+cblood+"','"+fname+"','"+faadhar+"','"+mname+"','"+maadhar+"','"+phone+"','"+email+"','"+message+"','1','"+z+"','0','"+aid+"','"+q+"','"+vacname+"','"+b+"')")
        conn.commit()
        
        return render(request,'rid_success.html',{'r':rid})
    else:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor = conn.cursor()
        mycursor.execute("select * from vaccines")
        result = mycursor.fetchall()
        cat = []
        for x in result:

            obj = vaccine()
            obj.vacname= x[2]
            cat.append(obj)
        #mycursor.execute("select vid from vaccines where vacname=obj.vacname ")
        #result1= mycursor.fetchall()
        #c= []
        #for y in result1:
            #s=vaccine()
            #s.vid=y[1]
            #c.append(s)


        return render(request,'vac.html', {'p':cat} )

def vaccn(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        rid=request.POST['id2'] 
        mycursor.execute("select distinct cname, dob, age, gender, cbloodgrp, fname, faadhno, mname, maadhno, phone, mail, address, rid from registration  where rid='"+rid+"'")
        result3=mycursor.fetchall()
        patients=[]
        for row in result3:
            s=revisit()
            s.rid=row[12]
            s.cname=row[0]
            s.dob=row[1]
            s.cbloodgrp=row[4]
            s.faadhno=row[6]
            s.mname=row[7]
            s.maadhno=row[8]
            #s.selecttype=row[12]
            #s.status=row[14]
            s.age=row[2]
            s.gender=row[3]
            s.fname=row[5]
           
            s.address=row[11]
            s.phone=row[9]
            s.mail=row[10]
            patients.append(s)
        return render(request,'revisitvac.html',{"patient":patients})
    else:
        return render(request,'vacc2.html')

def revisitvac(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()


        rid=request.POST['rid']
        cname=request.POST['cname']
        status="0"
        age=request.POST['age']
        gender=request.POST['gender']
        fname=request.POST['fname']
        address=request.POST['address']
        phone=request.POST['phone']
        mail=request.POST['mail']
        dob=request.POST['dob']
        cbloodgrp=request.POST['cbloodgrp']
        faadhno=request.POST['faadhno']
        mname=request.POST['mname']
        maadhno=request.POST['maadhno']
        selecttype="1"
        print("Sofia")
        vacname=request.POST['vacname']
        mycursor.execute("SELECT vid FROM vaccines where vname='"+vacname+"'")
        result8=mycursor.fetchone()
        q=str(result8[0])
        


        mycursor.execute("SELECT MAX(aid) FROM registration")
        result=mycursor.fetchone()
        for i in result:
            x=i+1
        aid=str(x)

        today=date.today()
        b=str(today)

        mycursor.execute("insert into registration(cname,dob,age,gender,cbloodgrp,fname,faadhno,mname,maadhno,phone,mail,address,selecttype,rid,status,aid,cdate,billissue,vacname,vacid) values('"+cname+"','"+dob+"','"+age+"','"+gender+"','"+cbloodgrp+"','"+fname+"','"+faadhno+"','"+mname+"','"+maadhno+"','"+phone+"','"+mail+"','"+address+"','"+selecttype+"','"+rid+"','"+status+"','"+aid+"','"+b+"','1','"+vacname+"','"+q+"')")
        conn.commit()
        return render(request,'successfullreappoinment.html')
        
    else:
        print("Madhu")
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor = conn.cursor()
        mycursor.execute("select * from vaccines")
        result = mycursor.fetchall()
        cat = []
        for x in result:

            obj = vaccine()
            obj.vacname= x[2]
            cat.append(obj)
        #mycursor.execute("select vid from vaccines where vacname=obj.vacname ")
        #result1= mycursor.fetchall()
        #c= []
        #for y in result1:
            #s=vaccine()
            #s.vid=y[1]
            #c.append(s)
        

        return render(request,'revisitvac.html', {'p':cat} )


def appsucc(request):
    return render(request,'appoinmentsuccessfull.html')


def revisitdetails(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()


        rid=request.POST['rid']
        cname=request.POST['cname']
        status="0"
        age=request.POST['age']
        gender=request.POST['gender']
        fname=request.POST['fname']
        address=request.POST['address']
        phone=request.POST['phone']
        mail=request.POST['mail']
        dob=request.POST['dob']
        cbloodgrp=request.POST['cbloodgrp']
        faadhno=request.POST['faadhno']
        mname=request.POST['mname']
        maadhno=request.POST['maadhno']
        selecttype="0"

        mycursor.execute("SELECT MAX(aid) FROM registration")
        result=mycursor.fetchone()
        for i in result:
            x=i+1
        aid=str(x)

        today=date.today()
        b=str(today)

        mycursor.execute("insert into registration(cname,dob,age,gender,cbloodgrp,fname,faadhno,mname,maadhno,phone,mail,address,selecttype,rid,status,aid,cdate,billissue) values('"+cname+"','"+dob+"','"+age+"','"+gender+"','"+cbloodgrp+"','"+fname+"','"+faadhno+"','"+mname+"','"+maadhno+"','"+phone+"','"+mail+"','"+address+"','"+selecttype+"','"+rid+"','"+status+"','"+aid+"','"+b+"','0')")
        conn.commit()
        return render(request,'successfullreappoinment.html')
    else:
        return render(request,'revisitdetails.html')


def vaccsuccessfull(request):
    return render(request,'vaccsuccessfull.html')


def successfullre(request):
    return render(request,'successfullreappoinment.html')


def bloods(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        daadhno=request.POST['daadhar']
        dname=request.POST['dname']  
        mail=request.POST['email']
        phone=request.POST['pnum']
        bloodgrp=request.POST['bgroup'] 
        age=request.POST['age']
        dob=request.POST['dob']
        gender='female'
         


        mycursor.execute("insert into userblood(daadhno,dname,mail,phone,bloodgrp,age,dob,gender) values('"+daadhno+"','"+dname+"','"+mail+"','"+phone+"','"+bloodgrp+"','"+age+"','"+dob+"','"+gender+"')")
        conn.commit()
        return redirect('bloodsuccess')
    else:
        return render(request,'blood.html')
        
    
    
def bloodsuccess(request):
  return render(request,'bloodsuccess.html')


def jobs(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        #filename='xyz.png'
        mycursor =conn.cursor()
        aname=request.POST['aname']
        appaadhar=request.POST['appaadhar']
        email=request.POST['email']
        mobile=request.POST['mobile']
        gender='female'
        dob=request.POST['dob']
        age=request.POST['age']
        address=request.POST['address']
        city=request.POST['city']
        pin=request.POST['pin']
        state=request.POST['state']
        jname=request.POST['jobname']
        


        mycursor.execute("insert into job(aname,appaadhar,email,mobile,gender,dob,age,address,city,pin,state,file,jname) values('"+aname+"','"+appaadhar+"','"+email+"','"+mobile+"','"+gender+"','"+dob+"','"+age+"','"+address+"','"+city+"','"+pin+"','"+state+"','"+filename+"','"+jname+"')")
        
        conn.commit()
        return render(request, 'jobsuccess.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor = conn.cursor()
        mycursor.execute("select * from jobs")
        result = mycursor.fetchall()
        c=[]
        for row in result:
            s=jobadd()
            s.jname=row[1]
            c.append(s)

        return render(request,'job.html',{'b':c})
    

def jobsuccess(request):
  return render(request,'jobsuccess.html')

def pagelogin(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        mail=request.POST['mail']
        password=request.POST['password']
        mycursor.execute("select * from adminlogin where mail='"+mail+"' and password='"+password+"' ")
        result=mycursor.fetchone()
        if(result!=None):
           
            return redirect('admin_index')
        
            #redirect('dashboard')
        else:
            return render(request,'page_login.html',{'status':'invalid credentials'})    
    else:
        return render(request,'page_login.html')
def adminindex(request):
    conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
    mycursor=conn.cursor()
    mycursor.execute("select max(aid) from registration")
    result=mycursor.fetchone()        
    aid=str(result[0])
    mycursor.execute("select count(status) from registration where status=1")
    result1=mycursor.fetchone()
    p=str(result1[0])
    mycursor.execute("select count(status) from registration where status=0")
    result2=mycursor.fetchone()
    q=str(result2[0])
    mycursor.execute("select sum(total) from billings ")
    result3=mycursor.fetchone()
    r=str(result3[0])
    
    mycursor.execute("select * from userblood where remove='0'")
    result4=mycursor.fetchall()
    donars=[]
    for row in result4:
        s=blood11()
        s.sno=row[0]
        s.daadhno=row[1]
        s.dname=row[2]
        s.mail=row[3]
        s.phone=row[4]
        s.bloodgrp=row[5]
        s.age=row[6]
        s.dob=row[7]
        s.gender=row[8]
        donars.append(s)

    mycursor.execute("select distinct rid, cname, mname, fname, dob, gender,age, mail, phone,address from registration where dis='0'")
    result5=mycursor.fetchall()
    registered=[]
    for row in result5:
       s=revisit()
      
       s.cname=row[1]
       s.dob=row[4]
       s.age=row[6]
       s.gender=row[5]
       s.cbloodgrp=row[5]
       s.fname=row[3]
       
       s.mname=row[2]
       
       s.phone=row[8]
       s.mail=row[7]
       s.address=row[9]
       
       s.rid=row[0]
       
       registered.append(s)

    mycursor.execute("select * from job where remove='0'")
    result6=mycursor.fetchall()
    applicant=[] 
    for row in result6:
        s=job11()
        s.sno=row[0]
        s.aname=row[1]
        s.appaadhar=row[2]
        s.email=row[3]
        s.mobile=row[4]
        s.gender=row[5]
        s.dob=row[6]
        s.age=row[7]
        s.address=row[8]
        s.city=row[9]
        s.pin=row[10]
        s.state=row[11]
        s.file=row[12]
        
        applicant.append(s)

    return render(request, 'admin_index.html', {'b':aid,'c':p,'d':q,'e':r,'donars':donars,'registered':registered,'applicant':applicant})




def removebloodsuccess(request,sno):
    
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'hospital'
    )
    query = conn.cursor()
    query.execute("update userblood set remove='1' where sno='"+sno+"'")
    conn.commit()
    return render(request,'removebloodsuccess.html')




def removejobuser(request,sno):
    
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'hospital'
    )
    query = conn.cursor()
    query.execute("update job set remove='1' where sno='"+sno+"'")
    conn.commit()
    return render(request,'removejobuser.html')
    
def pageforget(request):
    if(request.method=='POST'):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        mycursor = mydb.cursor()
            #retrive post details 
        email=request.POST['email']  
        result=None    
        mycursor.execute("select * from adminlogin where mail='"+email+"'")
        result=mycursor.fetchone()
        if(result!=None):        
            smtp_server = "smtp.gmail.com"
            port = 587  # for starttls 
            sender_email = "madhumithauppala@gmail.com"  # Replace with your sender email address
            password = "iqnluwqzranptqee"  # Replace with your email password or use environment variable
            
            email = request.POST['email']
            receiver_email = email.split(',')

            #text = request.POST['msg']
            #subject = request.POST['subject']
            
            # create the url for the form 
            base_url = request.build_absolute_uri('/')

            changepwd_url = urllib.parse.urljoin(base_url,  'changepwd/')

            # include the url in  the email body
            message = 'Subject: \n\n\n\nTo fill the form, please click on this link: {}'.format(changepwd_url)

            #This message is sent from Python.

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                for x in receiver_email:
                    server.sendmail(sender_email, x,message)
                return render(request,'pageforgetemailsuc.html')    
        else:
            return render(request,'page-forgot-password.html')
    else:
         return render(request,'page-forgot-password.html' )


def pageforgetemailsuc(request):
    return render(request,'pageforgetemailsuc.html')

def changepwd(request):
    # render the form that the user needs to fill
    #if "username" in request.session:
     #   uname = request.session.get("username")
    if(request.method=='POST'):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        newcur=con.cursor()
        email=request.POST["email"]
        password=request.POST["password"]
        newcur.execute("update adminlogin set password='" + password + "' where mail='" + email + "'")
        #newcur.execute("update users set password=%s where email=%s", (password, email))
        con.commit() 
        return render(request,'page_login.html')
    else:
        return render(request,'changepwd.html')
    


    #return render(request,'page-forgot-password.html')
#def pagereg(request):
#    return render(request,'page-register.html')
#def patient(request):
#    return render(request,'patient.html')
#def patientd(request):
#    return render(request,'patient-details.html')
#def doctor(request):
#    return render(request,'doctor.html')
def doctordetails(request):
    return render(request,'doctor-details.html')
def reviews(request):
    return render(request,'reviews.html')
def emailcompose(request,sid):
    
    conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="hospital"
    )
    mycursor =conn.cursor()
    mycursor.execute("update billings set mailsent='1' where sid='"+sid+"'")
    conn.commit()
    mycursor.execute("select * from billings where sid='"+sid+"'")
    # get email id and file name of the customer using sid
    #select mail, billfile from billings where sid=sid
    result=mycursor.fetchone()
    print("sofia")
    if(result!=None):
        print("x")
        customeremail= result[10]  #str(result[0])
        filename = result[18] #result[1]

        BASE_DIR = Path(__file__).resolve().parent.parent
        fromaddr = "madhumithauppala@gmail.com"
        toaddr = customeremail
        
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        # storing the senders email address  
        msg['From'] = fromaddr
        
        # storing the receivers email address 
        msg['To'] = toaddr
        
        # storing the subject 
        msg['Subject'] = "Rammohan Children's Hospital"
        
        # string to store the body of the mail
        body = "Hi, Please check the hospital bill"
        
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        filepath=str(BASE_DIR)+"\\media\\"+filename
        print(filepath)
        # open the file to be sent 
        attachment = open(filepath, "rb")
        
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        
        # encode into base64
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(fromaddr, "iqnluwqzranptqee")
        
        # Converts the Multipart msg into a string
        text = msg.as_string()
        
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        
        # terminating the session
        s.quit()
        print("hii")
        return render(request, 'email-compose.html')
    else:
        return render(request, 'sendbills.html')
  

def emailinbox(request):
    return render(request,'email-inbox.html')
def emailread(request):
    return render(request,'email-read.html')
def chartflot(request):
    return render(request,'chart-flot.html')
def chartmorris(request):
    return render(request,'chart-morris.html')
def chartchartjs(request):
    return render(request,'chart-chartjs.html')
def chartchartist(request):
    return render(request,'chart-chartist.html')
def chartsparkline(request):
    return render(request,'chart-sparkline.html')
def chartpeity(request):
    return render(request,'chart-peity.html')



def load(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        )
    mycursor = mydb.cursor()
    #retrive post details       
    mycursor.execute("select * from job")
    result=mycursor.fetchall()
    files=[]
    for x in result:
        f=Files()
        f.file=x[12]      
        files.append(f)    
    return render(request,'load.html',{"files":files})


def managevac(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from vaccines")
    result= query.fetchall()
    vaccines=[]
    for row in result:
        s=vaccine()
        s.sid=row[0]
        s.vacname=row[2]
        vaccines.append(s)  
    return render(request,'managevac.html',{"vaccine":vaccines})#{ key:list}



def add_vac(request):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        vid=request.POST['vid']
        vacname=request.POST['vacname']
        
        query.execute("select * from vaccines where vid='"+vid+"'")
        result= query.fetchone()
        if(result==None):
               
            query.execute("insert into vaccines(vid,vname) values('"+vid+"','"+vacname+"')")
            conn.commit()
            return render(request, 'addsuccess.html')
            
        else:
            return render(request, 'addexists.html')
    else:
        
       
        return render(request,'add_vac.html')



def edit_vac(request,sid):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        
        vid = request.POST['vid']
        vacname = request.POST['vacname']
        query.execute("update vaccines set sid='"+sid+"',vid ='"+vid+"',vname ='"+vacname+"' where sid='"+sid+"'")
        conn.commit()
        return render(request, 'success.html')
    
    
    else:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        query.execute("select * from vaccines where sid='"+sid+"'")
        result= query.fetchall()
        vaccines=[]
        for row in result:
            s=vaccine()
            s.sid=row[0]
            s.vid=row[1]
            s.vname=row[2]
            
            vaccines.append(s)  
        query1 = conn.cursor()
        query1.execute("select * from vaccines")
        result= query1.fetchall()
        
         
        return render(request,'edit_vac.html',{"vaccine":vaccines})#{ key:list}            



def del_vac(request,sid):
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'hospital'
    )
    query = conn.cursor()
    query.execute("DELETE FROM vaccines where sid='"+sid+"'")
    conn.commit()
    return render(request, 'del_vac.html')


def success(request):
    return render(request,'success.html')

def addsuccess(request):
    return render(request,'addsuccess.html')



def notpatient(request):
    return render(request,'notpatient.html')



def patientdis(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from registration where billissue='0' and selecttype='0'")
    result= query.fetchall()
    patients=[]
    for row in result:
        s=revisit()
        s.id=row[0]
        s.cname=row[1]
        s.dob=row[2]
        s.age=row[3]
        s.gender=row[4]
        s.cbloodgrp=row[5]
        s.fname=row[6]
        s.faadhno=row[7]
        s.mname=row[8]
        s.maadhno=row[9]
        s.phone=row[10]
        s.mail=row[11]
        s.address=row[12]
        s.selecttype=row[13]
        s.rid=row[14]
        s.status=row[15]
        s.aid=row[16]
        s.vacid=row[17]
        s.vacname=row[18]
        s.cdate=row[19]
        s.billissue=row[20]
        s.vreportissue=row[21]
        patients.append(s)  
    return render(request,'patientdis.html',{"patient":patients})#{ key:list}



def generateinpatientbills(request,id):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        
        rid = request.POST['rid']
        aid = request.POST['aid']
        cname = request.POST['cname']
        #datetime_str = str(request.POST['cdate'])
        cdate = request.POST['cdate']
        dob=request.POST['dob']
        age=request.POST['age']
        fname = request.POST['fname']
        mname = request.POST['mname']
        phone = request.POST['phone']
        mail = request.POST['mail']
        docfee = request.POST['docfee']
        room = request.POST['room']
        medcost = request.POST['medcost']
        charges = request.POST['charges']
        total=request.POST['total']
        today=date.today()
        ddate=str(today)
        query.execute("update registration set billissue='1' where id='"+id+"'")
        query.execute("insert into billings(rid,aid,cname,cdate,dob,age,fname,mname,phone,mail,docfee,room,medcost,charges,total,ddate,print) values('"+rid+"','"+aid+"','"+cname+"','"+cdate+"','"+dob+"','"+age+"','"+fname+"','"+mname+"','"+phone+"','"+mail+"','"+docfee+"','"+room+"','"+medcost+"','"+charges+"','"+total+"','"+ddate+"','0')")
        conn.commit()
        return redirect('printdis')
        
    else:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    
    query.execute("select * from registration where id='"+id+"'")
    result= query.fetchall()
    patients=[]
    for row in result:
        s=revisit()
        s.id=row[0]
        s.cname=row[1]
        s.dob=row[2]
        s.age=row[3]
        s.gender=row[4]
        s.cbloodgrp=row[5]
        s.fname=row[6]
        s.faadhno=row[7]
        s.mname=row[8]
        s.maadhno=row[9]
        s.phone=row[10]
        s.mail=row[11]
        s.address=row[12]
        s.selecttype=row[13]
        s.rid=row[14]
        s.status=row[15]
        s.aid=row[16]
        s.vacid=row[17]
        s.vacname=row[18]
        s.cdate=row[19]
        s.billissue=row[20]
        s.vreportissue=row[21]
        patients.append(s)  
    return render(request,'generateinpatientbills.html',{"patient":patients})#{ key:list}
    

def printdis(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from billings where print='0'")
    result= query.fetchall()
    inpatients=[]
    for row in result:
       s=bill()
       s.sid=row[0]
       s.rid=row[1]
       s.aid=row[2]
       s.cname=row[3]
       s.cdate=row[4]
       s.dob=row[5]
       s.age=row[6]
       s.fname=row[7]
       s.mname=row[8]
       s.phone=row[9]
       s.mail=row[10]
       s.room=row[12]
       s.docfee=row[11]
       s.medcost=row[13]
       s.charges=row[14]
       s.vaccost=row[15]
       s.total=row[16]
       s.ddate=row[17]
       s.billfile=row[18]
       s.vacbill=row[19]
       s.report=row[20]
       s.vacreport=row[21]
       s.print=row[22]
       s.printvac=row[23]
       s.mailsent=row[24]
       s.reportsent=row[25]
       s.vacid=row[26]
       s.vacname=row[27]
       s.vacmailsent=row[28]
       inpatients.append(s)  
    return render(request,'printdis.html',{"inpatient":inpatients})


def print_inpatientbills(request,sid):
   
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    print('hi')
    query.execute("update billings set print='1' where sid='"+sid+"'")
    conn.commit()
    query.execute("select * from billings where sid='"+sid+"'")
    result= query.fetchall()
    inpatients=[]
    for row in result:
        s=bill()
        s.sid=row[0]
        s.rid=row[1]
        s.aid=row[2]
        s.cname=row[3]
        s.cdate=row[4]
        s.dob=row[5]
        s.age=row[6]
        s.fname=row[7]
        s.mname=row[8]
        s.phone=row[9]
        s.mail=row[10]
        s.room=row[12]
        s.docfee=row[11]
        s.medcost=row[13]
        s.charges=row[14]
        s.vaccost=row[15]
        s.total=row[16]
        s.ddate=row[17]
        s.billfile=row[18]
        s.vacbill=row[19]
        s.report=row[20]
        s.vacreport=row[21]
        s.print=row[22]
        s.printvac=row[23]
        s.mailsent=row[24]
        s.reportsent=row[25]
        s.vacid=row[26]
        s.vacname=row[27]
        s.vacmailsent=row[28]
        
        inpatients.append(s)  
    return render(request,'print_inpatientbills.html',{"inpatient":inpatients})
        





def uploadvacbill(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        #filename='xyz.png'
        mycursor =conn.cursor()
        rid=request.POST['rid']
        cname=request.POST['cname']
        aid=request.POST['aid']
        
        


        mycursor.execute("update billings set vacbill='"+filename+"' where rid='"+rid+"' and aid='"+aid+"'")
        
        conn.commit()
        return redirect('uploadvacbillsuccess')
    else:
        return render(request,'uploadvacbill.html')





def uploadvacbillsuccess(request):
    return render(request,'uploadvacbillsuccess.html')



def sendvacbill(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from billings where vacbill IS NOT NULL and vacmailsent='0'")
    result= query.fetchall()
    bills=[]
    for row in result:
        s=bill()
        s.sid=row[0]
        s.rid=row[1]
        s.aid=row[2]
        s.cname=row[3]
        s.cdate=row[4]
        s.dob=row[5]
        s.age=row[6]
        s.fname=row[7]
        s.mname=row[8]
        s.phone=row[9]
        s.mail=row[10]
        s.room=row[12]
        s.docfee=row[11]
        s.medcost=row[13]
        s.charges=row[14]
        s.vaccost=row[15]
        s.total=row[16]
        s.ddate=row[17]
        s.billfile=row[18]
        s.vacbill=row[19]
        s.report=row[20]
        s.vacreport=row[21]
        s.print=row[22]
        s.printvac=row[23]
        s.mailsent=row[24]
        s.reportsent=row[25]
        s.vacid=row[26]
        s.vacname=row[27]
        s.vacmailsent=row[28]

        bills.append(s) 
    return render(request,'sendvacbill.html',{"bills":bills})#{ key:list}




def email_composevac(request,sid):
    
    conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="hospital"
    )
    mycursor =conn.cursor()
    mycursor.execute("update billings set vacmailsent='1' where sid='"+sid+"'")
    conn.commit()
    mycursor.execute("select * from billings where sid='"+sid+"'")
    # get email id and file name of the customer using sid
    #select mail, billfile from billings where sid=sid
    result=mycursor.fetchone()
    print("sofia")
    if(result!=None):
        print("x")
        customeremail= result[10]  #str(result[0])
        filename = result[19] #result[1]

        BASE_DIR = Path(__file__).resolve().parent.parent
        fromaddr = "madhumithauppala@gmail.com"
        toaddr = customeremail
        
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        # storing the senders email address  
        msg['From'] = fromaddr
        
        # storing the receivers email address 
        msg['To'] = toaddr
        
        # storing the subject 
        msg['Subject'] = "Rammohan Children's Hospital"
        
        # string to store the body of the mail
        body = "Hi, Please check the hospital bill"
        
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        filepath=str(BASE_DIR)+"\\media\\"+filename
        print(filepath)
        # open the file to be sent 
        attachment = open(filepath, "rb")
        
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        
        # encode into base64
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(fromaddr, "iqnluwqzranptqee")
        
        # Converts the Multipart msg into a string
        text = msg.as_string()
        
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        
        # terminating the session
        s.quit()
        print("hii")
        return render(request, 'email_composevac.html')
    else:
        return render(request, 'sendvacbill.html')


def uploadfile(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        #filename='xyz.png'
        mycursor =conn.cursor()
        rid=request.POST['rid']
        cname=request.POST['cname']
        aid=request.POST['aid']
        
        


        mycursor.execute("update billings set billfile='"+filename+"' where rid='"+rid+"' and aid='"+aid+"'")
        
        conn.commit()
        return redirect('uploadfilesuccess')
    else:
        return render(request,'uploadfile.html')

def uploadfilesuccess(request):
    return render(request,'uploadfilesuccess.html')


def sendbills(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from billings where mailsent='0' and billfile IS NOT NULL")
    result= query.fetchall()
    bills=[]
    for row in result:
        s=bill()
        s.sid=row[0]
        s.rid=row[1]
        s.aid=row[2]
        s.cname=row[3]
        s.cdate=row[4]
        s.dob=row[5]
        s.age=row[6]
        s.fname=row[7]
        s.mname=row[8]
        s.phone=row[9]
        s.mail=row[10]
        s.room=row[12]
        s.docfee=row[11]
        s.medcost=row[13]
        s.charges=row[14]
        s.vaccost=row[15]
        s.total=row[16]
        s.ddate=row[17]
        s.billfile=row[18]
        s.vacbill=row[19]
        s.report=row[20]
        s.vacreport=row[21]
        s.print=row[22]
        s.printvac=row[23]
        s.mailsent=row[24]
        s.reportsent=row[25]
        s.vacid=row[26]
        s.vacname=row[27]
        s.vacmailsent=row[28]

        bills.append(s) 
    return render(request,'sendbills.html',{"bills":bills})#{ key:list}




def uploadreportfile(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        #filename='xyz.png'
        mycursor =conn.cursor()
        rid=request.POST['rid']
        cname=request.POST['cname']
        aid=request.POST['aid']
        mail=request.POST['mail']
        
        


        mycursor.execute("insert into billings(rid,aid,report,cname,mail) values('"+rid+"','"+aid+"','"+filename+"','"+cname+"','"+mail+"')")
        
        conn.commit()
        return redirect('reportsuccess')
    else:
        return render(request,'uploadreportfile.html')



def reportsuccess(request):
    return render(request,'reportsuccess.html')



def sendreports(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from billings where report IS NOT NULL and reportsent='0'")
    result= query.fetchall()
    bills=[]
    for row in result:
        s=bill()
        s.sid=row[0]
        s.rid=row[1]
        s.aid=row[2]
        s.cname=row[3]
        s.cdate=row[4]
        s.dob=row[5]
        s.age=row[6]
        s.fname=row[7]
        s.mname=row[8]
        s.phone=row[9]
        s.mail=row[10]
        s.room=row[12]
        s.docfee=row[11]
        s.medcost=row[13]
        s.charges=row[14]
        s.vaccost=row[15]
        s.total=row[16]
        s.ddate=row[17]
        s.billfile=row[18]
        s.vacbill=row[19]
        s.report=row[20]
        s.vacreport=row[21]
        s.print=row[22]
        s.printvac=row[23]
        s.mailsent=row[24]
        s.reportsent=row[25]
        s.vacid=row[26]
        s.vacname=row[27]
        s.vacmailsent=row[28]

        bills.append(s) 
    return render(request,'sendreports.html',{"bills":bills})#{ key:list}



def emailcompose2(request,sid):
    conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="hospital"
    )
    mycursor =conn.cursor()
    mycursor.execute("update billings set reportsent='1' where sid='"+sid+"'")
    conn.commit()
    mycursor.execute("select * from billings where sid='"+sid+"'")
    # get email id and file name of the customer using sid
    #select mail, billfile from billings where sid=sid
    result=mycursor.fetchone()
    if(result!=None):
        customeremail= result[10]  #str(result[0])
        filename = result[20] #result[1]

        BASE_DIR = Path(__file__).resolve().parent.parent
        fromaddr = "madhumithauppala@gmail.com"
        toaddr = customeremail
        
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        # storing the senders email address  
        msg['From'] = fromaddr
        
        # storing the receivers email address 
        msg['To'] = toaddr
        
        # storing the subject 
        msg['Subject'] = "Rammohan Children's Hospital"
        
        # string to store the body of the mail
        body = "Hi, Please check the hospital report"
        
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        filepath=str(BASE_DIR)+"\\media\\"+filename
        print(filepath)
        # open the file to be sent 
        attachment = open(filepath, "rb")
        
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        
        # encode into base64
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(fromaddr, "iqnluwqzranptqee")
        
        # Converts the Multipart msg into a string
        text = msg.as_string()
        
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        
        # terminating the session
        s.quit()
        return render(request, 'email-compose2.html')
    else:
        return render(request, 'sendreports.html')



def managestatus(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        rid=request.POST['rid'] 
        aid=request.POST['aid']
        
        mycursor.execute("update registration set status='1' where rid='"+rid+"' and selecttype='0' and aid='"+aid+"'")
        conn.commit()
        return redirect('successfull')
    else:
        return render(request,'managestatus.html')
    
def successfull(request):
    return render(request,'successfull.html')


def inpatient(request):
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        mycursor.execute("select * from registration where status='1' and selecttype='0' and dis='0'")
        result5=mycursor.fetchall()
        patients=[]
        for row in result5:
            s=revisit()
            s.id=row[0]
            s.cname=row[1]
            s.dob=row[2]
            s.age=row[3]
            s.gender=row[4]
            s.cbloodgrp=row[5]
            s.fname=row[6]
            s.faadhno=row[7]
            s.mname=row[8]
            s.maadhno=row[9]
            s.phone=row[10]
            s.mail=row[11]
            s.address=row[12]
            s.selecttype=row[13]
            s.rid=row[14]
            s.status=row[15]
            s.aid=row[16]
            s.vacid=row[17]
            s.vacname=row[18]
            s.cdate=row[19]
            s.billissue=row[20]
            s.vreportissue=row[21]
            patients.append(s) 
        return render(request,'inpatientdisplay.html',{"patient":patients})


def inpatientdisplay(request):
    return render(request,'inpatientdisplay.html')

def outpatient(request):
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        mycursor.execute("select * from registration where status='0' and selecttype='0'")
        result4=mycursor.fetchall()
        patients=[]
        for row in result4:
            s=revisit()
            s.id=row[0]
            s.cname=row[1]
            s.dob=row[2]
            s.age=row[3]
            s.gender=row[4]
            s.cbloodgrp=row[5]
            s.fname=row[6]
            s.faadhno=row[7]
            s.mname=row[8]
            s.maadhno=row[9]
            s.phone=row[10]
            s.mail=row[11]
            s.address=row[12]
            s.selecttype=row[13]
            s.rid=row[14]
            s.status=row[15]
            s.aid=row[16]
            s.vacid=row[17]
            s.vacname=row[18]
            s.cdate=row[19]
            s.billissue=row[20]
            s.vreportissue=row[21]
            patients.append(s) 
        return render(request,'outpatientdisplay.html',{"patient":patients})
    
def outpatientdisplay(request):
    return render(request,'outpatientdisplay.html')



def date1(request):
    return render(request,'date1.html')
def datefetch(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        d=request.POST['d']
        mycursor.execute("select * from registration where cdate='"+d+"' ")
        result=mycursor.fetchall()
        patients=[]
        for row in result:
            s=revisit()
            s.id=row[0]
            s.cname=row[1]
            s.dob=row[2]
            s.age=row[3]
            s.gender=row[4]
            s.cbloodgrp=row[5]
            s.fname=row[6]
            s.faadhno=row[7]
            s.mname=row[8]
            s.maadhno=row[9]
            s.phone=row[10]
            s.mail=row[11]
            s.address=row[12]
            s.selecttype=row[13]
            s.rid=row[14]
            s.status=row[15]
            s.aid=row[16]
            s.vacid=row[17]
            s.vacname=row[18]
            s.cdate=row[19]
            s.billissue=row[20]
            s.vreportissue=row[21]
            patients.append(s) 
        return render(request,'datefetch.html',{"patient":patients})
    else:
        return render(request,'date.html')



def todate(request):
    return render(request,'todate.html')
def fromdate(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        df=request.POST['d']
        dt=request.POST['dt']

        mycursor.execute("select * from registration where cdate between '"+df+"' and '"+dt+"' ")
        result=mycursor.fetchall()
        patients=[]
        for row in result:
           s=revisit()
           s.id=row[0]
           s.cname=row[1]
           s.dob=row[2]
           s.age=row[3]
           s.gender=row[4]
           s.cbloodgrp=row[5]
           s.fname=row[6]
           s.faadhno=row[7]
           s.mname=row[8]
           s.maadhno=row[9]
           s.phone=row[10]
           s.mail=row[11]
           s.address=row[12]
           s.selecttype=row[13]
           s.rid=row[14]
           s.status=row[15]
           s.aid=row[16]
           s.vacid=row[17]
           s.vacname=row[18]
           s.cdate=row[19]
           s.billissue=row[20]
           s.vreportissue=row[21]
           patients.append(s) 
        return render(request,'displaydatedetails.html',{"patient":patients})
    else:
        return render(request,'todate.html')  
def displaydatedetails(request):
    return render(request,'displaydatedetails.html')



def single(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospital"
        ) 
        mycursor =conn.cursor()
        rid=request.POST['rid'] 
        #mycursor.execute("select distinct cname, dob, age, gender, cbloodgrp, fname, faadhno, mname, maadhno, phone, mail, address, selecttype, rid, status from registration  where rid='"+rid+"'")
        mycursor.execute("SELECT DISTINCT cname, dob, age, gender, cbloodgrp, fname, faadhno, mname, maadhno, phone, mail, address, selecttype, rid, status FROM registration WHERE rid = '" + rid + "'")

        result7=mycursor.fetchall()
        patients=[]
        for row in result7:
            s=revisit()
            s.rid=row[13]
            s.cname=row[0]
            s.dob=row[1]
            s.cbloodgrp=row[4]
            s.faadhno=row[6]
            s.mname=row[7]
            s.maadhno=row[8]
            s.selecttype=row[12]
            s.status=row[14]
            s.age=row[2]
            s.gender=row[3]
            s.fname=row[5]
           
            s.address=row[11]
            s.phone=row[9]
            s.mail=row[10]
            

            patients.append(s)
        return render(request,'singledetails.html',{"patient":patients})#{ key:list} 
    else:
        return render(request,'ridwise.html')
def singledetails(request):
    return render(request,'singledetails.html')
def ridwise(request):
    return render(request,'ridwise.html')


def datein(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        d=request.POST['d']
        mycursor.execute("select * from registration where cdate='"+d+"' and status='1' ")
        result=mycursor.fetchall()
        patients=[]
        for row in result:
            s=revisit()
            s.id=row[0]
            s.cname=row[1]
            s.dob=row[2]
            s.age=row[3]
            s.gender=row[4]
            s.cbloodgrp=row[5]
            s.fname=row[6]
            s.faadhno=row[7]
            s.mname=row[8]
            s.maadhno=row[9]
            s.phone=row[10]
            s.mail=row[11]
            s.address=row[12]
            s.selecttype=row[13]
            s.rid=row[14]
            s.status=row[15]
            s.aid=row[16]
            s.vacid=row[17]
            s.vacname=row[18]
            s.cdate=row[19]
            s.billissue=row[20]
            s.vreportissue=row[21]
            patients.append(s) 
        return render(request,'dataindetails.html',{"patient":patients})
    else:
         return render(request,'datewisein.html')

def dataindetails(request):
    return render(request,'dataindetails.html')
def datewisein(request):
    return render(request,'datewisein.html')

def datewiseout(request):
    return render(request,'datewiseout.html')
def dateout(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        mycursor =conn.cursor()
        d=request.POST['d']
        mycursor.execute("select * from registration where cdate='"+d+"' and status='0' ")
        result=mycursor.fetchall()
        patients=[]
        for row in result:
            s=revisit()
            s.id=row[0]
            s.cname=row[1]
            s.dob=row[2]
            s.age=row[3]
            s.gender=row[4]
            s.cbloodgrp=row[5]
            s.fname=row[6]
            s.faadhno=row[7]
            s.mname=row[8]
            s.maadhno=row[9]
            s.phone=row[10]
            s.mail=row[11]
            s.address=row[12]
            s.selecttype=row[13]
            s.rid=row[14]
            s.status=row[15]
            s.aid=row[16]
            s.vacid=row[17]
            s.vacname=row[18]
            s.cdate=row[19]
            s.billissue=row[20]
            s.vreportissue=row[21]
            patients.append(s) 
        return render(request,'dataoutdetails.html',{"patient":patients})
    else:
        return render(request,'datewiseout.html')
def dataoutdetails(request):
    return render(request,'dataoutdetails.html')


def managejob(request):
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'hospital'
    )
    query = conn.cursor()
    query.execute("select * from jobs")
    result= query.fetchall()
    j=[]
    for row in result:
        s=jobadd()
        s.jid=row[0]
        s.jname=row[1]
        j.append(s)  
    return render(request,'managejob.html',{"jobs":j})#{ key:list}




def addjob(request):
    return render(request,'addjob.html')


def jobadding(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(

            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        mycursor =conn.cursor()
        d=request.POST['jobname']
        mycursor.execute("insert into jobs(jname)values('"+d+"') ")
        conn.commit()
        return render(request,'addsuccessjob.html')

def addsuccessjob(request):
    return render(request,'addsuccessjob.html')




def editjob(request,jid):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        
        
        j= request.POST['jobname']
        query.execute("update jobs set jname='"+j+"' where jid='"+jid+"' ")
        conn.commit()
        return render(request, 'jobedittedsuccessfull.html')
    
    else:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        query.execute("select * from jobs where jid='"+jid+"' ")
        result= query.fetchall()
        j=[]
        for row in result:
            s=jobadd()
            s.jid=row[0]
            s.jname=row[1]
            j.append(s)  
        return render(request,'editjob.html',{"jobs":j})




def jobedittedsuccessfull(request):
    return render(request,'jobedittedsuccessfull.html')


def deljob(request,jid):

    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'hospital'
    )
    query = conn.cursor()
    query.execute("DELETE FROM jobs where jid='"+jid+"'")
    conn.commit()
    
    return render(request,'jobdelsuccessfull.html')
 
def jobdelsuccessfull(request):
    return render(request,'jobdelsuccessfull.html')
#def uploadfile(request):
#    return render(request,'uploadfile.html')
    


def uploadvacreport(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="hospital"
        )
        #filename='xyz.png'
        mycursor =conn.cursor()
        rid=request.POST['rid']
        cname=request.POST['cname']
        aid=request.POST['aid']
        mail=request.POST['mail']
        


        mycursor.execute("update billings set vacreport='"+filename+"', cname='"+cname+"', mail='"+mail+"' where rid='"+rid+"' and aid='"+aid+"'")
        
        conn.commit()
        return redirect('reportvacsuccesful')
    else:
        return render(request,'uploadvacreport.html')





def reportvacsuccesful(request):
    return render(request,'reportvacsuccesful.html')





def patientvacdis(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from registration where billissue='0' and selecttype='1'")
    result= query.fetchall()
    vacpatients=[]
    for row in result:
        s=revisit()
        s.id=row[0]
        s.cname=row[1]
        s.dob=row[2]
        s.age=row[3]
        s.gender=row[4]
        s.cbloodgrp=row[5]
        s.fname=row[6]
        s.faadhno=row[7]
        s.mname=row[8]
        s.maadhno=row[9]
        s.phone=row[10]
        s.mail=row[11]
        s.address=row[12]
        s.selecttype=row[13]
        s.rid=row[14]
        s.status=row[15]
        s.aid=row[16]
        s.vacid=row[17]
        s.vacname=row[18]
        s.cdate=row[19]
        s.billissue=row[20]
        s.vreportissue=row[21]
        vacpatients.append(s)  
    return render(request,'patientvacdis.html',{"vacpatient":vacpatients})#{ key:list}



def generatevacbills(request,id):
    if request.method=='POST':
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
        query = conn.cursor()
        
        rid = request.POST['rid']
        aid = request.POST['aid']
        cname = request.POST['cname']
        #datetime_str = str(request.POST['cdate'])
        cdate = request.POST['cdate']
        dob=request.POST['dob']
        age=request.POST['age']
        fname = request.POST['fname']
        mname = request.POST['mname']
        phone = request.POST['phone']
        mail = request.POST['mail']
        vacid = request.POST['vacid']
        vacname = request.POST['vacname']
        vaccost = request.POST['vaccost']
        total=request.POST['total']
        today=date.today()
        ddate=str(today)
        query.execute("update registration set billissue='1' where id='"+id+"'")
        query.execute("insert into billings(rid,aid,cname,cdate,dob,age,fname,mname,phone,mail,vacid,vacname,vaccost,total,ddate,printvac) values('"+rid+"','"+aid+"','"+cname+"','"+cdate+"','"+dob+"','"+age+"','"+fname+"','"+mname+"','"+phone+"','"+mail+"','"+vacid+"','"+vacname+"','"+vaccost+"','"+total+"','"+ddate+"','0')")
        conn.commit()
        return redirect('printvacdis')
        
    else:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    
    query.execute("select * from registration where id='"+id+"'")
    result= query.fetchall()
    patients=[]
    for row in result:
        s=revisit()
        s.id=row[0]
        s.cname=row[1]
        s.dob=row[2]
        s.age=row[3]
        s.gender=row[4]
        s.cbloodgrp=row[5]
        s.fname=row[6]
        s.faadhno=row[7]
        s.mname=row[8]
        s.maadhno=row[9]
        s.phone=row[10]
        s.mail=row[11]
        s.address=row[12]
        s.selecttype=row[13]
        s.rid=row[14]
        s.status=row[15]
        s.aid=row[16]
        s.vacid=row[17]
        s.vacname=row[18]
        s.cdate=row[19]
        s.billissue=row[20]
        s.vreportissue=row[21]

        patients.append(s)  
    return render(request,'generatevacbills.html',{"patient":patients})#{ key:list}
    


def printvacdis(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from billings where printvac='0'")
    result= query.fetchall()
    vacpatients=[]
    for row in result:
       s=bill()
       s.sid=row[0]
       s.rid=row[1]
       s.aid=row[2]
       s.cname=row[3]
       s.cdate=row[4]
       s.dob=row[5]
       s.age=row[6]
       s.fname=row[7]
       s.mname=row[8]
       s.phone=row[9]
       s.mail=row[10]
       s.room=row[12]
       s.docfee=row[11]
       s.medcost=row[13]
       s.charges=row[14]
       s.vaccost=row[15]
       s.total=row[16]
       s.ddate=row[17]
       s.billfile=row[18]
       s.vacbill=row[19]
       s.report=row[20]
       s.vacreport=row[21]
       s.print=row[22]
       s.printvac=row[23]
       s.mailsent=row[24]
       s.reportsent=row[25]
       s.vacid=row[26]
       s.vacname=row[27]
       s.vacmailsent=row[28]

       vacpatients.append(s)  
    return render(request,'printvacdis.html',{"vacpatient":vacpatients})





def print_vacbills(request,sid):
   
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    print('hi')
    query.execute("update billings set printvac='1' where sid='"+sid+"'")
    conn.commit()
    query.execute("select * from billings where sid='"+sid+"'")
    result= query.fetchall()
    inpatients=[]
    for row in result:
        s=bill()
        s.sid=row[0]
        s.rid=row[1]
        s.aid=row[2]
        s.cname=row[3]
        s.cdate=row[4]
        s.dob=row[5]
        s.age=row[6]
        s.fname=row[7]
        s.mname=row[8]
        s.phone=row[9]
        s.mail=row[10]
        s.room=row[12]
        s.docfee=row[11]
        s.medcost=row[13]
        s.charges=row[14]
        s.vaccost=row[15]
        s.total=row[16]
        s.ddate=row[17]
        s.billfile=row[18]
        s.vacbill=row[19]
        s.report=row[20]
        s.vacreport=row[21]
        s.print=row[22]
        s.printvac=row[23]
        s.mailsent=row[24]
        s.reportsent=row[25]
        s.vacid=row[26]
        s.vacname=row[27]
        s.vacmailsent=row[28]
        
        inpatients.append(s)  
    return render(request,'print_vacbills.html',{"inpatient":inpatients})
        

def vacreportdis(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from registration where vreportissue='0' and selecttype='1'")
    result= query.fetchall()
    vacpatients=[]
    for row in result:
        s=revisit()
        s.id=row[0]
        s.cname=row[1]
        s.dob=row[2]
        s.age=row[3]
        s.gender=row[4]
        s.cbloodgrp=row[5]
        s.fname=row[6]
        s.faadhno=row[7]
        s.mname=row[8]
        s.maadhno=row[9]
        s.phone=row[10]
        s.mail=row[11]
        s.address=row[12]
        s.selecttype=row[13]
        s.rid=row[14]
        s.status=row[15]
        s.aid=row[16]
        s.vacid=row[17]
        s.vacname=row[18]
        s.cdate=row[19]
        s.billissue=row[20]
        s.vreportissue=row[21]
        vacpatients.append(s)  
    return render(request,'vacreportdis.html',{"vacpatient":vacpatients})#{ key:list}




def printvacreport(request,id,rid,aid):
   
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    print('hi')
    query.execute("update registration set vreportissue='1' where id='"+id+"'")
    conn.commit()
    query.execute("insert into billings(printvac,rid,aid) values('1','"+rid+"','"+aid+"')")

    conn.commit()
    query.execute("select * from registration where id='"+id+"'")
    result= query.fetchall()
    inpatients=[]
    for row in result:
        s=revisit()
        s.id=row[0]
        s.cname=row[1]
        s.dob=row[2]
        s.age=row[3]
        s.gender=row[4]
        s.cbloodgrp=row[5]
        s.fname=row[6]
        s.faadhno=row[7]
        s.mname=row[8]
        s.maadhno=row[9]
        s.phone=row[10]
        s.mail=row[11]
        s.address=row[12]
        s.selecttype=row[13]
        s.rid=row[14]
        s.status=row[15]
        s.aid=row[16]
        s.vacid=row[17]
        s.vacname=row[18]
        s.cdate=row[19]
        s.billissue=row[20]
        s.vreportissue=row[21]
        inpatients.append(s)  
    return render(request,'printvacreport.html',{"inpatient":inpatients})
        
def removeuser(request,id,rid,aid):
   
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    print('hi')
    query.execute("update registration set vreportissue='1' where id='"+id+"'")
    conn.commit()
    query.execute("update billings set printvac='1' where rid='"+rid+"' and aid='"+aid+"'")
    conn.commit()
     
    return redirect('vacreportdis')
        


def sendvacreport(request):
    conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'hospital'
        )
    query = conn.cursor()
    query.execute("select * from billings where vacreport IS NOT NULL and reportsent='0'")
    result= query.fetchall()
    bills=[]
    for row in result:
        s=bill()
        s.sid=row[0]
        s.rid=row[1]
        s.aid=row[2]
        s.cname=row[3]
        s.cdate=row[4]
        s.dob=row[5]
        s.age=row[6]
        s.fname=row[7]
        s.mname=row[8]
        s.phone=row[9]
        s.mail=row[10]
        s.room=row[12]
        s.docfee=row[11]
        s.medcost=row[13]
        s.charges=row[14]
        s.vaccost=row[15]
        s.total=row[16]
        s.ddate=row[17]
        s.billfile=row[18]
        s.vacbill=row[19]
        s.report=row[20]
        s.vacreport=row[21]
        s.print=row[22]
        s.printvac=row[23]
        s.mailsent=row[24]
        s.reportsent=row[25]
        s.vacid=row[26]
        s.vacname=row[27]
        s.vacmailsent=row[28]

        bills.append(s) 
    return render(request,'sendvacreport.html',{"bills":bills})#{ key:list}





def email_composevac2(request,sid):
    conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="hospital"
    )
    mycursor =conn.cursor()
    mycursor.execute("update billings set reportsent='1' where sid='"+sid+"'")
    conn.commit()
    mycursor.execute("select * from billings where sid='"+sid+"'")
    # get email id and file name of the customer using sid
    #select mail, billfile from billings where sid=sid
    result=mycursor.fetchone()
    if(result!=None):
        customeremail= result[10]  #str(result[0])
        filename = result[21] #result[1]

        BASE_DIR = Path(__file__).resolve().parent.parent
        fromaddr = "madhumithauppala@gmail.com"
        toaddr = customeremail
        
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        
        # storing the senders email address  
        msg['From'] = fromaddr
        
        # storing the receivers email address 
        msg['To'] = toaddr
        
        # storing the subject 
        msg['Subject'] = "Rammohan Children's Hospital"
        
        # string to store the body of the mail
        body = "Hi, Please check the vaccination report"
        
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        filepath=str(BASE_DIR)+"\\media\\"+filename
        print(filepath)
        # open the file to be sent 
        attachment = open(filepath, "rb")
        
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        
        # encode into base64
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login(fromaddr, "iqnluwqzranptqee")
        
        # Converts the Multipart msg into a string
        text = msg.as_string()
        
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        
        # terminating the session
        s.quit()
        return render(request, 'email_composevac2.html')
    else:
        return render(request, 'sendvacreport.html')

#def register(request):
    
    
# Create your views here.