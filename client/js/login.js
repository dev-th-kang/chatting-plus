document.querySelector('.login_send').addEventListener('click',()=>{
    const userid = document.querySelector('.userid').value;
    const password = document.querySelector('.password').value;
    if(userid != "" && password != ""){
        fetch("http://localhost:8000/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },body:JSON.stringify({
                'userid':userid,
                'password':password
            })
            })
            .then((response) => response.json())
            .then((data) =>{   
                if(data.msg =="succeed"){
                    console.log(data)
                    sessionStorage.setItem('token',JSON.stringify(data.token))
                   //const useritem = sessionStorage.getItem('user')
                    alert('로그인이 완료되었습니다.')
                    location.href="./index.htm"
                }else{
                    console.log(data.msg)
                    alert("아이디나 비밀번호를 잘못입력하였습니더ㅏ.");
                    return;
                }
            });
    }else{
        alert('빈칸이 없어야합니다..');
    }
})