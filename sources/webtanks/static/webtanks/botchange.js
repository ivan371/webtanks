function change(type, X, Y)
	{
		
		switch (type){	//1 - up; //2 - down //3 - right // 4 - left
		case 1:
			img.src = '/static/webtanks/images/bot2.png';
      			img.onload = function(){
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 2:
			img.src = '/static/webtanks/images/bot3.png';
      			img.onload = function(){
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 3:
			img.src = '/static/webtanks/images/bot1.png';
      			img.onload = function(){
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			
			break;
		case 4:
			img.src = '/static/webtanks/images/bot4.png';
      			img.onload = function(){
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		}
	}

