document.addEventListener("DOMContentLoaded",function(){
	loadSchedule();
	loadToday();
	document.getElementById("employee-name").addEventListener("blur",(event)=>{nameCheck()});
})

function loadSchedule(){
	let schedule = document.getElementById("schedule");
	let row = [];
	let column = [];
	let cell = [];
	let daysOfTheWeek = ["","Monday","Tuesday","Wednesday","Thurstday","Friday","Saturday","Sunday"];
	let employees = loadEmployees();

	let screenWidth = window.innerWidth;
	let numberOfEmployees = employees.length;/////////////////////////////////////////////////////////////////

	for(let i = 0; i < numberOfEmployees; i++){
		row.push(document.createElement("div"));

		row[i].classList.add("row");

  		row[i].style.height = "30px";
  		schedule.children[0].children[0].appendChild(row[i]);

  		column.push([]);
  		cell.push([]);

  			for(let j = 0; j < 8; j++){
  				column[i].push(document.createElement("div"));
  				column[i][j].classList.add("col");

  				row[i].appendChild(column[i][j])
  				// Give a class and fill the first row.
  				if(i==0){
  					column[i][j].classList.add("first-row");

  					cell[i].push(document.createElement("p"));
  					cell[i][j].innerHTML = daysOfTheWeek[j];
  					column[i][j].appendChild(cell[i][j]);
  				}
  				// Give a class and fill the first column.
  				else if(j==0){
  					if (employees[i].groups%2==0){
  						column[i][j].classList.add("first-col-primary");
  					}else{
  						column[i][j].classList.add("first-col-secundary");
  					}
  					cell[i].push(document.createElement("p"));
  					cell[i][j].innerHTML = employees[i].username;
  					column[i][j].appendChild(cell[i][j]);
  				}
  			}
	}
}

function loadEmployees(){
	const users = JSON.parse(document.getElementById('users-data').textContent);

	differentGroups = [];

	users.forEach ((user) =>{
		if(user.is_staff){
		group = user.groups;
		if(!differentGroups.includes(group)){
			differentGroups.push(group);}
		}})

	orderedUsers=[""];

	differentGroups.forEach((group) =>{
		users.forEach((user) =>{
			if(group==user.groups && user.is_staff){
				orderedUsers.push(user);
			}
		});
	});
	return orderedUsers;
}

function nameCheck(){
	/**
	 * Checks if the given name in edit-schedule exist in the database,
	 * if not than an error message shows up. 
	 * In case of correction the error message dissapears.
	 */

	// Get the name from the form
	let name = document.getElementById("employee-name");
	// Get employees' data
	let employees = loadEmployees();
	// Make a list of the names of emplyoees
	let names = [];
	employees.forEach((employee)=>{
		names.push(employee.username);
	});
	// Hide or show the error message
	let nameError = document.getElementById("name-error");
	if (names.includes(name.value)){
		nameError.hidden=true;
	}else{
		nameError.hidden=false;
	}
}

function loadToday(){
	/**
	 * Loads the current day into edit-schedule 
	 */
	const today = new Date().toISOString().slice(0, 10);
	document.getElementById("shift-date").value=today;
}