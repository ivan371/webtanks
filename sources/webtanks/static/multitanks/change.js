function change(type, X, Y)
	{
		if(who == 1)
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
			ctx.clearRect(X-10, Y-10, 40, 40);
      		img.onload = function(){		
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
		}
		else
		{
			switch (type){	//1 - up; //2 - down //3 - right // 4 - left
			case 1:
				img.src = b1;
				break;
			case 2:
				img.src = b2;
				break;
			case 3:
				img.src = b3;
				break;
			case 4:
				img.src = b4;
				break;
			case 5:
				img.src = b5;
				break;
			case 6:
				img.src = b6;
				break;
			case 7:
				img.src = b7;
				break;
			case 8:
				img.src = b8;
				break;
			}
			otx.clearRect(X-10, Y-10, 40, 40);
			img.onload = function(){	
				otx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
		}
	}
