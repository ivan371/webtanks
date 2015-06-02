function win(X, Y, kind)
{
	if (kind == 0)
	{
		if(X - 15 <= XT && X + 15 >= XT && Y - 15 <= YT && Y + 15 >= YT)
		{
			clearInterval(optime);
			document.forms["lose"].submit();
		}
	}
	else
	{
		//alert(X);
		//alert(Y);
		//alert(XO);
		//alert(YO);
		if(X - 15 <= XO && X + 15 >= XO && Y - 15 <= YO && Y + 15 >= YO)
		{
			clearInterval(optime);
			document.forms["win"].submit();
		}
	}
}

function putdraw()
{
	ctx.clearRect(0, 0, 690, 1024);
	img.onload = function(){		
		ctx.drawImage(img, 100, 100, 800, 800, XT, YT, 20, 20);
	}
	otx.clearRect(0, 0, 1024, 690);
	back.onload = function(){	
		otx.drawImage(back, 100, 100, 800, 800, XO, YO, 20, 20);
	}
}
