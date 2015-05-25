function shootcase(XImageData, YImageData, XTimeout, YTimeout, flag, X, Y, hex)
{
		//alert(Xt);
		//alert(X);
		if(X - 15 <= Xt && X + 15 >= Xt && Y - 15 <= Yt && Y + 15 >= Yt)
		{
			//alert("YOU LOSE");
			document.location.href = '/static/webtanks/LOSE.html'
		}
		if(hex != 808080)
		{
			if(hex == "BCF4FF")
			{
				dtx.clearRect(X-5, Y-5, 20, 20);
				wtx.clearRect(X-5, Y-5, 20, 20);
			}			
			else
			{
				var img_data = wtx.getImageData(X + XImageData, Y + YImageData, 1, 1).data;
    				var R = img_data[0];
    				var G = img_data[1];
    				var B = img_data[2];  
    				var rgb = R + ',' + G + ',' + B;
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
				setTimeout(function(){shoot(flag, X + XTimeout, Y + YTimeout, hex)}, 20);
			}
		}
		else
		{
			dtx.clearRect(X-5, Y-5, 20, 20);
		}
}

function shoot(flag, X, Y, hex)
{
	switch(flag)
	{
		case 1:
			shootcase(0, 0, - 5, 0, 1, X, Y, hex)
			break;
		case 2:
			shootcase(24, 0, 5, 0, 2, X, Y, hex)
			break;
		case 3:
			shootcase(0, 24, 0, 5, 3, X, Y, hex)
			break;
		case 4:
			shootcase(0, 0, 0, -5, 4, X, Y, hex)
			break;
	}		
}
