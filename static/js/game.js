/*
let data = {};

const api_get = function (url, callback) {
        // it is not called from outside
        // loads data from API, parses it and calls the callback with it

        fetch(url, {
            method: 'GET',
            credentials: 'same-origin'
        })
            .then(response => response.json())  // parse the response as JSON
            .then(json_response => callback(json_response));  // Call the `callback` with the returned object
    };


async function getData(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data;
};*/

/*const drawACard = function (deck, selector, url) {
    let newCard = getData(url);
    deck.addEventListener("click", function(){
        //document.querySelector(selector).appendChild(newCard)
        console.log(newCard);
    };
});

drawACard(dgBack, "#dg-cards-in-hands", "http://0.0.0.0:8000/draw-dg-card");*/

document.addEventListener('contextmenu', function(event) {
   event.preventDefault();
}, true);

let dgCardsInHands = document.querySelectorAll(".dg-card-hand");
let trCardsInHands = document.querySelectorAll(".tr-card-hand");
const dgBack = document.querySelector("#dg-back");
const trBack = document.querySelector("#tr-back");

for (card of dgCardsInHands) {

    card.addEventListener("click", function(){

        document.querySelector("#cards-on-table").appendChild(this);
        if (this.dataset.type == "race") {

            document.querySelector("#race").dataset.race = this.dataset.name;
            document.querySelector("#race").innerHTML = this.dataset.name;
        }

        else if (this.dataset.type == "class") {

            document.querySelector("#class").dataset.class = this.dataset.name;
            document.querySelector("#class").innerHTML = this.dataset.name;
        };

        this.classList.add("on-table");
        this.classList.remove("dg-card-hand");
    });

    card.addEventListener("contextmenu", function(){

        if (this.classList.contains("on-table")) {

            if (this.dataset.type == "race") {

            document.querySelector("#race").dataset.race = "human";
            document.querySelector("#race").innerHTML = "Ember";
            }

            else if (this.dataset.type == "class") {

                document.querySelector("#class").dataset.class = "bumpkin";
                document.querySelector("#class").innerHTML = "Bugris";
            };
        };

        this.remove();
    });
};

for (card of trCardsInHands) {

    card.addEventListener("click", function() {

        document.querySelector("#cards-on-table").appendChild(this);
        if (Number(this.dataset.bonus) >= 1) {
            document.querySelector("#combat-strength").innerHTML = Number(document.querySelector("#combat-strength").innerHTML) + Number(this.dataset.bonus);
        };
        this.classList.remove("tr-card-hand");
        this.classList.add("on-table");
    });


    card.addEventListener("auxclick", function(){

        if (this.classList.contains("on-table")) {

            if (Number(this.dataset.bonus) >= 1) {
                let actualCombatStrength = Number(document.querySelector("#combat-strength").innerHTML);
                document.querySelector("#combat-strength").innerHTML = actualCombatStrength - this.dataset.bonus;
            };
            this.remove()
        };
    });
};

document.querySelector("#dice").addEventListener("click", function(){

    let roll = Math.floor(Math.random() * 6) + 1;
    document.querySelector("#rolled-dice").innerHTML = `<img src="/static/images/dice${roll}.png" width="100px">`;
});

document.querySelector("#rolled-dice").addEventListener("click", function(){

    this.innerHTML = '';
});