export const truncate = (data,maxword)=>{
    const splitQs=data.split(' ')
    if (splitQs.length>maxword-1){
    const arrData=splitQs
    let newArrData=[]
    for (let i = 0; i < arrData.length; i++) {
            if (i>maxword-1) break;
            newArrData.push(arrData[i]);
        }
        return newArrData.join(' ')
    }
    return splitQs.join(' ')
}

export const sendData=(data,csrf,numLikes,)=>{
    $.ajax(
        {
            type:'POST',
            url:'/likes/',
            data:{
                'csrfmiddlewaretoken':csrf,
                'data':data.getAttribute('value'),
            },
            success:res=>{
                numLikes.innerHTML=`<strong>likes:</strong>  ${res.data[0]['num_likes']}`
                if (res.data[0]['liked'] != true){
                data.firstElementChild.setAttribute('src','/static/img/icon/hand-thumbs-up.svg')
                data.firstElementChild.setAttribute('alt','Unlike Button')
                }else{
                data.firstElementChild.setAttribute('src','/static/img/icon/hand-thumbs-up-fill.svg')
                data.firstElementChild.setAttribute('alt','Like Button')
                }
            },
            error:err=>{
            console.log(err)
            }
    
        }
    )
        
}

export const sendComment=(data,pk,...args)=>{
    if (data.value!='') {
        $.ajax({
            type:'POST',
            url:'/add-comment/',
            data:{
                'csrfmiddlewaretoken':args[0],
                'pk':pk,
                'data':data.value,
            },
            success:res=>{
                args[1].innerHTML+=`
                <section class="comment-section">
                    <p>Dari: <strong>${res.data[0].author}</strong></p>
                    <p>${res.data[0].isi}</p>
                    <hr>
                </section>
                `
                data.value=''
            },
            error:err=>{
                console.log(err)
            }
    
    
        })
        
    }
}

export const sendSearchData=(data,nameInput,nameTable,tableBody,csrf)=>{
    $.ajax(
        {
            type:'POST',
            url:'/search-admin/',
            data:{
                'csrfmiddlewaretoken':csrf,
                'data':data,
                'nameInput':nameInput['name'],
            },
            success:(res)=>{
                nameTable.innerHTML=' '
                const data =res.data
                if (Array.isArray(data)){
                    if (nameTable==tableBody['table-article']){
                        data.forEach((e,i)=>{
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
                            nameTable.innerHTML+=`<tr>
                            <th scope="row">${i+1}</th>
                            <td>${truncate(e.name,2)}</td>
                            <td><a class="btn btn-danger text-capitalize" href="#" role="button">delete</a> | <a class="btn btn-warning text-capitalize" href="/update/category/${e.id}" role="button">updated</a></td>
                        </tr>
                        `
                        })
                    }else if(nameTable==tableBody['table-user']){
                        data.forEach((e,i)=>{
                            status=e.is_superuser && e.is_staff && e.is_active ? 'Active | Staff | Super User': e.is_staff && e.is_active ? 'Active | Staff ': 'Active'
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
                    if (nameInput.value.length>0) nameTable.innerHTML+=`<center><h3>${res.data}</h3></center>`
                    else nameTable.innerHTML+=``
                }
            },
            error:(err)=>{
                // console.log(err)
            }
        }
    )
}

export const showMoreComm=(csrf,...args)=>{
    if (args[2].children.length<100) {
        $.ajax({
            url:'/show-comment/',
            type:'POST',
            data:{
                'csrfmiddlewaretoken':csrf,
                'pk':args[0],
                'data':args[1].value,
            },
            success:res=>{
                res.data.forEach(e=>{
                    args[2].innerHTML+=`
                    <section class="comment-section">
                        <p>Dari: <strong>${e.author}</strong></p>
                        <p>${e.isi}</p>
                        <hr>
                    </section>
                    `
                })
                args[1].value=res.end_data
                args[4].children[0].value=res.end_data
                if (args[2].children.length>= 11) args[4].classList.remove('d-none')
                if (args[2].children.length===res.len_data) args[3].classList.add('d-none')
            },
            error:err=>console.log(err)
        })
        
    }
}
export const showLessComm=(comm,...args)=>{
    const children=comm.children.length
    let amount=0
    if (children%10===0)amount=children-10
    else amount=Math.floor(children/10)*10
    args[0].value=amount
    args[0].parentElement.classList.remove('d-none')
    const data=[]
    for (let i = 0; i < comm.children.length; i++) {
        if (i===amount)break;
        data.push(comm.children[i])
    }
    comm.innerHTML=''
    for (let i = 0; i < data.length; i++) {
        comm.innerHTML+=`
        <section class="comment-section">
        ${data[i].innerHTML}
        </section>
        `
    }
    if (amount===10) args[1].parentElement.classList.add('d-none')
}