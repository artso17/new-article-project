const url =window.location.href
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value
const searchInput=document.getElementsByClassName('search-input')
const tableBody=document.getElementsByClassName('table-body')
console.log(csrf)

const truncate = (data,maxword)=>{
    splitQs=data.split(' ')
    if (splitQs.length>maxword-1){
    const arrData=splitQs
    newArrData=[]
    for (let i = 0; i < arrData.length; i++) {
        if (i>maxword-1){
        break;
        }
    newArrData.push(arrData[i]);
    }
    // console.log(newArrData.join(' '))
        return newArrData.join(' ')
    }
    return splitQs.join(' ')
}

const sendSearchData=(data,nameInput,nameTable)=>{
    $.ajax(
        {
            type:'POST',
            url:'/search-admin/',
            data:{
                'csrfmiddlewaretoken':csrf,
                'data':data,
                'nameInput':nameInput['name'],
                // 'nameTable':nameTable,
            },
            success:(res)=>{
                console.log(res.data)
                nameTable.innerHTML=' '
                console.log(nameTable)
                const data =res.data

                if (Array.isArray(data)){
                    console.log(nameTable==tableBody['table-article'])
                    if (nameTable==tableBody['table-article']){
                        data.forEach((e,i)=>{
                            console.log(e)
                            nameTable.innerHTML+=`<tr>
                            <th scope="row">${i+1}</th>
                            <td>${truncate(e.judul,2)}</td>
                            <td>
                                ${e.category.join(' ')}
                            </td>
                            <td>${e.author}</td>
                            <td>${e.published}</td>
                            <td>${e.updated}</td>
                            <td><a class="btn btn-danger text-capitalize" href="" role="button">delete</a> | <a class="btn btn-warning text-capitalize" href="/update/article/${e.id}" role="button">updated</a></td>
                        </tr>
                        `
                        })
                    }else if(nameTable== tableBody['table-category']){
                        data.forEach((e,i)=>{
                            console.log(e)
                            nameTable.innerHTML+=`<tr>
                            <th scope="row">${i+1}</th>
                            <td>${truncate(e.name,2)}</td>
                            <td><a class="btn btn-danger text-capitalize" href="#" role="button">delete</a> | <a class="btn btn-warning text-capitalize" href="/update/category/${e.id}" role="button">updated</a></td>
                        </tr>
                        `
                        })
                    }else if(nameTable==tableBody['table-user']){
                        data.forEach((e,i)=>{
                            console.log(e)
                            status=e.is_superuser && e.is_staff && e.is_active ? 'Active | Staff | Super User': e.is_staff && e.is_active ? 'Active | Staff ': 'Active'
                            console.log(status)
                            nameTable.innerHTML+=`<tr>
                            <th scope="row">${i+1}</th>
                            <td>${truncate(e.username,2)}</td>
                            <td>${status}</td>
                            <td>${e.group.join(' | ')}</td>
                            <td><a class="btn btn-danger text-capitalize" href="#" role="button">delete</a> | <a class="btn btn-warning text-capitalize" href="/update/user/${e.id}" role="button">updated</a></td>
                        </tr>
                        `
                        })
                    }else if(nameTable==tableBody['table-group']){
                        data.forEach((e,i)=>{
                            nameTable.innerHTML+=`<tr>
                            <th scope="row">${i+1}</th>
                            <td>${truncate(e.name,2)}</td>
                            <td><a class="btn btn-danger text-capitalize" href="#" role="button">delete</a> | <a class="btn btn-warning text-capitalize" href="/update/group/${e.id}" role="button">updated</a></td>
                        </tr>
                        `
                        })
                    }

                }else{
                    if (nameInput.value.length>0){
                        nameTable.innerHTML+=`<center><h3>${res.data}</h3></center>`
                    }else{
                        nameTable.innerHTML+=``
                    }
                }
            },
            error:(err)=>{
                console.log(err)
            }
        }
    )
    }

searchInput['article_search'].addEventListener('keyup',e=>{
    sendSearchData(e.target.value,searchInput['article_search'],tableBody['table-article'])
});

searchInput['category_search'].addEventListener('keyup',e=>{
    sendSearchData(e.target.value,searchInput['category_search'],tableBody['table-category'])
});

searchInput['user_search'].addEventListener('keyup',e=>{
    sendSearchData(e.target.value,searchInput['user_search'],tableBody['table-user'])
});

searchInput['group_search'].addEventListener('keyup',e=>{
    sendSearchData(e.target.value,searchInput['group_search'],tableBody['table-group'])
});