document.addEventListener("DOMContentLoaded",function(){
	loadSchedule();

})

function loadSchedule(){
	let schedule = document.getElementById("schedule");
	let row = [];
	let column = [];
	let cell = [];
	let daysOfTheWeek = ["","Monday","Tuesday","Wednesday","Thurstday","Friday","Saturday","Sunday"];
	let employee = ["","Joe", "Lily", "Bob", "Anna"];
	let screenWidth = window.innerWidth;
	let numberOfEmployees = employee.length;/////////////////////////////////////////////////////////////////

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
  				// First column
  				else if(j==0){
  					column[i][j].classList.add("first-col");

  					cell[i].push(document.createElement("p"));
  					cell[i][j].innerHTML = employee[i];
  					column[i][j].appendChild(cell[i][j]);
  				}
  			}
	}
}