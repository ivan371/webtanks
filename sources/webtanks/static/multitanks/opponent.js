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
				//alert(key);
				who = 0;
				if(key == 1)
				{
					//alert(77);
					KeyOpp(37);
				}
				if(key == 2)
				{
					//alert(77);
					KeyOpp(39);
				}
				if(key == 3)
				{
					//alert(77);
					KeyOpp(40);
				}
				if(key == 4)
				{
					//alert(77);
					KeyOpp(38);
				}
				if(key == 5)
				{
					//alert(77);
					KeyOpp(32);
				}
				/*else
				{
				switch(key)
				{
					case 1:
						KeyOpp(37);
						break;
					case 2:
						alert(77);
						KeyOpp(39);
						break;
					case 3:
						KeyOpp(40);
						break;
					case 4:
						KeyOpp(38);
						break;
				}
				}*/
				opponentf();
			}
			if(type == 0)
			{
				return;
				clearInterval(opptime);			
			}
			//alert(type);
		},
		error: function(xhr, errmsg, err){
			alert(xhr.status + ": " + xhr.responseText);
		}	
	});
}
