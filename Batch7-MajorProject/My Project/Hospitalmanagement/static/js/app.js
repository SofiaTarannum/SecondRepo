
var gender;
var specialization = [];
function validateapp()
{
    var cname = document.appform.cname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(cname == "") 
    {
        
        alert("please enter your name");
        return false;
    }
    if(re.test(cname)==false)
    {
       alert("name of the applicant should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
    //-------------------------
    var fname = document.appform.fname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(fname == "") 
    {
        
        alert("please enter your father name");
        return false;
    }
    if(re.test(fname)==false)
    {
       alert("name of the father should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
//-----------------------------------------
    var mname = document.appform.mname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(mname == "") 
    {
        
        alert("please enter your mother name");
        return false;
    }
    if(re.test(mname)==false)
    {
       alert("name of the mother should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
//----------------------------------








    
}
 



