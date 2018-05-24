"use strict";
$(function(){
    var dataForm = $("#dataForm");
    var btnCancel = $("#btnCancel");
    var btnNew = $("#btnNew");

    //Hide form and cancel button on page load
    btnCancel.hide();
    dataForm.hide();

    getAppointments();

    //btnNew click event
    btnNew.click(NewAppointment);

    //btnCancel Click event
    btnCancel.click(CancelForm);


    //cancel form
    function CancelForm(evt){
        btnNew.text("NEW");
        btnCancel.hide();
        dataForm.hide();
    }//end function

    //Add appointment record to DB
    function NewAppointment(evt){  
        if( btnNew.text() == "NEW"){
            btnNew.text("ADD");
            dataForm.show();
            btnCancel.show();
        }
        else{
            var txtDate =  $("#txtDate").val();
            var txtTime = $("#txtTime").val();
            var txtDesc = $("#txtDesc").val().trim();

            var date1 = new Date(txtDate + ' ' + txtTime);

            //validate and submit form
            if(txtDate == '' || txtTime == '' || txtDesc == ''){
                $("#errorDisplay").text("All fields are required required!!!");
            }
            else if(Date.parse(date1) > Date.parse(new Date())){
                $("#apptForm").submit();
            }
            else
                $("#errorDisplay").text("The date and time must be in the future!!!");

        }
    }//end function

    //search button click event
    $("#btnSearch").click(function(){
        getAppointments( $("#txtSearch").val() );

    });//end search button click event

    function getAppointments(searchText){    
            $.ajax({
                type: 'GET',
                url: '/cgi-bin/pservice/getappt.cgi',
                data: { 'searchString': searchText },
                success: function(results) {

                    $("#storedData").empty().append("<tr><th>Date</th><th>Time</th><th>Description</th></tr>"); //empty table to reload contents
                    //loop through JSON objects and display details
                    for(let result of results){
                        var date = new Date(result.Appt);

                        $("#storedData")
                        .append("<tr><td>" +date.toLocaleDateString('en-US',{month: 'long', day: 'numeric'})  + 
                        "</td><td>" + date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) +
                        "</td><td>" + result.Desc + 
                        "</td></tr>");

                    }
                    //console.log(results);                    
                },
                error: function() {
                    alert("Something Went Wrong!!!");
                }
            });
    }
});