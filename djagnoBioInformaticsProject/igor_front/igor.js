'use strict';

/**
 * Ajax с телом FormData
 * @param {string} route - адресс
 * @param {string} method - метод запроса
 * @param {FormData} formData - данные
 * @param {function} callback - функция, которая будет вызвана после запроса
 */
async function ajaxForm(route, method, formData, callback) {

    const reqBody = {
        method: method,
        mode: 'cors',
        credentials: 'include',
    };

    if (method !== 'GET' && method !== 'HEAD') {
        reqBody['body'] = formData;
    }

    const req = new Request(route, reqBody);
    let responseJson = null;
    try {
        const response = await fetch(req);
        if (response.ok) {
            responseJson = await response.json();
            callback(responseJson);
        } else {
            throw new Error('Response not ok');
        }
    } catch (exception) {
        let test = document.querySelectorAll('.textProgress');
        for( let i = 0; i < test.length; i++ )
            { test[i].outerHTML = ""; }
        let textField = creteTextField("U down.");
        let groupAdd = document.getElementsByClassName("choseFile")[0]
        groupAdd.appendChild(textField);
    }
}

function createImageField(textAddition,imageSrc) {
    let itemDiv=document.createElement("div")
    itemDiv.className="item"

    itemDiv.innerHTML=`<figure>
                    <img src="${imageSrc}" class="readyImages"
                        alt="">
                    <figcaption> <b class="textAddition"> ${textAddition} </b> </figcaption>
            </figure>`
    return itemDiv
}

function appendImages(images) {
    let test = document.querySelectorAll('.containerImage');
    for( let i = 0; i < test.length; i++ )
        { test[i].outerHTML = ""; }
    let containerImage=document.createElement("div")
    containerImage.className="containerImage"
    for (var textAddition in images) {
        let itemDiv=createImageField(textAddition, images[textAddition])
        containerImage.appendChild(itemDiv)
    }
    app.appendChild(containerImage)
}

function kek(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.responseType = 'arraybuffer';
    xhr.onload = function () {
    if (this.status === 200) {
    var filename = "";
    var disposition = xhr.getResponseHeader('Content-Disposition');
    if (disposition && disposition.indexOf('attachment') !== -1) {
    var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
    var matches = filenameRegex.exec(disposition);
    if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, '');
    }
    var type = xhr.getResponseHeader('Content-Type');

    var blob = new Blob([this.response], { type: type });
    if (typeof window.navigator.msSaveBlob !== 'undefined') {
    // IE workaround for "HTML7007: One or more blob URLs were revoked by closing the blob for which they were created. These URLs will no longer resolve as the data backing the URL has been freed."
    window.navigator.msSaveBlob(blob, filename);
    } else {
    var URL = window.URL || window.webkitURL;
    var downloadUrl = URL.createObjectURL(blob);

    if (filename) {
    // use HTML5 a[download] attribute to specify filename
    var a = document.createElement("a");
    // safari doesn't support this yet
    if (typeof a.download === 'undefined') {
    window.location = downloadUrl;
    } else {
    a.href = downloadUrl;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    }
    } else {
    window.location = downloadUrl;
    }

    setTimeout(function () { URL.revokeObjectURL(downloadUrl); }, 100); // cleanup
    }
    }
    };
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send($.param(params));


}

function creteTextField(text) {
    let itemDiv=document.createElement("div");
    itemDiv.className = "textProgress"
    itemDiv.textContent = text;
    return itemDiv;
}

function sendAjax(e) {
    e.preventDefault()
    let test = document.querySelectorAll('.textProgress');
    for( let i = 0; i < test.length; i++ )
        { test[i].outerHTML = ""; }
    let textField = creteTextField("Build in progress.");
    let groupAdd = document.getElementsByClassName("choseFile")[0]
    groupAdd.appendChild(textField);
    var formData = new FormData()
    let file = document.getElementById("inp").files.item(0)
    formData.append('photo', file)
    let images = []
    ajaxForm("http://localhost:8000/api/get_mtx_data", "POST", formData, (r) => {
        images = r
        console.log(images)
        appendImages(images)
        let test = document.querySelectorAll('.textProgress');
        for( let i = 0; i < test.length; i++ )
            { test[i].outerHTML = ""; }
        let textField = creteTextField("Build finished successfully.");
        let groupAdd = document.getElementsByClassName("choseFile")[0]
        groupAdd.appendChild(textField);
    })

    console.log(file)
}


function createLinkToDownload(url) {
    var link = document.createElement('a');
    link.setAttribute('href',url);
    link.setAttribute('download','download');
    return link
}

function appendText(images) {
    let firstUrl = images['Predicted cells by clusters:']
    let secondUrl = images['Interactive pyLDAvis graph:']
    console.log(firstUrl, secondUrl)
    delete images['Predicted cells by clusters:']
    delete images['Interactive pyLDAvis graph:']
    let elem = createLinkToDownload(firstUrl);
    kek(firstUrl)
    //elem.click()
    //app.appendChild(elem)
    /*let test = document.querySelectorAll('.containerImage');
    for( let i = 0; i < test.length; i++ )
        { test[i].outerHTML = ""; }
    let containerImage=document.createElement("div")
    containerImage.className="containerImage"
    for (var textAddition in images) {
        let itemDiv=createImageField(textAddition, images[textAddition])
        containerImage.appendChild(itemDiv)
    }
    app.appendChild(containerImage)*/
}

function sendAjax2(e) {
    e.preventDefault()
    let test = document.querySelectorAll('.textProgress');
    for( let i = 0; i < test.length; i++ )
        { test[i].outerHTML = ""; }
    let textField = creteTextField("Build in progress.");
    let groupAdd = document.getElementsByClassName("choseFile")[0]
    groupAdd.appendChild(textField);
    var formData = new FormData()
    let file = document.getElementById("inp").files.item(0)
    formData.append('photo', file)
    let images = []
    ajaxForm("http://localhost:8000/api/build_model_and_get_mtx_data", "POST", formData, (r) => {
        images = r
        console.log(images)
        appendText(images)     
        appendImages(images)
        let test = document.querySelectorAll('.textProgress');
        for( let i = 0; i < test.length; i++ )
            { test[i].outerHTML = ""; }
        let textField = creteTextField("Build finished successfully.");
        let groupAdd = document.getElementsByClassName("choseFile")[0]
        groupAdd.appendChild(textField);
    })

    console.log(file)
}

let app = document.getElementById("app")
let form = document.getElementById("form")
let usingModelEvent = document.getElementById("usingBuildModelBtn")
usingModelEvent.onclick = sendAjax
let buildNewModelBtn = document.getElementById("buildNewModelBtn")
buildNewModelBtn.onclick = sendAjax2