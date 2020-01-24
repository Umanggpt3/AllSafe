let checkbox = document.getElementById('turnOnOff');
chrome.storage.local.get(['onOffkey'], function (result) {
    if (result.onOffkey == 1) {
        checkbox.checked = true;
    } else {
        checkbox.checked = false;
    }
});

console.log(checkbox.checked);
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('turnOnOff').addEventListener('change', function() {
        console.log("Kuch to hai");
        if (document.getElementById('turnOnOff').checked) {
            chrome.storage.local.set({onOffkey: 1}, function(){
                console.log("Doing It's Magic!");
            });
            console.log("hello");
        } else {
            chrome.storage.local.set({onOffkey: 0}, function () {
                console.log("Not Doing It's Magic!");
            });
        }
    });
});