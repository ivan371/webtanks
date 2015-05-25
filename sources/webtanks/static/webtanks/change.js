function change(type, X, Y)
	{
		
		switch (type){	//1 - up; //2 - down //3 - right // 4 - left
		case 1:
			img.src = t1;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 2:
			img.src = t2;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 3:
			img.src = t3;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			
			break;
		case 4:
			img.src = t4;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 5:
			img.src = t5;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 6:
			img.src = t6;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		case 7:
			img.src = t7;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			
			break;
		case 8:
			img.src = t8;
      			img.onload = function(){
				ctx.restore();			
				ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
			}
			break;
		}
	}
