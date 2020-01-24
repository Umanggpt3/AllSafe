let text = document.body.innerText;
console.log(text);
console.log(typeof text);

let text_string = "html_doc = " + text;
let xhr = new XMLHttpRequest();
let theUrl = "http://127.0.0.1:8000/testing/";
xhr.open("POST", theUrl, true);

xhr.onreadystatechange = function() {
    if (xhr.readyState == 4){
        alert("Entered");
    }
    else{
        alert("Not Entered");
    }
};
xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
xhr.send(text_string);