function validatelogin()
{
    var c=document.adminform.mail.value;
    if(c == "")
    {
        alert("please enter your email");
        return false;

    }
    var d=document.adminform.password.value;
    if(d == "")
    {
        alert("please enter your password");
        return false;

    }
}