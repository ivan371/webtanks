function send_for_pressing(keydata, numchange) {
			datakey = keydata,
 			$.ajax({
 	  			type: 'POST',
 	  			url: "treating/",
	  			data: {'name': keydata,},
 				dataType: 'json',
 	  			success: function(arr){
 					type = arr[0];
 					XT = arr[1];
 					YT = arr[2];
 					Xs[0] = arr[1];
 					Ys[0] = arr[2];
 					Xt = XT;
					Yt = YT;
 					if(type==1)
 					{
 	   					ctx.fillStyle = '#FFC552';
        						ctx.rect(XT, YT, 24, 24);
         					ctx.fill();
						if (nums != numchange)
 						{
							change(numchange, XT, YT);
							nums = numchange;
 						}
 						else
 						{
							change(numchange + 4, XT, YT);
							nums = numchange + 4;
 						}
 					}
 					else
 					{
						//alert('Oops!')
 					}
 	  			},
 				error: function(xhr, errmsg, err){
 						alert(xhr.status + ": " + xhr.responseText);
 					}
 			});
}

function whatKey(evt) {
        oldBack = back;
		var type = 0;
		var fX = 0;
		var fY = 0;
		var num = 0;
		var numer = 0;
		var t = 0;
		var j = 0;
		for(var i = 0; i < numbots; i++)
		{
			if(dbot[i] == 1)
			{
				j++;
			}
		}
		if(j == numbots)
		{
			/*$.ajax({
					type: 'POST',
					url: "win/",
					error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
				});*/
			document.forms["win"].submit();
		}
		switch (evt.keyCode) {
		case 37:
			send_for_pressing(1, 1)
		break;
	    case 39:
			send_for_pressing(2, 2)
		break;
	    case 40:
			send_for_pressing(3, 4)
        break;
      	case 38:
			send_for_pressing(4, 3)
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
						//alert('Oops!')
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
