function opponentf()
{
	$.ajax({
		type: 'POST',
		url: "getkey/",
		success: function(arr){
			var type = arr[0];
			if(type == 1)
			{
				var key = arr[1];
				var str = arr[3];
				var X = 0;
				var Y = 0;
				XO = arr[4];
				YO = arr[5];
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
 					shootOp(flag, X, Y, 0, 0);
				who = 0;
				}
				else{
					Opflag = key;
					chop(key, arr[4], arr[5]);
 				}
				}
		},
		error: function(xhr, errmsg, err){
			alert(xhr.status + ": " + xhr.responseText);
		}	
	});
}
