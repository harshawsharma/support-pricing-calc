
// Attach a submit handler to the form
$( "#calcform" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();

  // Get some values from elements on the page:
  var $form = $( this ),
    term = $form.find( "input[name=MonthlyBill]" ).val(),
    url = $form.attr("action");
   
  $(function(){
    $(".ccfield-prepend1").empty();
  });

  // Send the data using post
	var posting = $.post( url, JSON.stringify({ "MonthlyBill": term }) );
  
  // Put the results in a div
  posting.done(function( apiresponse ) {
    $.each(apiresponse, function () {
      $.each(this, function (name, value) {
        //console.log(name + '=' + value);
        $( ".ccfield-prepend1" ).append(name+value+"<br/>");
      });
    });
 	});
});