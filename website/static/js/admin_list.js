const url =window.location.href
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value
const searchInput=document.getElementsByClassName('search-input')
const tableBody=document.getElementsByClassName('table-body')
//  console.log(searchInput) 



import { sendSearchData } from "./module.js"



    for (let i = 0; i < searchInput.length; i++) {
        searchInput[i].addEventListener('keyup',e=>{
            sendSearchData(e.target.value,searchInput[i],tableBody[i],tableBody,csrf)
        });
    }

