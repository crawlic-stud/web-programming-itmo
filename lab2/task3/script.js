function getUrls() {
    var inputs = document.querySelectorAll('input[name^="url"]');
    var urls = [];
    for (let i of inputs) {
        urls.push(i.value);
    }
    return urls;
}

function showUrl(url) {
    var frame = document.getElementById("frame");
    frame.hidden = false;
    frame.src = url;
}

function slideshow() {
    var urls = getUrls();
    var interval = parseInt(document.getElementById("interval").value);
    function showNextUrl() {
        if (urls.length > 0) {
            showUrl(urls.shift());
            setTimeout(showNextUrl, interval * 1000);
        }
    }
    showNextUrl();
}