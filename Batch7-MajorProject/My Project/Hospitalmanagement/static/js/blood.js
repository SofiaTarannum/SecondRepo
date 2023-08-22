var gender;
var specialization = [];

function bloodvalidation()
{
    var a=document.bloodform.dname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(a == "") 
    {
        
        alert("please enter your Donar name");
        return false;
    }
    if(re.test(a)==false)
    {
        alert("name of the Donar should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
    var b=document.bloodform.daadhar.value;
    if(b == "")
    {
        alert("please enter your aadhar number");
        return false;

    }
    var c=document.bloodform.email.value;
    if(c == "")
    {
        alert("please enter your email");
        return false;

    }
    var d=document.bloodform.pnum.value;
    if(d == "")
    {
        alert("please enter your mobile number");
        return false;
    }
    var e=document.bloodform.bgroup.value;
    if(e == "")
    {
        alert("please enter your Blood group");
        return false;
    }
    var f=document.bloodform.age.value;
    if(f == "")
    {
        alert("please enter your Age");
        return false;
    }
    var g=document.bloodform.dob.value;
    if(g == "")
    {
        alert("please enter your Date of Birth");
        return false;
    }
    gender = document.querySelector('input[name="gender"]:checked');
    if (gender === null)
    {
        alert("Gender required!");
        return false;
    }
 return true;









    






}