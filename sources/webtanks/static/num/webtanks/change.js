function change(type, X, Y)
	{
		
		switch (type){	//1 - up; //2 - down //3 - right // 4 - left
		case 1:
			img.src = '/static/webtanks/images/tank2.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 2:
			img.src = '/static/webtanks/images/tank3.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 3:
			img.src = '/static/webtanks/images/tank1.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			
			break;
		case 4:
			img.src = '/static/webtanks/images/tank4.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 5:
			img.src = '/static/webtanks/images/tank6.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 6:
			img.src = '/static/webtanks/images/tank7.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 7:
			img.src = '/static/webtanks/images/tank5.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			
			break;
		case 8:
			img.src = '/static/webtanks/images/tank8.png';
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		}
	}
