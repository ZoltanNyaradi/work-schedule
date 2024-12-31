document.addEventListener("DOMContentLoaded",function(){
	loadSchedule();
	loadToday();
	document.getElementById("employee-name").addEventListener("blur",(event)=>{nameCheck()});
	let shiftClass = document.getElementsByClassName("shift");
	for(let i=0; i<4; i++){
		shiftClass[i].addEventListener("click",(event)=>{klickToShift()});
	}
	document.getElementById("vacation").addEventListener("click",(event)=>{klickToVacation()});
	document.getElementById("sick").addEventListener("click",(event)=>{klickToSick()});

	loadEmployeesToEditSchedule();
})

function loadSchedule(){
	/***
	 * Load the schedule table on the screen. 
	 */
	let schedule = document.getElementById("schedule");
	let row = [];
	let column = [];
	let cell = [];
	let daysOfTheWeek = ["","Monday","Tuesday","Wednesday","Thurstday","Friday","Saturday","Sunday"];
	let datesOfTheWeek = loadDatesOfTheWeek();
	let employees = loadEmployees();
	let numberOfEmployees = employees.length;
	let shiftsOfTheWeek = loadSchiftOfTheWeek(datesOfTheWeek[0], numberOfEmployees, employees, datesOfTheWeek);
	

	for(let i = 0; i < numberOfEmployees; i++){
		row.push(document.createElement("div"));
		// Make a row for every employee and one more for the dates
		row[i].classList.add("row");
		// Add the row class to them
  		schedule.children[0].children[0].appendChild(row[i]);
  		// Place it in the schedule

  		column.push([]);
  		// Add an empty Array for columns
  		cell.push([]);
  		// Add an empty Array for cells

  			for(let j = 0; j < 8; j++){
  				column[i].push(document.createElement("div"));
  				// Make a column for the emplyoees and 7 for the days of the week
  				column[i][j].classList.add("col");
  				// Add col class to them
  				row[i].appendChild(column[i][j])
  				// Add the columns to a row

  				if(i==0){
  					// If we are in the first row
  					column[i][j].classList.add("first-row");
  					// Add the first row class to it
  					cell[i].push(document.createElement("p"));
  					// Add a paragraph to the cell
  					cell[i][j].innerHTML = `${daysOfTheWeek[j]} <br/> ${datesOfTheWeek[j]}`;
  					// Add the proper day and date to it
  					column[i][j].appendChild(cell[i][j]);
  					// Add it to a column
  				}
  				else if(j==0){
  					// Else if it is the first column but not the first row
  					if (employees[i].groups%2==0){
  						// Color the first cells by positions
  						// If the employee in an even group
  						column[i][j].classList.add("first-col-primary");
  						// Add to the primary color group
  					}else{
  						column[i][j].classList.add("first-col-secondary");
  						// Else add to the secondary color group
  					}
  					column[i][j].classList.add("first-col");
  					// Add the first-col class to it
  					cell[i].push(document.createElement("p"));
  					// Add a paragraph to the cell
  					cell[i][j].innerHTML = employees[i].username;
  					// Write an emplyoee's name in it
  					column[i][j].appendChild(cell[i][j]);
  					// The cell to a column
  				}else{
  					// If it is neither first row or first column
  					if(shiftsOfTheWeek[i-1][j-1]===undefined){
  						// If there is no related shift to the cell
  						column[i][j].innerHTML = "";
  						// Add an empty text to the cell
  					} else {
  						// If there is a related shift to the cell
  					column[i][j].innerHTML = shiftsOfTheWeek[i-1][j-1];
  						// Add this shift as a text to it
  					}
  					column[i][j].addEventListener("click",(event)=>{
  						fillForm(datesOfTheWeek[j], employees[i].id)
  					});
  						// Fill employee and date to editSchedule 
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

function klickToShift(){
	let shiftClass = document.getElementsByClassName("shift");
	for(let i=0; i<4; i++){
		shiftClass[i].style.backgroundColor = "#FFFFFF";
	}
	document.getElementById("vacation").checked=false;
	document.getElementById("sick").checked=false;
}

function klickToVacation(){
	let shiftClass = document.getElementsByClassName("shift");
	for(let i=0; i<4; i++){
		shiftClass[i].style.backgroundColor = "#EEEEFF88";
		shiftClass[i].value = undefined;
	}
	document.getElementById("sick").checked=false;
}

function klickToSick(){
	let shiftClass = document.getElementsByClassName("shift");
	for(let i=0; i<4; i++){
		shiftClass[i].style.backgroundColor = "#EEEEFF88";
		shiftClass[i].value = undefined;
	}
	document.getElementById("vacation").checked=false;
}

function loadEmployeesToEditSchedule(){
	const employeesForDropdown = JSON.parse(document.getElementById('users-data').textContent);
	i=0;
	let employeeName = document.getElementById("employee-name");
	let options=[];
	employeesForDropdown.forEach ((employeeForDropdown)=>{
		options[i] = document.createElement("option");
		options[i].value = employeeForDropdown.id;
		options[i].text = employeeForDropdown.username;
		if (employeeForDropdown.is_staff){
			employeeName.appendChild(options[i]);
		}
		i++;
	})
}

function loadDatesOfTheWeek(){
	const date = new Date();
	let todayIs = date.getDay();

	if (todayIs==0){
		date.setDate(date.getDate()-6);
	} else{
		date.setDate(date.getDate()-todayIs+1)
	}

	let datesOfTheWeek = [];
	datesOfTheWeek.push("");
	for (let i=0; i<7; i++){
		datesOfTheWeek.push(date.toISOString().slice(0, 10));
		date.setDate(date.getDate()+1);
	}
	return datesOfTheWeek;
}

function loadSchiftOfTheWeek(monday, numberOfEmployees, employees, datesOfTheWeek){

	const schedules = JSON.parse(document.getElementById("schedule-data").textContent);
	let shiftsOfTheWeek = [];
	let shift = "";

	for (let i = 1; i<numberOfEmployees; i++){

		shiftsOfTheWeek.push([]);
		for (let j = 1; j<8; j++){
			schedules.forEach((individuellSchedule)=>{
				if(individuellSchedule.user==employees[i].id && individuellSchedule.date == datesOfTheWeek[j]){
					if(individuellSchedule.vacation==true){
						shift = "Vacation";
					} else {
						if (individuellSchedule.sick==true){
							shift = "Sick";
						} else {
							shift = individuellSchedule.begin_of_work_1.slice(0,5) + "-" +
							    individuellSchedule.end_of_work_1.slice(0,5);

							if(individuellSchedule.begin_of_work_2 != null){
								shift += "<br class='shift-break'>"+ individuellSchedule.begin_of_work_2.slice(0,5) + "-" +
							    individuellSchedule.end_of_work_2.slice(0,5);
							}
						}	
					}					
				shiftsOfTheWeek[i-1].push(shift);
				} else {
					shift = "";

				}
			})			

		}
	}
	//console.log(shiftsOfTheWeek);
	return shiftsOfTheWeek

}

function fillForm(date, employee){
	/**
	* Fill date and employee in edit schedule
	* with the given properties. 
	*/
	document.getElementById("employee-name").value = employee;
	document.getElementById("shift-date").value = date;
}