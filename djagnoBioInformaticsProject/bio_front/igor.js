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
        let textField = creteTextField("Input data is in incorrect format!.");
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

function creteTextField(text) {
    let itemDiv=document.createElement("div");
    itemDiv.className = "textProgress"
    itemDiv.textContent = text;
    return itemDiv;
}

function createLinkToDownload(url, text) {
    var link = document.createElement('a');
    link.setAttribute('href',url);
    link.download = url;
    link.text = text;
    return link
}

function appendText(images) {
    let firstUrl = images['Predicted cells by clusters:']
    let secondUrl = images['Interactive pyLDAvis graph:']
    console.log(firstUrl, secondUrl)
    delete images['Predicted cells by clusters:']
    delete images['Interactive pyLDAvis graph:']
    let elem = createLinkToDownload(firstUrl, 'Predicted cells by clusters');
    let elem2 = createLinkToDownload(secondUrl, 'Interactive pyLDAvis graph');
    let groupAdd = document.getElementsByClassName("choseFile")[0]
    elem.className = "infoForDownload";
    elem2.className = "infoForDownload";
    groupAdd.appendChild(elem);
    groupAdd.appendChild(elem2);
}

function deleteAllInfo() {
    let elems = document.querySelectorAll('.textProgress');
    for( let i = 0; i < elems.length; i++ )
        { elems[i].outerHTML = ""; }
    elems = document.querySelectorAll('.containerImage');
    for( let i = 0; i < elems.length; i++ )
        { elems[i].outerHTML = ""; }
    elems = document.querySelectorAll('.infoForDownload');
    for( let i = 0; i < elems.length; i++ )
        { elems[i].outerHTML = ""; }
}

function usingExistingModel(e) {
    e.preventDefault();
    deleteAllInfo();
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
        appendText(images)
        appendImages(images)
        let elems = document.querySelectorAll('.textProgress');
        for( let i = 0; i < elems.length; i++ )
            { elems[i].outerHTML = ""; }
        let textField = creteTextField("Build finished successfully.");
        let groupAdd = document.getElementsByClassName("choseFile")[0]
        groupAdd.appendChild(textField);
    })

    console.log(file)
}

function usingJustBuildModel(e) {
    e.preventDefault();
    deleteAllInfo();
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
        let elems = document.querySelectorAll('.textProgress');
        for( let i = 0; i < elems.length; i++ )
            { elems[i].outerHTML = ""; }
        let textField = creteTextField("Build finished successfully.");
        let groupAdd = document.getElementsByClassName("choseFile")[0]
        groupAdd.appendChild(textField);
    })

    console.log(file)
}

let app = document.getElementById("app")
let form = document.getElementById("form")
let usingModelEvent = document.getElementById("usingBuildModelBtn")
usingModelEvent.onclick = usingExistingModel
let buildNewModelBtn = document.getElementById("buildNewModelBtn")
buildNewModelBtn.onclick = usingJustBuildModel