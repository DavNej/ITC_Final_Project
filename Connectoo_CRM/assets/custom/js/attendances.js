var attendances = {};

attendances.changeToAbsent = function() {
    attendances.change = $(this).closest('tr').find('td .label.label-sm.label-default.checkin');
    attendances.change.removeClass('label label-sm label-default checkin');
    attendances.change.addClass('label label-sm label-not-arrive not');
    attendances.change.html('Absent');
    attendances.numAbsent = $('td .label.label-sm.label-not-arrive.not').length;
    attendances.numCheckin = $('td .label.label-sm.label-default.checkin').length;
    $('.number.absent').html(attendances.numAbsent);
    $('.number.checkin').html(attendances.numCheckin);
    
};

attendances.changeToCheckin = function() {
    attendances.change = $(this).closest('tr').find('td .label.label-sm.label-not-arrive.not');
    attendances.change.removeClass('label label-sm label-not-arrive not');
    attendances.change.addClass('label label-sm label-default checkin');
    attendances.change.html('Check in');
    attendances.numAbsent = $('td .label.label-sm.label-not-arrive.not').length;
    attendances.numCheckin = $('td .label.label-sm.label-default.checkin').length;
    $('.number.absent').html(attendances.numAbsent);
    $('.number.checkin').html(attendances.numCheckin);
    
};

attendances.numAbsent = $('td .label.label-sm.label-not-arrive.not').length;
attendances.numCheckin = $('td .label.label-sm.label-default.checkin').length;

$(document).ready(
    function(){
        $('.notarrive').bind("click", attendances.changeToAbsent);
        $('.check-in').bind("click", attendances.changeToCheckin);
        console.log(attendances.numAbsent);
        $('.number.absent').html(attendances.numAbsent);
        $('.number.checkin').html(attendances.numCheckin);
    }
);


