function chop(type, X, Y)
{
		//1 - up; //2 - down //3 - right // 4 - left
			if(Optype != type)
			{
				Optype = type;
			}
			else
			{
				Optype = Optype + 4;
				type = type + 4;
			}
			if(type == 1)
			{
				newimg.src = b1;
			}
			if(type == 2)
			{
				newimg.src = b2;
			}
			if(type == 3)
			{
				newimg.src = b3;
			}
			if(type == 4)
			{
				newimg.src = b4;
			}
			if(type == 14)
			{
				newimg.src = b5;
			}
			if(type == 24)
			{
				newimg.src = b6;
			}
			if(type == 34)
			{
				newimg.src = b7;
			}
			if(type == 44)
			{
				newimg.src = b8;
			}
			//ctx.clearRect(X-30, Y-30, 80, 80);
			otx.clearRect(X-10, Y-10, 40, 40);
			//alert(type);
			//alert(X);
			//alert(Y);
			//newimg.src = b2;
			newimg.onload = function(){	
				otx.drawImage(newimg, 100, 100, 800, 800, X, Y, 20, 20);
			}
}