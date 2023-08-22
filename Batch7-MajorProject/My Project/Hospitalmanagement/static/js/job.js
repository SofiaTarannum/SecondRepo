///function SaveStudentDetails() {
  // return validateControls();
//}
var gender;
var specialization = [];
function validateControls()
{
    //FirstName
    var aname = document.jobform.aname.value;
    var re = /^[a-zA-Z\s]+$/;
    if(aname == "") 
    {
        
        alert("please enter your name");
        return false;
    }
    if(re.test(aname)==false)
    {
       alert("name of the applicant should be only characters(check whether you have entered special characters or digits) ");
       return false;
    }
    //aadhar
    var aadhar=document.jobform.appaadhar.value;
    if(aadhar == "") 
    {
        
        alert("please enter your aadhar");
        return false;
    }

    var email = document.jobform.email.value;
    if(email== "") 
    {
        alert("please enter your valid email Id");
        //email.focus();
        return false;
    }
      //Mobile
    var mobile = document.jobform.mobile.value;
    if(mobile== "") 
    {

        alert("please enter your mobile number");
        //email.focus();
        return false;
    }
    if(isNaN(mobile))
    {
    alert("contact number should be digits only");
    return false;
    }
    
    //Gender   
    gender = document.querySelector('input[name="gender"]:checked');
    if (gender === null)
    {
        alert("Gender required!");
        //gender.focus();
        return false;
    }
    //Dob
    var dob = document.jobform.dob.value
    if (dob == "") 
    {
        alert("please enter your Date of Birth");
        //dob.focus();
        return false;
    }
    //age
    var age = document.jobform.age.value;
    if (age == "") 
    {
        alert("please enter your age ");
        //address.focus();
        return false;
    }

    //Address
    var address = document.jobform.address.value;
    if (address == "") 
    {
        alert("please enter your address details");
        //address.focus();
        return false;
    }
    

    //City
    var city = document.jobform.city.value;
    var re = /^[a-zA-Z\s]+$/;
    if (city == "") 
    {
        alert("please enter your city");
        return false;
    }
    if (re.test(city)===false)
    {
                alert("city should have only characters(check whether you have entered special characters or digits) ");
        return false;
    }
    
    // Pin
    var pin = document.jobform.pin.value;
    if(isNaN(pin))
    {
     alert("pincode should be digits only");
     return false;
    }
    if (pin == "") 
    {
        alert("please enter your pin");
        //address.focus();
        return false;
    }
    // State
    var state = document.jobform.state.value;
    var re = /^[a-zA-Z\s]+$/;
    if (state== "") 
    {
        alert("please enter your state");
        //address.focus();
        return false;
    }       
    if (re.test(state)===false)
    {
        alert("state name should have only characters(check whether you have entered special characters or digits) ");
        return false;
    }
   
    
    

        return true;
}
 



