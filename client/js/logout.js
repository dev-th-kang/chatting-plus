document.querySelector('.logoutBtn').addEventListener('click',()=>{
    fetch('http://localhost:8000/logout',
    {
        method:'POST',
        headers:{
            "Content-Type": "application/json",
            "Authorization":JSON.parse(sessionStorage.getItem("token")).token
        },
    })
    .then((response) => response.json())
    .then((data)=>{
        if(data.msg == "succeed"){
            sessionStorage.removeItem("token")
            alert("로그아웃이 완료되었습니다.")
            location.href = "./login.htm"
        }

    })
})