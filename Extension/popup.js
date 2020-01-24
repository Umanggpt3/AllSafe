let checkbox = document.getElementById('turnOnOff');
console.log(checkbox.checked);
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('turnOnOff').addEventListener('change', function() {
        console.log("Kuch to hai");
        if (document.getElementById('turnOnOff').checked) {
            //chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
                // chrome.tabs.sendMessage(tabs[0].id, {turnOnOff: "On"}, function(response) {
                //   //console.log(response.farewell);
                // });
                chrome.storage.local.set({key: 1}, function(){
                    console.log("Doing It's Magic!");
                });
                console.log("hello");
            //});
        } else {
            // chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
                // chrome.tabs.sendMessage(tabs[0].id, {turnOnOff: "Off"}, function(response) {
                //   //console.log(response.farewell);
                // });
                chrome.storage.local.set({key: 0}, function () {
                    console.log("Not Doing It's Magic!");
                });
            //});
        }
    });
});