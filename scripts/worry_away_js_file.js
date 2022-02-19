var input = document.getElementById("venttext");


input.addEventListener("keyup", function(event)
{
    if(event.keyCode === 13)
    {
        event.preventDefault();
        document.getElementById("ventBtn").click();
    }
})

function popFunction()
{
    var popScreen = document.getElementById("popTest");
    popScreen.classList.toggle("show")
}
