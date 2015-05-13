function botchange(kind, Xb, Yb)
	{
		
		switch (kind){	//1 - up; //2 - down //3 - right // 4 - left
		case 1:
			newimg.src = '/static/webtanks/images/bot2.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			break;
		case 2:
			newimg.src = '/static/webtanks/images/bot3.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			break;
		case 3:
			newimg.src = '/static/webtanks/images/bot1.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			
			break;
		case 4:
			newimg.src = '/static/webtanks/images/bot4.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			break;
		case 5:
			newimg.src = '/static/webtanks/images/bot6.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			break;
		case 6:
			newimg.src = '/static/webtanks/images/bot7.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			break;
		case 7:
			newimg.src = '/static/webtanks/images/bot5.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			
			break;
		case 8:
			newimg.src = '/static/webtanks/images/bot8.png';
      			newimg.onload = function(){
				btx.drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
			}
			break;
		}
	}

