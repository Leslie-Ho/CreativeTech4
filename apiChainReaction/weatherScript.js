const d = new Date();
//const triggerButton = document.getElementById('refreshTrigger')

let minutes = d.getMinutes();

let weatherAppID = "f8bb3293d3e0c78998d7b539f896df63";
let searchMethod = 'zip';
let currentZip = '91007';
let currentYear = 2023;

function searchWeather(searchTerm) {
    fetch(`https://api.openweathermap.org/data/2.5/weather?zip=${currentZip},us&appid=${weatherAppID}&units=Imperial`).then(result => {
        //console.log(result.json);
        return result.json();
    }).then(result => {
        console.log("weather description: " + result.weather[0].description)
        searchPokemon(result)
        searchMetMuseum(result.weather[0].description)
        
    })
    document.body.style.backgroundImage = 'url("https://steamuserimages-a.akamaihd.net/ugc/1758073114103109159/20B042641BF6359FEE0D9E96CE7D62205EB179A3/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")'
}

function searchPokemon(searchTerm) {
    let windDegree = searchTerm.wind.deg;
        if(windDegree < 12) {
            windDegree = 12;
        }
    console.log("wind Degree: " + windDegree);
    windDegree /= 12;
    windDegree = Math.floor(windDegree).toString()

    let cloudDensity = searchTerm.clouds.all;
    if(cloudDensity < 10) {
        cloudDensity = 10;
    }
    cloudDensity /= 10;
    cloudDensity = Math.ceil(cloudDensity).toString();
    console.log("cloud density: " + cloudDensity);

    fetch('https://pokeapi.co/api/v2/characteristic/' + windDegree, {
        method: 'GET',
        headers: {
            'Accept' : 'application/json',
        }
    })
    .then(response => response.json())
    .then(response => {
        let pokePersonality = response.descriptions[7].description;
        console.log("pokemon personality: " + pokePersonality)
        document.getElementById('pokePersonality').innerHTML = pokePersonality
    })

    fetch('https://pokeapi.co/api/v2/pokemon-color/' + cloudDensity, {
        method: 'GET',
        headers: {
            'Accept' : 'application/json',
        }
    })
    .then(response => response.json())
    .then(response => {
        //tODO get pokemon name and image from color
        let pokemonSpecies = response.pokemon_species.length;
        let randNum = Math.floor(Math.random() * pokemonSpecies);
        let pokeName = response.pokemon_species[randNum].name;
        console.log("pokemon name: " + pokeName)
        document.getElementById('pokeName').innerHTML = pokeName;
        
        fetch('https://pokeapi.co/api/v2/pokemon/' + pokeName, {
            method: 'GET',
            headers: {
                'Accept' : 'application/json',
            }
        })
        .then(response => response.json())
        .then(response => {
            //get Pokemon image
            //console.log(response.sprites.front_default)
            document.getElementById("pokeImage").src=response.sprites.front_default;

        })
    })
}

function searchMetMuseum(searchTerm) {
    fetch('https://collectionapi.metmuseum.org/public/collection/v1/search?q=' + searchTerm, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(response => {
        let objectCount = JSON.stringify(response.objectIDs.length);
        let randNum = Math.floor(Math.random() * objectCount)
        let objectID = response.objectIDs[randNum];
        
        fetch('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + objectID, {
            method: 'GET',
            headers: {
                'Accept' : 'application/json',
            }
        })
        .then(response => response.json())
        .then(response => {
            document.getElementById("primaryArt").src=response.primaryImage;

            let accessionYear = parseInt(response.accessionYear);
            console.log("assessed year: " + accessionYear);
            let yearSinceAccession = (currentYear - accessionYear).toString();
            fetch('https://poetrydb.org/linecount/' + yearSinceAccession, {
                method: 'GET',
                headers: {
                    'Accept' : 'application/json',
                }
            })
            .then(response => response.json())
            .then(response => {
                let poemCount = response.length;
                let randPoem = Math.floor(Math.random() * poemCount)
                console.log("first line of poem: " + response[randPoem].lines[0]);
                document.getElementById('poemLine').innerHTML = response[randPoem].lines[0];
            })
        })
    })
}

function convertUnix(unix) {
    var date = new Date(unix * 1000);
    var hour = date.getHours();
    var min = date.getMinutes();
    if (hour > 12) {
        hour -= 12;
    }  
    var formatted = hour + ':' + min + " PM";
    return formatted;
}

function setTime() {
    let now = new Date();
    let date = now.toDateString();
    let hours = now.getHours();
    let minute = now.getMinutes();
    let timeOfDay = " AM"

    if (hours > 12) {
        hours -= 12;
        timeOfDay = " PM"
    }   
    if (minute < 10){
        minute = "0" + minute;
    }
    
    document.getElementById('date').innerHTML = date;
    document.getElementById('time').innerHTML = hours + ":" + minute + timeOfDay;
}

//triggerButton.addEventListener("click", searchWeather(currentZip))

searchWeather(currentZip);
//window.onload = setTime();
//setInterval(setTime, 1000);