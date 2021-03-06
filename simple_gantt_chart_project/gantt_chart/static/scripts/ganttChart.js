const addTask = document.querySelector('[id=addTask]');
const addWeek = document.querySelector('[id=addWeek]');
const projects = document.querySelector('[id=projects]');
const daysTitles = document.getElementById('days-titles');
const jsonData = document.getElementById('id_data');
const projectName = document.getElementById('projectName')
const projectButtons = document.getElementsByClassName('project-selection-button')
const currentDate = new Date(); 
let numOfWeeks = 2;
let currentMonth = currentDate.getUTCMonth();
let startDay = currentDate.getUTCDay();
let currentTask = 0;
const result = []
// get last url element
const url = window.location.href
let currentSegment = url.split("/").pop();
// assuming there is only one url parameter
currentSegment = currentSegment.substring(13, currentSegment.length-1);




// add first, default task
addNewTask();
fillDaysTitles();
console.log(currentSegment)

// fill project name
projectName.value = currentSegment

// add events to buttons in project list
Array.prototype.forEach.call(projectButtons, function(projectButton) {
    projectButton.addEventListener('click', event => {
      console.log(projectButton.value)
    })

    // show selected project
    if (projectButton.name == currentSegment){

        addClasses(projectButton,["bg-secondary", "text-white"]);
    }


});


addWeek.addEventListener('click', (e) => {

    if (e){
        e.preventDefault();
    };

    console.log(result);
    });

    
function updateResultJson(){

    combinedData = {
        projectName:projectName.value,
        tasks: result
    };
    let resultString = JSON.stringify(combinedData);
    jsonData.value = resultString;
    console.log(resultString)
    };


addTask.addEventListener('click', (e) => {

addNewTask(e)
});

function addNewTask(event=null){

    if (event){
        event.preventDefault();
    };


    console.log('add task');
    // add task to result
    const taskElement = {
        id: currentTask,
        taskName: '',
        days: []
    };
    result.push(taskElement)

    // create elements
    // row div
    const rowDiv = document.createElement('div');
    addClasses(rowDiv,["row", "border", "border-top-0", "border-secondary", "rounded"]);
    // name div
    const nameDiv = document.createElement('div');
    addClasses(nameDiv,["col-md-3", "rounded", "p-3"]);
    // name input
    const nameInput = document.createElement('input');
    addClasses(nameInput,["align-middle", "form-control"]);
    nameInput.setAttribute("id", `${currentTask}`); 
    nameInput.addEventListener('input', () => {
        console.log(`switched button id: ${nameInput.id}, its value:${nameInput.value}`);
        result[parseInt(nameInput.id)].taskName = nameInput.value;
        updateResultJson()

    });

    // days div
    const daysDiv = document.createElement('div');
    addClasses(daysDiv,["col-md-9", "rounded", "p-3"]);
    // days
    for (let i =0; i < numOfWeeks * 7; i++){

        dayNumber = getDay(i)  // temporary ToDo
        monthNumber = currentMonth  // temporary ToDo
        const oneDay = document.createElement('button');
        addClasses(oneDay,["align-middle", "btn", "btn-sm", "btn-outline-secondary", "pr-auto"]);
        oneDay.setAttribute("style", "width: 40px; height: 25px;");
        oneDay.setAttribute("id", `${currentTask}.${monthNumber}.${dayNumber}`);  // each day id to find out which day was selected
        oneDay.addEventListener('click', () => {
            console.log(`switched button id: ${oneDay.id}, its value:${oneDay.classList.contains('bg-warning')}`);
            oneDay.classList.toggle('bg-warning');
            let selectedTaskNum = result[parseInt(oneDay.id.split('.')[0])]
            if (oneDay.classList.contains('bg-warning')){
                selectedTaskNum.days.push(oneDay.id);
            }else{
                let dayIndex =  selectedTaskNum.days.indexOf(oneDay.id)
                selectedTaskNum.days.splice(dayIndex, 1)
            };
            updateResultJson()
            console.log(selectedTaskNum.days)
        });

        daysDiv.appendChild(oneDay);
        
    
    };
    console.log(result)


    nameDiv.appendChild(nameInput);
    rowDiv.appendChild(nameDiv);
    rowDiv.appendChild(daysDiv);
    projects.appendChild(rowDiv);

    currentTask++

}

function fillDaysTitles(){
    for (let i =0; i < numOfWeeks * 7; i++){
        const oneDayTitle = document.createElement('div');
        addClasses(oneDayTitle,["align-middle","d-inline-block"]);
        oneDayTitle.setAttribute("style", "width: 40px; height: 25px;");
        currentDay = startDay+i
        oneDayTitle.innerHTML = `${currentDay}.${currentMonth}`;
        daysTitles.appendChild(oneDayTitle);

        };


};

function getDay(buttonNumber){
        return(startDay + buttonNumber)
};



function addClasses(element, classes){
    for (let i =0; i < classes.length; i++){
        element.classList.add(classes[i])
    
    };


};



