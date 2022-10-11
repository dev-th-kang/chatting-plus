
const listDiv = document.querySelector('.list')
const btn = document.querySelector('.btn');
const positBtn = document.querySelector('.create_btn');
const nonpositBtn = document.querySelector('.list_btn');
positBtn.addEventListener('click',()=>{
    location.href='./index.htm';
})
nonpositBtn.addEventListener('click',()=>{
    location.href='./list.htm';
})
document.addEventListener('DOMContentLoaded',()=>{
    positBtn.style = "background-color:#1AAB8A;"
    positBtn.innerHTML = "✅TODO 작성";
    nonpositBtn.innerHTML = "🔥TODO 목록";
})
function createTodo(contents){
    
    fetch(`http://localhost:8000/todo`, {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        "Authorization":JSON.parse(sessionStorage.getItem("token")).token
    }, body: JSON.stringify({
        'contents': contents,
    }),
    })
    .then((response) => response.json())
    .then((data) =>{
        console.log("data",data)
        if(data.token == null){
            console.log(data);
            alert('게시되었습니다.')
            location.reload();
        }else{
            newToken = data.token
            sessionStorage.setItem('token',JSON.stringify({'token':newToken}))
            createTodo(contents)
        }
    });
}
btn.addEventListener('click',()=>{
    console.log('a')
    const contents = document.querySelector('.todo_contents').value;
    document.querySelector('.todo_contents').value = "";
    //console.log(title+" "+content);
    if(contents == ""){
        alert("값을 입력해주세요!");
        return;
    }
    console.log(JSON.parse(sessionStorage.getItem("token")));
    createTodo(contents)
})