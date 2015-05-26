function rgbToHex(R,G,B) {return toHex(R)+toHex(G)+toHex(B)}
function toHex(n) {
      n = parseInt(n,10);
      if (isNaN(n)) return "00";
      n = Math.max(0,Math.min(n,255));
      return "0123456789ABCDEF".charAt((n-n%16)/16)  + "0123456789ABCDEF".charAt(n%16);
    }
function bot(num, perc)
{
	var type = 0;
	var Xb = 0;
	var Yb = 0;
	var t = 0;
	var fX = 0;
	var fY = 0;
	var numb = 0;
	var elem = 0;
	var X = 0;
	var Y = 0;
	if(dbot[num] == 1)
	{
		botx[num].clearRect(0, 0, 1034, 730);
		//alert('bot died!');
	}
	else
	{
	
		var flag = Math.floor((Math.random() * 4) + 1);
		switch(flag)
		{
			case 1:
				botX[num] = botX[num] - 5;
				var img_data = wtx.getImageData(botX[num], botY[num], 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				if(hex == 808080)
				{
					flag = 2;
					botX[num] = botX[num] + 5;
				}
				if(perc == 3)
				{
					X = botX[num];
					Y = botY[num] + 11;
					perc = 0;
					shoot(flag,X, Y, 0);
				}
				else
				{
					perc++;
				}
				break;
			case 2:
				botX[num] = botX[num] + 5;
				var img_data = wtx.getImageData(botX[num] + 24, botY[num], 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				if(hex == 808080)
				{
					flag = 1;
					botX[num] = botX[num] - 5;
				}
				if(perc == 3)
				{
					X = botX[num];
					Y = botY[num] + 11;
					perc = 0;
					shoot(flag, X, Y, 0);
				}
				else
				{
					perc++;
				}
				break;
			case 3:
				botY[num] = botY[num] + 5;
				var img_data = wtx.getImageData(botX[num], botY[num] + 24, 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				if(hex == 808080)
				{
					flag = 4;
					botY[num] = botY[num] - 5;
				}
				if(perc == 3)
				{
					X = botX[num] + 11;
					Y = botY[num];
					perc = 0;
					shoot(flag, X, Y, 0);
				}
				else
				{
					perc++;
				}
				break;
			case 4:
				botY[num] = botY[num] - 5;
				var img_data = wtx.getImageData(botX[num], botY[num], 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				if(hex == 808080)
				{
					flag = 3;
					botY[num] = botY[num] + 5;
				}
				if(perc == 3)
				{
					X = botX[num] + 11;
					Y = botY[num];
					perc = 0;
					shoot(flag, X, Y, 0);
				}
				else
				{
					perc++;
				}
			}				
		botx[num].clearRect(botX[num]-5, botY[num]-5, 30, 30);					
		if(bnum[num] == flag)
		{
			bnum[num] = bnum[num] + 4;
			flag = bnum[num];
		}	
		botchange(flag, botX[num], botY[num], num);
		bnum[num] = flag;
		var t = Math.floor((Math.random() * 800))
		setTimeout(function(){bot(num, perc)}, t);
		/*$.ajax({
	  			type: 'POST',
	  			url: "shot/",
	  			data: {'name': 1,
					'num': num,
					'flag': flag,
					'X': Xr,
					'Y': Yr},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					fX = arr[1];
					fY = arr[2];
					numb = arr[3];
					if(type==2)
					{
	   					//newimg.src = '/static/webtanks/images/bullet.png';
      						//newimg.onload = function(){
						//	btx.drawImage(newimg, 0, 0, 280, 280, fX, fY, 5, 5);
						//}
						
						//window.preventDefault();
						//alert("OK");						
						t = timeid;
						time[t] = setInterval(function() {flight(numb, t, num + 1, Xr, Yr)}, 20);
						timeid++;
					}
					else
					{
						//alert('game over');
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
		var t = Math.floor((Math.random() * 800))
		setTimeout(function(){bot(num, Xr, Yr)}, t);*/
			
	/*$.ajax({
		type: 'POST',
		url: "bot/",
		data: {'name': 6,
			'num': num,},
		dataType: 'json',
		success: function(arr){
			type = arr[0];
			Xb = arr[1];
			Yb = arr[2];
			Xs[num + 1] = Xb;
			Ys[num + 1] = Yb;
			kind = arr[3];
			numbot = arr[4];
			if(type == 4)
			{
				botx[num].clearRect(0, 0, 1034, 730); 
				if(bnum == kind)
				{
					bnum = bnum + 4;
					kind = bnum;
				}					
				botchange(kind, Xs[num + 1], Ys[num + 1], num);
				bnum = kind;	
				$.ajax({
	  			type: 'POST',
	  			url: "bot/",
	  			data: {'name': 5,
					'num': num,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					fX = arr[1];
					fY = arr[2];
					numb = arr[3];
					if(type==2)
					{
	   					//newimg.src = '/static/webtanks/images/bullet.png';
      						//newimg.onload = function(){
						//	btx.drawImage(newimg, 0, 0, 280, 280, fX, fY, 5, 5);
						//}
						
						//window.preventDefault();
						//alert("OK");						
						t = timeid;
						time[t] = setInterval(function() {flight(numb, t, num + 1)}, 20);
						timeid++;
					}
					else
					{
						//alert('game over');
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
				bot(num, Xr, Yr);
			}
			else
			{
				alert('bot died!')
			}
	  	},
		error: function(xhr, errmsg, err){
				alert(xhr.status + ": " + xhr.responseText);
			}	
					
	});*/
	}	
}
