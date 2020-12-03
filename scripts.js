var API_ENDPOINT = "https://<api_gw_endpoint>.amazonaws.com/dev"


function showOpinion() {


	$.ajax({
				url: API_ENDPOINT + '/myList',
				type: 'GET',
				success: function (response) {

	        jQuery.each(response, function(i,data) {

						if (data['published'] == true) {
	    					
						$("#opinion").append("\
						        <div> \
							    <div> \
            					<h3>" + data['message'] + "</h3> \
            					<p>" + data['name'] + ", " + data['firm'] + "</p> \
          						</div> \
        						</div>");
						}
	        });
				},
				error: function () {
						alert("error");
				}
		});
};

document.getElementById("addOpinion").onclick = function(){

	var inputData = {
		"name": $('#postName').val(),
		"firm": $('#postFirm').val(),
		"email" : $('#postEmail').val(),
		"message" : $('#postMessage').val()
	};

	$.ajax({
	      url: API_ENDPOINT + '/myOpinionsSaveAndSend',
	      type: 'POST',
	      data:  JSON.stringify(inputData)  ,
	      contentType: 'application/json; charset=utf-8',
	      success: function (response) {
					document.getElementById("postReturn").textContent="Thank you! Opinion added to database. Publication will be after acceptance adminisrator of this site.";
	      },
	      error: function () {
	          alert("error");
	      }
	  });
};


showOpinion()
