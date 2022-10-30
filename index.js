var  hydrationImage;
var plasticImage; 

const hydrationList = document.getElementsByClassName("hydration");
hydrationImage = hydrationList[0];
hydrationImage.addEventListener("click", myFunction);

function myFunction() {
    console.log("Hi");
 
}

const plasticList = document.getElementsByClassName("plastic");
plasticImage = plasticList[0];
plasticImage.addEventListener("click", wyFunction);

function wyFunction() { 
    console.log("bye");
}



