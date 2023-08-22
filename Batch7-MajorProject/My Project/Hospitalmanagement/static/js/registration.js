function registationvalidation()
{
    var a=document.registrationform.cname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(a == "") 
    {
        
        alert("please enter your Child name");
        return false;
    }
    if(re.test(a)==false)
    {
        alert("name of the Child should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
    var g=document.registrationform.dob.value;
    if(g == "")
    {
        alert("please enter your Date of Birth");
        return false;
    }
    var f=document.registraionform.age.value;
    if(f == "")
    {
        alert("please enter your Age");
        return false;
    }
    var z=document.registrationform.fname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(z == "") 
    {
        
        alert("please enter your Father name");
        return false;
    }
    if(re.test(z)==false)
    {
        alert("name of the Father should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
    var w=document.registrationform.faadhar.value;
    if(w == "")
    {
        alert("please enter your  Father aadhar number");
        return false;

    }
    var x=document.registrationform.mname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(x == "") 
    {
        
        alert("please enter your Mother name");
        return false;
    }
    if(re.test(x)==false)
    {
        alert("name of the Mother should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
    var v=document.registrationform.maadhar.value;
    if(v == "")
    {
        alert("please enter your  Mother aadhar number");
        return false;

    }
    var q=document.registrationform.phone.value;
    if(q == "")
    {
        alert("please enter your mobile number");
        return false;
    }
    var p=document.registrationform.email.value;
    if(p == "")
    {
        alert("please enter your email");
        return false;
    }
    var address = document.registrationform.message.value;
    if (address == "") 
    {
        alert("please enter your address details");
        
        return false;
    }
    
  return true;






}