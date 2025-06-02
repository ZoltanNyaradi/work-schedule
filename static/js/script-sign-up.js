document.addEventListener("DOMContentLoaded",function(){

	const button = document.getElementsByClassName("btn")[0];

	const name = document.getElementById("id_username");

	const password = document.getElementById("id_password1");

	const password2 = document.getElementById("id_password2");

	button.addEventListener("click",(event)=>{
		
		if (name.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your username!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
		}
		else if (password.value==""){
			event.preventDefault();
			Swal.fire({
	  			title: 'Error!',
				text: 'Enter your password!',
				icon: 'error',
				confirmButtonText: 'OK'
			})
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