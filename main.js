function copytext() {

    let summary = document.querySelector("#summary");
    summary.select();
    summary.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(summary.value);
    //alert("Copied Text");
}