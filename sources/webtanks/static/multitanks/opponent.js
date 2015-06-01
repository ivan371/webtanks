function opponentf()
{
	$.ajax({
		type: 'POST',
		url: "getkey/",
		success: function(arr){
			var type = arr[0];
			var key = arr[1];
			var str = arr[3];
			XO = arr[4];
			YO = arr[5];
			if(arr[6] == 2)
			{
				document.forms["win"].submit();
			}
			if(type == 1)
			{
				//alert(key);
				if(key == 5)
				{
					if(Opflag == 1)
					{
						X = XO + 5;
 						Y = YO + 9;
					}
					if(Opflag == 2)
					{
						X = XO + 5;
 						Y = YO + 7;
					}
					if(Opflag == 3)
					{
						X = XO + 7;
 						Y = YO + 5;
					}
					if(Opflag == 4)
					{
						X = XO + 7;
 						Y = YO + 5;
					}
					var flag = Opflag;
					X = XO;
					Y = YO;
 					shootOp(flag, X, Y, 0, 0);
				who = 0;
				}
				else{
					Opflag = key;
					chop(key, arr[4], arr[5]);
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
