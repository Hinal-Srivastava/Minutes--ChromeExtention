function copytext() {

    let summarytext = document.getElementById("summary");
    summarytext.select();
    document.execCommand("copy")
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied Summary " ;
}

function outFunc() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Click to Copy";
}

document.getElementById("copyButton").addEventListener("click", copytext); 
document.getElementById("copyButton").addEventListener("onmouseout", outFunc); 

const useraction = async () => {
    const response = await fetch('http://127.0.0.1:8000/summarizer?youtube_video=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQr4QMBUPxWo', {
        method: 'GET',
        mode: "no-cors",
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin' : '*'
        }
    });
    const myJson = await response.json();
    console.log(myJson);
}


document.getElementById("hugtextButton").addEventListener("click", useraction);
