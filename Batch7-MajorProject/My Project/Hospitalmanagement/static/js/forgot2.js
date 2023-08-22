function validateforgot2()
{
    var c=document.forgot2.email.value;
    if(c == "")
    {
        alert("please enter your email");
        return false;

    }
    var d=document.forgot2.password.value;
    if(d == "")
    {
        alert("please enter your password");
        return false;

    }
    var e=document.forgot2.password1.value;
    if(e!=d)
    {
       
        alert("please provide same password and comfrim password");
        return false;
 
    }
}