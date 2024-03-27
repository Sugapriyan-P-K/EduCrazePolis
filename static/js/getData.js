"use strict";

const scriptELement =
    document.currentScript ||
    document.querySelector('script[src*="getData.js"]');
const fetchFile = scriptELement.dataset.value;
const card = document.getElementById("card-content");

const renderCards = function (data) {
    data.forEach((elem) => {
        const html = `<div class="card">
                            <h2>${elem.title}</h2>
                        <p>${elem.description}</p>
                        <a href="${elem.linker}/page/1/">New Game <span class="material-symbols-outlined">arrow_forward</span></a>
                    </div>`;
        card.innerHTML += html;
    });
};

fetch(`http://localhost:3000/api/data/${fetchFile}`)
    .then((response) => response.json())
    .then((data) => renderCards(data))
    .catch((err) => console.log("here", err));
