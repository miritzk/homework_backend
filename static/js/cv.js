var fullname = "Mirit Zelichonok"
console.log(fullname); // console

function checkEmail() {
    const email = document.getElementById("email");
    if (!email.checkValidity()) {
        document.getElementById("error_msg").innerHTML = email.validationMessage;
    } 
    else {
        document.getElementById("error_msg").innerHTML = "";
    }
}