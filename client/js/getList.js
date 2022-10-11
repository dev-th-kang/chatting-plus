const listDiv = document.querySelector('.list')
const btn = document.querySelector('.btn'); 
const nonpositBtn = document.querySelector('.create_btn');
const positBtn = document.querySelector('.list_btn');
positBtn.addEventListener('click',()=>{
    location.href='./list.htm';
})
nonpositBtn.addEventListener('click',()=>{
    location.href='./index.htm';
})
function deleteFunc(contents){
    fetch(`http://localhost:8000/todo/${contents}`, {
    method: "DELETE",
    headers: {
        "Content-Type": "application/json",
        "Authorization":JSON.parse(sessionStorage.getItem("token")).token
    },
    })
    .then((response) => response.json())
    .then((data) =>{
        console.log('data',data) 
        if(data.token == null){
            alert("삭제되었습니다.")
            window.location.reload()
        }else{
            newToken = data.token
            sessionStorage.setItem('token',JSON.stringify({'token':newToken}))
            deleteFunc(contents)
        }
    })
}
function deleteList(contents){
    
    const result = confirm(`"${contents}"라는 내용을 정말 삭제하시겠습니까?`)
    if(!result) return;
    console.log(contents)
    deleteFunc(contents)
    
}
function getList(){
    //alert("a")
    positBtn.style = "background-color:#1AAB8A;"
    positBtn.innerHTML = "🔥TODO 목록";
    nonpositBtn.innerHTML = "✅TODO 작성";
    fetch(`http://localhost:8000/todo`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization":JSON.parse(sessionStorage.getItem("token")).token
    },
    })
    .then((response) => response.json())
    .then((data) =>{
        if(data.token == null){
            for(var i=data.length-1;i>=0;i--){
                console.log(data[i].contents)
                listDiv.innerHTML+=
                `
                <small>

                    <h5 style = "margin-left: 10px;" class="list_contents">
                        <button class='del_btn' onclick="javascript:deleteList('${data[i].contents}')">❌</button>  
                        ${data.length-i}번 : <m class= "td_contents">${data[i].contents}</m>
                    </h5>
                </small>
                <hr>
                
    
                `
                const delBtn = document.querySelectorAll('.del_btn')
                for(let i =0; i<delBtn.length;i++){
                    delBtn[i].style ='background-color:white;border: 0px'
                }
                const td_contents = document.querySelectorAll('.td_contents')
                for(let i =0; i<td_contents.length;i++){
                }
            }
        }else{
            newToken = data.token
            sessionStorage.setItem('token',JSON.stringify({'token':newToken}))
            getList()
        }
    });
}
document.addEventListener('DOMContentLoaded',()=>{
    getList()
})

