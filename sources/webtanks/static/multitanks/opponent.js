function opponentf()
{
	$.ajax({
		type: 'POST',
		url: "getkey/",
		success: function(arr){
			var type = arr[0];
			var key = arr[1];
			var str = arr[3];
			if(type == 1)
			{
				//alert(key);
				who = 0;
				if(key == 5)
				{
					//alert(77);
					KeyOpp(32);
				}
				else{
				if (nums != key)
 				{
					change(key, arr[4], arr[5]);
					nums = key;
 				}
 				else
 				{
					change(key + 4, arr[4], arr[5]);
					nums = key + 4;
 				}
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
			}
			/*if(type == 0)
			{
				return;
				clearInterval(opptime);			
			}*/
			//opponentf();
			//alert(type);
		},
		error: function(xhr, errmsg, err){
			alert(xhr.status + ": " + xhr.responseText);
		}	
	});
}
