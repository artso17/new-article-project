const url =window.location.href
const articleForm=document.getElementById('articleform')
const articleInput=document.getElementsByName('article_search')[0]
const articleTable=document.getElementById('table-article')
const articleCsrf=document.getElementsByName('csrfmiddlewaretoken')[1].value

console.log(articleInput)

const sendSearchData=(data)=>{
    $.ajax(
        {
            type:'POST',
            url:'/search-admin/',
            data:{
                'csrfmiddlewaretoken':articleCsrf,
                'data':data,
            },
            success:(res)=>{
                console.log(res)
            },
            error:(err)=>{
                console.log(err)
            }
        }

    )
}

articleInput.addEventListener('keyup',e=>{
    articleTable.innerHTML='';
    sendSearchData(e.target.value)
})