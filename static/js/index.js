var button1 =document.getElementById("register");
var button2 =document.getElementById("change_password");
const login = document.getElementById("login");
const logout= document.getElementById("logout");
var del = document.getElementById("del");
button1.addEventListener("click", function(){
    window.location.href=location+"register";
})

button2.addEventListener("click", function(){
    window.location.href=location+"change";
})

login.addEventListener("click",function(){
    window.location.href=location+"login";
})

logout.addEventListener("click",function(){
    window.location.href=location+"logout";
})

del.addEventListener("click",function(){
    window.location.href=location+"delete";
})