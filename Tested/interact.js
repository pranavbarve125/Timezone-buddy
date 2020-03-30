var years = [2020, 2021, 2022];
var numberOfYears = years.length;
var monthdays = new Object();
var monthdays = {
    "January" : 31,
    "February" : 0,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31
};
var fromYear = document.querySelector("#from .year");
var fromMonth = document.querySelector("#from .month");
var fromDay = document.querySelector("#from .day");
var startYear = 0;
var startMonth = 0;
var startDay = 0;

function yearChangeFunction(){
    if ((fromYear.value % 4) == 0){
        monthdays['February'] = 29;
    }
    else{
        monthdays['February'] = 28;
    }
    
    if (fromYear.value != "NA"){
        fromMonth.disabled = false;
        for(var key in monthdays){
            fromMonth.innerHTML += "<option value = " + key + ">" + key + "</option>";
        }
    }
    else{
        fromMonth.innerHTML = "";
        fromDay.innerHTML = "";
        fromMonth.disabled = true;
        fromDay.disabled = true;
    }
}

function monthChangeFunction(){
    numberOfDays = monthdays[fromMonth.value];
    fromDay.disabled = false;
    for(var i=0; i<numberOfDays; i++){
        currentDate = i+1;
        fromDay.innerHTML += "<option value = " + currentDate + ">" + currentDate + "</option>";
    }
}

function pageLoad(){
    for(var i=0; i<numberOfYears; i++){
        fromYear.innerHTML += "<option value=" + years[i] + ">" + years[i] + "</option>"
    }
}