var input = document.getElementById("venttext");


input.addEventListener("keyup", function(event)
{
    if(event.keyCode === 13)
    {
        event.preventDefault();
        document.getElementById("ventBtn").click();
    }
})

document.addEventListener('mouseout', e => {
    if (!e.toElement && !e.relatedTarget) {
        document.querySelector('.exit-intent-popup').classList.add('visible'); 
    }
});
