function shoot(flag, X, Y, hex)
{
	//alert(Xt);
	//alert(X);
	if((X - 20 <= Xt && X + 20 >= Xt && Y - 20 <= Yt && Y + 20 >= Yt))
	{
		//alert("YOU LOSE");
		document.location.href = '/static/webtanks/LOSE.html'
	}
	else
	{
	switch(flag)
	{
		case 1:
			if(hex != 808080)
			{
				var img_data = wtx.getImageData(X, Y, 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				dtx.clearRect(X-5, Y-5, 20, 20); 
				if(bulnum == 0)
				{	   					
					newimg.src = '/static/webtanks/images/bullet.png';
					bulnum = 1;
				}      			
				else
				{
					newimg.src = '/static/webtanks/images/bullet2.png';
					bulnum = 0;
				}			
				newimg.onload = function(){
					dtx.drawImage(newimg, 0, 0, 280, 280, X, Y, 5, 5);
				}
				setTimeout(function(){shoot(flag, X - 5, Y, hex)}, 20);
			}
			else
				dtx.clearRect(X-5, Y-5, 20, 20);
			break;
		case 2:
			if(hex != 808080)
			{
				var img_data = wtx.getImageData(X + 24, Y, 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				dtx.clearRect(X-5, Y-5, 20, 20); 
				if(bulnum == 0)
				{	   					
					newimg.src = '/static/webtanks/images/bullet.png';
					bulnum = 1;
				}      			
				else
				{
					newimg.src = '/static/webtanks/images/bullet2.png';
					bulnum = 0;
				}			
				newimg.onload = function(){
					dtx.drawImage(newimg, 0, 0, 280, 280, X, Y, 5, 5);
				}
				setTimeout(function(){shoot(flag, X + 5, Y, hex)}, 20);
			}
			else
				dtx.clearRect(X-5, Y-5, 20, 20);
			break;
		case 3:
			if(hex != 808080)
			{
				var img_data = wtx.getImageData(X, Y + 24, 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				dtx.clearRect(X-5, Y-5, 20, 20);  
				if(bulnum == 0)
				{	   					
					newimg.src = bul1;
					bulnum = 1;
				}      			
				else
				{
					newimg.src = bul2;
					bulnum = 0;
				}			
				newimg.onload = function(){
					dtx.drawImage(newimg, 0, 0, 280, 280, X, Y, 5, 5);
				}
				setTimeout(function(){shoot(flag, X, Y + 5, hex)}, 20);
			}
			else
				dtx.clearRect(X-5, Y-5, 20, 20);
			break;
		case 4:
			if(hex != 808080)
			{
				var img_data = wtx.getImageData(X, Y, 1, 1).data;
      				var R = img_data[0];
     				var G = img_data[1];
     				var B = img_data[2];  var rgb = R + ',' + G + ',' + B;
      				// конвертируем из RGB в HEX
      				var hex = rgbToHex(R,G,B);
				dtx.clearRect(X-5, Y-5, 20, 20); 
				if(bulnum == 0)
				{	   					
					newimg.src = '/static/webtanks/images/bullet.png';
					bulnum = 1;
				}      			
				else
				{
					newimg.src = '/static/webtanks/images/bullet2.png';
					bulnum = 0;
				}			
				newimg.onload = function(){
					dtx.drawImage(newimg, 0, 0, 280, 280, X, Y, 5, 5);
				}
				setTimeout(function(){shoot(flag, X, Y - 5, hex)}, 20);
			}
			else
				dtx.clearRect(X-5, Y-5, 20, 20);
			break;
	}		
	}
}
