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
        } else {
            throw new Error('Response not ok');
        }
    } catch (exception) {
        console.log('Ajax Error:', exception.message);
    }

    callback(responseJson);
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


function sendAjax(e) {
    e.preventDefault()
    var formData = new FormData()
    let file = document.getElementById("inp").files.item(0)
    formData.append('photo', file)
    let images = []

    ajaxForm("http://localhost:8000/api/get_mtx_data", "POST", formData, (r) => {
        images = r
        console.log(images)
        appendImages(images)

    })
    console.log(file)
}


let app = document.getElementById("app")
let form = document.getElementById("form")
form.onsubmit = sendAjax;