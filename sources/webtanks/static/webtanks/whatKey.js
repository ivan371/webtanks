function whatKey(evt) {
        	oldBack = back;
		var type = 0;
		var X = 0;
		var Y = 0;
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
					X = arr[1];
					Y = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(X, Y, 24, 24);
        					ctx.fill();	
						if (num != 1)
						{
							change(1, X, Y);
							num = 1;
						}
						else
						{
							change(5, X, Y);
							num = 5;
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
					X = arr[1];
					Y = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(X, Y, 24, 24);
        					ctx.fill();		
						if (num != 2)
						{
							change(2, X, Y);
							num = 2;
						}
						else
						{
							change(6, X, Y);
							num = 6;
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
					X = arr[1];
					Y = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(X, Y, 24, 24);
        					ctx.fill();	
						if (num != 4)
						{
							change(4, X, Y);
							num = 4;
						}
						else
						{
							change(8, X, Y);
							num = 8;
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
					X = arr[1];
					Y = arr[2];
					if(type==1)
					{
	   					ctx.fillStyle = '#FFC552';
       						ctx.rect(X, Y, 24, 24);
        					ctx.fill();	
						if (num != 3)
						{
							change(3, X, Y);
							num = 3;
						}
						else
						{
							change(7, X, Y);
							num = 7;
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
					X = arr[4];
					Y = arr[5];
					if(type==2)
					{
	   					newimg.src = '/static/webtanks/images/bullet.png';
      						newimg.onload = function(){
							btx.drawImage(newimg, 0, 0, 280, 280, fX, fY, 5, 5);
						}
						
						//window.preventDefault();
						t = timeid;
						time[t] = setInterval(function() {flight(num, t)}, 20);
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
       		 default:
        		  //alert("Please only use the arrow keys.");
		}

        }