let isSamePass = false;
function passwordValidCheckHandler(){
    const cpass =document.querySelector('.cpassword').value
    const pass =document.querySelector('.password').value
    if(cpass == pass){
        const chkpass = document.querySelector('.chkpass')
        chkpass.innerHTML = 'password confirm ✅:'
        isSamePass = true;
    }else{
        const chkpass = document.querySelector('.chkpass')
        chkpass.innerHTML = 'password confirm 🚫:'
        isSamePass = false;
    }
}
document.querySelector('.password').addEventListener('input',passwordValidCheckHandler)
document.querySelector('.cpassword').addEventListener('input',passwordValidCheckHandler)
document.querySelector('.join_send').addEventListener('click',()=>{
    const name = document.querySelector('.name').value;
    const userid = document.querySelector('.userid').value;
    const password = document.querySelector('.password').value;
    const email = document.querySelector('.email').value;
    if(name != "" && userid != "" && password != "" && email != ""){
        if(isSamePass){
            fetch("http://localhost:8000/join", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },body:JSON.stringify({
                    'name':name,
                    'userid':userid,
                    'password':password,
                    'email':email
                })
                })
                .then((response) => response.json())
                .then((data) =>{
                    if(data.msg == "succeed"){
                        alert("가입을 완료하였습니다.");
                        location.href="./login.htm"
                    }else{
                        alert("이미 존재하는 아이디입니다..");
                    }
                });
        }else{
        alert('입력하신 두 비밀번호가 다릅니다.');
        }
    }else{
        alert('빈칸이 없어야합니다..');
    }
})