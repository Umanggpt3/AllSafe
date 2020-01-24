let bulleyKeyVar = 0;
chrome.storage.local.get(['onOffkey'], function (result) {
    //console.log("Value currently is " + result.key);
    chrome.storage.local.get(['bullykey'], function (result_t) {
        if (result.onOffkey == 1) {
            if (result_t.bullykey == 1) {
                console.log("bully");
                bulleyKeyVar = 1;

                let text = document.body.innerText;
                let body_doc = document.documentElement.innerHTML;
                let json_data = {
                    body_text: text,
                    body_html: body_doc,
                    flag: 1,
                };
                let xhr = new XMLHttpRequest();
                theUrl = "http://127.0.0.1:8000/testing/offensive/";



                xhr.open("POST", theUrl, true);
                let r;
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == 4 && this.status == 200) {
                        console.log("Entered");
                        r = this.responseText;
                        // console.log(r);
                        // console.log(typeof r);
                        manipulateDOM(r);
                    } else {
                        console.log("Not Entered");
                    }
                };
                xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                xhr.send(JSON.stringify(json_data));
                function manipulateDOM(changedDOM) {
                    document.open('text/html');
                    document.write(changedDOM);
                    document.close();
                }
            }
                else {

                    let text = document.body.innerText;
                    let body_doc = document.documentElement.innerHTML;
                    let json_data = {
                        body_text: text,
                        body_html: body_doc,
                        flag: 0,
                    };
                    let xhr = new XMLHttpRequest();
                    theUrl = "http://127.0.0.1:8000/testing/offensive/";



                    xhr.open("POST", theUrl, true);
                    let r;
                    xhr.onreadystatechange = function () {
                        if (xhr.readyState == 4 && this.status == 200) {
                            console.log("Entered");
                            r = this.responseText;
                            // console.log(r);
                            // console.log(typeof r);
                            manipulateDOM(r);
                        } else {
                            console.log("Not Entered");
                        }
                    };
                    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                    xhr.send(JSON.stringify(json_data));
                    function manipulateDOM(changedDOM) {
                        document.open('text/html');
                        document.write(changedDOM);
                        document.close();
                    }
                }
            
        }



    });

});