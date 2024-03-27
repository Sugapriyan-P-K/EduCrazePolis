"use strict";

const scriptELement =
    document.currentScript ||
    document.querySelector('script[src*="getData.js"]');
const fetchFile = scriptELement.dataset.value;
const row = document.querySelector(".row");

const renderCards = function (data) {
    data.forEach((elem) => {
        const html = `<div class="col-12 col-md-4 my-5">
        <div class="card">
            <div class="card-body">
                <h4 class="card-title">
                    ${elem.title}
                    <span class="badge bg-primary">new</span>
                </h4>
                <p class="card-text">
                    ${elem.description}
                </p>
                <div class="d-grid">
                    <a href="${elem.linker}/page/1/" class="btn btn-dark btn-block mt-4"
                        >New Game</a
                    >
                </div>
            </div>
            <div class="card-footer">
                <p class="text-muted card-text">
                    Updated on: June 6, 2023
                </p>
            </div>
        </div>
    </div>`;
        row.innerHTML += html;
    });
};

fetch(`http://localhost:3000/api/data/${fetchFile}`)
    .then((response) => response.json())
    .then((data) => renderCards(data))
    .catch((err) => console.log("here", err));
