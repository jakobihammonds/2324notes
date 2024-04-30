console.log("hi");

var stud1 = document.getElementById("student-1");
//welcome to lambda functions...  Google it
stud1.addEventListener("click",() => {
     stud1.style.backgroundColor="pink";
})

var stud2 = document.getElementById("student-2");
//welcome to lambda functions...  Google it
stud2.addEventListener("click",() => {
     stud2.style.backgroundColor="orange";
})

var stud3 = document.getElementById("student-3");
//welcome to lambda functions...  Google it
stud3.addEventListener("click",() => {
     if(stud3.style.backgroundColor=="green"){
          stud3.style.backgroundColor="#FFFFFF"
     }else{
          stud3.style.backgroundColor="green";
     }
})