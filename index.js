document.getElementById("summaryze").addEventListener("click", function(){
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs) {
        let url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/", true);
        xhr.send(url);
    })
}) 