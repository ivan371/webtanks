function flight(num, t)
	{
		var X = 0;
		var Y = 0;
		var type = 0;
		change(nums, XT, YT);
		if(nums < 5)
		{
			nums = nums + 4;
		}			
		else
		{
			nums = nums - 4;
		}
		window.addEventListener('keydown', whatKey, true);
		$.ajax({
	  			type: 'POST',
	  			url: "flight/",
				data: {'name': num,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					X = arr[1];
					Y = arr[2];					
					//num = arr[3];
					if(type==3)
					{
						btx.fillStyle = '#FFC552';
       						btx.rect(X, Y, 5, 5);
        					btx.fill();
							if(bulnum == 0)
							{	   					
								newimg.src = '/static/webtanks/images/bullet.png';
								bulnum = 1;
							}      			
							else
							{
								newimg.src = '/static/webtanks/images/bullet2.png';
								bulnum = 0;
							}			
							newimg.onload = function(){
							btx.drawImage(newimg, 0, 0, 280, 280, X, Y, 5, 5);
						}
						//setInterval(function() { flight(num) }, 20);
					}
					else
					{
						clearInterval(time[t]);					
						//alert('game over');
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
						//window.addEventListener('keydown', whatKey, true);
					}	
					
			});
	}
