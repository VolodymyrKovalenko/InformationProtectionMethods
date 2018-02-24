function onLoad() {var file = document.getElementById("file1").files[0];


var reader = new FileReader();
reader.onload = function (e) {
    var textArea = document.getElementById("myTextArea1");
    textArea.value = e.target.result;
};
reader.readAsText(file);
console.log(file);}

function onLoad2() {var file = document.getElementById("file2").files[0];


var reader = new FileReader();
reader.onload = function (e) {
    var textArea = document.getElementById("myTextArea2");
    textArea.value = e.target.result;
};
reader.readAsText(file);
console.log(file);}


function saveTextAsFile() {
  var textToWrite = document.getElementById('myTextArea2').value;
  console.log(textToWrite.value);
  var textFileAsBlob = new Blob([ textToWrite ], { type: 'text/plain' });
  var fileNameToSaveAs = "saveEncrFile";

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  if (window.webkitURL != null) {
    // Chrome allows the link to be clicked without actually adding it to the DOM.
    downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
  } else {
    // Firefox requires the link to be added to the DOM before it can be clicked.
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
  }

  downloadLink.click();
}

var button = document.getElementById('save');
button.addEventListener('click', saveTextAsFile);

function destroyClickedElement(event) {
  // remove the link from the DOM
  document.body.removeChild(event.target);
}

function saveTextAsFile2() {
  var textToWrite = document.getElementById('myTextArea1').value;
  console.log(textToWrite.value);
  var textFileAsBlob = new Blob([ textToWrite ], { type: 'text/plain' });
  var fileNameToSaveAs = "saveDecrFile";

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  if (window.webkitURL != null) {
    // Chrome allows the link to be clicked without actually adding it to the DOM.
    downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
  } else {
    // Firefox requires the link to be added to the DOM before it can be clicked.
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement2;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
  }

  downloadLink.click();
}

var button2 = document.getElementById('save2');
button2.addEventListener('click', saveTextAsFile2);

function destroyClickedElement2(event) {
  // remove the link from the DOM
  document.body.removeChild(event.target);
}
