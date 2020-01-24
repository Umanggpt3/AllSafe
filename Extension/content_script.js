let text = document.body.innerText;
console.log(text);
console.log(typeof text);

console.log(document.body.innerHTML);
let body_doc = document.body.innerHTML;

// let text_string = "html_text=" + JSON.jsonify({
//     html_text: text,
//     body_doc: body_doc
// });
let json_data = {
    abc : text,
    def : body_doc
}
let xhr = new XMLHttpRequest();
let theUrl = "http://127.0.0.1:8000/testing/";
xhr.open("POST", theUrl, true);

xhr.onreadystatechange = function() {
    if (xhr.readyState == 4){
        console.log("Entered");
    }
    else{
        console.log("Not Entered");
    }
};
xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
xhr.send(JSON.stringify(json_data));