function search_oponent()
{
	$.ajax({
		type: 'POST',
  		url: "choose/",
		dataType: 'json',
  		success: function(res){
  			if(res == 1)
			{
				clearInterval(time);
				document.location.href = '/static/webtanks/WIN.html';
				document.form["redirect"].submit();
			}
		}
		error: function(xhr, errmsg, err){
					alert(xhr.status + ": " + xhr.responseText);
				}					
			});
}
