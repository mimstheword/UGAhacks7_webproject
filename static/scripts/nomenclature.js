function buttonErase() {


    //stores input value in a variable
    var hold = document.getElementById("venttext").value;
    //var hold = "test";
    //Empties input field
    document.getElementById('venttext').value = ' ';
    console.log(hold);

    $.ajax({
        type: "POST",
        url: "/parse_data",
        data: JSON.stringify(hold),
        contentType: 'application/json',
        success: function(data){
            document.getElementById("venttext").value = data.Category[0];
            console.log(data)
        }
    });
}