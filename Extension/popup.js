let checkbox = document.getElementById('turnOnOff');
let bullybox = document.getElementById('bully');
document.getElementById("pwdBtn").addEventListener('click',function(){
    pwd  = document.getElementById("pwdBox").value;
    if(pwd=="better"){
        document.getElementById("overlay").style.display="none";
    }

});



chrome.storage.local.get(['onOffkey'], function (result) {
    if (result.onOffkey == 1) {
        checkbox.checked = true;
    } else {
        checkbox.checked = false;
    }
});

chrome.storage.local.get(['bullykey'], function (result) {
    if (result.bullykey == 1) {
        bullybox.checked = true;
    } else {
        bullybox.checked = false;
    }
});

document.addEventListener('DOMContentLoaded', function () {
    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            chrome.storage.local.set({onOffkey: 1}, function(){
                console.log("Doing It's Magic!");
            });
        } else {
            chrome.storage.local.set({onOffkey: 0}, function () {
                console.log("Not Doing It's Magic!");
            });
        }
        location.reload(true);
    });
    bullybox.addEventListener('change', function() {
        if (bullybox.checked) {
            chrome.storage.local.set({bullykey: 1}, function(){
                console.log("Doing It's Magic!");
            });
        } else {
            chrome.storage.local.set({bullykey: 0}, function () {
                console.log("Not Doing It's Magic!");
            });
        }
    });
});