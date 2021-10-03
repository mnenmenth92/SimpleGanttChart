const addTask = document.querySelector('[id=addTask]');
const addWeek = document.querySelector('[id=addWeek]');
const projects = document.querySelector('[id=projects]');
const daysTitles = document.getElementById('days-titles');
const jsonData = document.getElementById('id_data');
const currentDate = new Date(); 
let numOfWeeks = 2;
let currentMonth = currentDate.getUTCMonth();
let startDay = currentDate.getUTCDay();
let currentTask = 0;
const result = []





// add first, default task
console.log(projects)
console.log(addTask)
addNewTask()
fillDaysTitles()


addWeek.addEventListener('click', (e) => {

    if (e){
        e.preventDefault();
    };

    console.log(result);
    });



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
        
        let resultString = "abcdes";  // ToDo result -> string
        jsonData.value = resultString;
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



