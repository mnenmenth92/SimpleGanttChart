# SimpleGanttChart
Web site that allows to create  basic  Gantt chart. 
It's focused on short term projects which are partialy repetitive where there is no point for making detailed, complicated charts.

# Basic functions

- chart is created by adding tasks
- each task can be described with:
  - name
  - start date
  - end date
  - dependence - start date can't be set before some other task
- chart can be created just after web page is loaded
- chart can be saved as image
- chart is saved in editable version only when personal account is created and user is logged in
- every chart is stored on personal account of user. 
- each chart is categorized as 'In progress' or 'Finished' or 'Template'
- each category has its own list of charts
- 'Templates' can be used as a base while creating new project

# Technologies

- Django
- Bootstrap
- Javascript

