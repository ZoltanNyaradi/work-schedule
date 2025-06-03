/**
 * Script for sign in page.
 * 
 * Fire error allert if there is a misstake in the form.
 * */

document.addEventListener("DOMContentLoaded",function(){

	const button = document.getElementsByClassName("btn")[0];

	const name = document.getElementById("id_login");

	const password = document.getElementById("id_password");

	button.addEventListener("click",(event)=>{
		// The username field is empty
		if (name.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your username!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
		}
		// The password field is empty
		else if (password.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your password!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
		}
	})
})

// The username and/or the password is incorrect
function handleFormError(errors) {
    for (const field in errors) {
    	if(errors[field]!=="* This field is required."){
	        Swal.fire({
		        title: 'Error!',
		        text: errors[field],
		        icon: 'error'
    		})
    	}
    }
}