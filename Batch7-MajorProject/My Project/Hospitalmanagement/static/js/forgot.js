function validateforgot()
{
    var c=document.forgot.email.value;
    if(c == "")
    {
        alert("please enter your email");
        return false;

    }
}