function setEvents()
{
    //Fetch user events
    var events = [{title : "Plantes à garder",start:"2023-03-07",end:"2023-03-27"}]
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {events:events});
    calendar.render();
}