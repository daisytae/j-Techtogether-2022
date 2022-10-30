var  hydrationImage;
var plasticImage; 

const hydrationList = document.getElementsByClassName("hydration");
hydrationImage = hydrationList[0];
hydrationImage.addEventListener("click", myFunction);

function myFunction() {
    console.log("Hi");
    document.getElementById("hydration").innerHTML = "location.href='hydration.html'";
}




