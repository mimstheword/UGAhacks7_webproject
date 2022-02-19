var input = document.getElementById("venttext");

input.addEventListener("keyup", function(en)
{
    if(en.keyCode === 13)
    {
        en.preventDefault();
        document.getElementById("ventBtn").click();
    }
})

