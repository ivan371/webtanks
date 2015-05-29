function change(type, X, Y)
	{
		
		switch (type){	//1 - up; //2 - down //3 - right // 4 - left
		case 1:
			img.src = t1;
			break;
		case 2:
			img.src = t2;
			break;
		case 3:
			img.src = t3;
			break;
		case 4:
			img.src = t4;
			break;
		case 5:
			img.src = t5;
			break;
		case 6:
			img.src = t6;
			break;
		case 7:
			img.src = t7;
			break;
		case 8:
			img.src = t8;
			break;
		}
      	img.onload = function(){
			ctx.restore();			
			ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
		}
	}
