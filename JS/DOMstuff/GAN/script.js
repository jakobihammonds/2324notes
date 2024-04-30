//imports

//global variables or object
var winloseLBL = document.getElementById("winlose");   //finds by id
var winnerImg = document.querySelector(".winimg");     //finds by class/tag/id/by anything in your html... kind of
var bod = document.querySelector("body");
var pTag = document.querySelector("p");






//functions
function isNumeric(num) {
     return !isNaN(parseFloat(num) && isFinite(num))
}

//events
document.getElementById("start").onclick = function(){
     console.log("let's start the game");
     var range = ""
     while (!isNumeric(range)) {
          var range = parseInt(prompt("Set boundaries zero to ...?"))
     }
     //computer will pick a number
     const ANS = Math.floor(Math.random() * range +1);
     console.log(ANS);

     while(guess!=ANS){
          var guess = ""
          while (!isNumeric(guess)) {
               //                          tickMark string ${variable} tickMark
               var guess = parseInt(prompt(`guess a number between 0 and ${range}`))
          }

          if(guess==ANS){
               winloseLBL.innerHTML="Hurray you got it!"
               winnerImg.style.display="block"; //visibility
               bod.style.backgroundColor="green";
               pTag.style.backgroundColor="red";
          }
          else if (guess < ANS) {
               alert("Guess higher!")
               bod.style.backgroundColor = "red"
           }
           else {
               alert("Guess lower!")
               bod.style.backgroundColor = "blue"
           }

     }

}

//mainloop if necessary
