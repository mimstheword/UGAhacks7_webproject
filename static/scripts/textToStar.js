var canvas = document.querySelector('canvas');
var c = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.hight = window.innerHeight;


c.beginPath();
c.fillStyle = "#FFFFFF";
c.fillRect(5,5,5,5);
c.fillRect(150,5,5,5,);
c.closePath();