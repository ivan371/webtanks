function botchange(kind, Xb, Yb, num)
	{
		switch (kind){	//1 - up; //2 - down //3 - right // 4 - left
		case 1:
			newimg.src = b1;
			numz[num] = 1;
			break;
		case 2:
			newimg.src = b2;
			numz[num] = 2;
			break;
		case 3:
			newimg.src = b3;
			numz[num] = 3;			
			break;
		case 4:
			newimg.src = b4;
			numz[num] = 4;
			break;
		case 5:
			newimg.src = b5;
			numz[num] = 5;
			break;
		case 6:
			newimg.src = b6;
			numz[num] = 6;
			break;
		case 7:
			newimg.src = b7;
			numz[num] = 7;			
			break;
		case 8:
			newimg.src = b8;
			numz[num] = 8;
			break;
		}
		newimg.onload = function(){
			botx[num].drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
		}
	}

