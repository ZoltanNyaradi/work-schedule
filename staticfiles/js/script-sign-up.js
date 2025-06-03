/***
 * Script for sign up page.
 * 
 * Fire an error message if the form is incorrectly filled.
 */
 document.addEventListener("DOMContentLoaded",function(){

	const button = document.getElementsByClassName("btn")[0];

	const name = document.getElementById("id_username");

	const password = document.getElementById("id_password1");

	const password2 = document.getElementById("id_password2");

	button.addEventListener("click",(event)=>{
		// Username field is empty
		if (name.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your username!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
		}
		// First password field is empty
		else if (password.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your password!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
		// Second password field is empty
		} else if (password2.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your password again!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
		}
	})

})

/**
 * Other errors.
 * 
 * Password is not long enough
 * Password is too common
 * Password is too similar to the username
 * The 2 password is not matching
 * */
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