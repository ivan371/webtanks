function whatKey(evt) {
        	oldBack = back;
		var type = 0;
		var fX = 0;
		var fY = 0;
		var num = 0;
		var numer = 0;
		var t = 0;
		switch (evt.keyCode) {
		case 37:
			datakey = 1;
			$.ajax({
	  			type: 'POST',
	  			url: "treating/",
	  			data: {'name': 1,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					XT = arr[1];
					YT = arr[2];
					Xs[0] = arr[1];
					Ys[0] = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(XT, YT, 24, 24);
        					ctx.fill();	
						if (nums != 1)
						{
							change(1, XT, YT);
							nums = 1;
						}
						else
						{
							change(5, XT, YT);
							nums = 5;
						}
					}
					else
					{
						alert('game over')
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
			break;

	        case 39:
			datakey = 2;
			 $.ajax({
	  			type: 'POST',
	  			url: "treating/",
	  			data: {'name': 2,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					XT = arr[1];
					YT = arr[2];
					Xs[0] = arr[1];
					Ys[0] = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(XT, YT, 24, 24);
        					ctx.fill();		
						if (nums != 2)
						{
							change(2, XT, YT);
							nums = 2;
						}
						else
						{
							change(6, XT, YT);
							nums = 6;
						}
					}
					else
					{
						alert('game over')
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});	         
			 break;

	        case 40:
			datakey = 3;
			$.ajax({
	  			type: 'POST',
	  			url: "treating/",
	  			data: {'name': 3,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					XT = arr[1];
					YT = arr[2];
					Xs[0] = arr[1];
					Ys[0] = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(XT, YT, 24, 24);
        					ctx.fill();	
						if (nums != 4)
						{
							change(4, XT, YT);
							nums = 4;
						}
						else
						{
							change(8, XT, YT);
							nums = 8;
						}
					}
					else
					{
						alert('game over')
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
          		break;

      	      	 case 38:
			datakey = 4;
			$.ajax({
	  			type: 'POST',
	  			url: "treating/",
	  			data: {'name': 4,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					XT = arr[1];
					YT = arr[2];
					Xs[0] = arr[1];
					Ys[0] = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(XT, YT, 24, 24);
        					ctx.fill();	
						if (nums != 3)
						{
							change(3, XT, YT);
							nums = 3;
						}
						else
						{
							change(7, XT, YT);
							nums = 7;
						}
					}
					else
					{
						alert('game over')
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
         		 break;
		case 32:
			$.ajax({
	  			type: 'POST',
	  			url: "treating/",
	  			data: {'name': 5,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					fX = arr[1];
					fY = arr[2];
					num = arr[3];
					XT = arr[4];
					YT = arr[5];
					Xs[0] = arr[4];
					Ys[0] = arr[5];
					if(type==2)
					{
	   					//newimg.src = '/static/webtanks/images/bullet.png';
      						//newimg.onload = function(){
						//	btx.drawImage(newimg, 0, 0, 280, 280, fX, fY, 5, 5);
						//}
						
						//window.preventDefault();
						t = timeid;
						time[t] = setInterval(function() {flight(num, t, 0)}, 20);
						timeid++;
					}
					else
					{
						alert('game over')
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
			break;
		//case 49:
		//	bot()
			//break;
       		 default:
        		  //alert("Please only use the arrow keys.");
		}

        }