function opponentf()
{
	$.ajax({
		type: 'POST',
		url: "getkey/",
		success: function(arr){
			var type = arr[0];
			var key = arr[1];
			if(type == 1)
			{
				who = 0;
				switch(key)
				{
					case 1:
						KeyOpp(37);
						break;
					case 2:
						KeyOpp(39);
						break;
					case 3:
						KeyOpp(40);
						break;
					case 4:
						KeyOpp(38);
						break;
				}
			}
			if(type == 0)
			{
				clearInterval(opptime);			
			}
			//alert(type);
		},
		error: function(xhr, errmsg, err){
			alert(xhr.status + ": " + xhr.responseText);
		}	
	});
}
