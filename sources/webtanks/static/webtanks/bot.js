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
			Xb = arr[1];
			Yb = arr[2];
			kind = arr[3];
			if(type == 4)
			{
				btx.clearRect(0, 0, 1034, 730); 
				if(bnum == kind)
				{
					bnum = bnum + 4;
					kind = bnum;
				}					
				botchange(kind, Xb, Yb);
				bnum = kind;
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
