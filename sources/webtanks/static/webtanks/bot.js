function bot()
{
	var type = 0;
	var Xb = 0;
	var Yb = 0;
	$.ajax({
		type: 'POST',
		url: "bot/",
		data: {'name': 6,},
		dataType: 'json',
		success: function(arr){
			type = arr[0];
			X = arr[1];
			Y = arr[2];
			kind = arr[3];
			if(type == 4)
			{
				ctx.fillStyle = '#FFC552';
      				ctx.rect(Xb, Yb, 24, 24);
        			ctx.fill();	
				botchange(kind, Xb, Yb);
				bot();
			}
			else
			{
				alert('bot died!')
			}
	  	},
		error: function(xhr, errmsg, err){
				alert(xhr.status + ": " + xhr.responseText);
			}	
					
	});
}
