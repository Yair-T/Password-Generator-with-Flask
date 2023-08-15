// The code by Yair-T | https://youtube.com/@Yair-T | https://github.com/Yair-T
let password = document.querySelector(".password-input"); 
let btn = document.querySelector(".material-symbols-outlined"); 
gen_btn = document.querySelector(".btn"); 
btn.addEventListener("click", function () { 
    password.select(); password.setSelectionRange(0, 99999); 
    navigator.clipboard.writeText(password.value);
     btn.innerText = "done"; setTimeout(() => { 
        btn.innerText = 'content_copy'; 
    }, 1500); 
});