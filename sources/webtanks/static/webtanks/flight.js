function flight(num, t)
	{
		var X = 0;
		var Y = 0;
		var kind = 0;
		X = XT;
		Y = YT;
		kind = nums;
		change(kind, X, Y);
		if(nums < 5)
		{
			nums = nums + 4;
		}			
		else
		{
			nums = nums - 4;
		}
		//window.addEventListener('keydown', whatKey, true);
		$.ajax({
	  			type: 'POST',
	  			url: "flight/",
				data: {'name': num,},
				dataType: 'json',
	  			success: function(arr){
					kind = arr[0];
					X = arr[1];
					Y = arr[2];					
					//num = arr[3];
					if(kind==3)
					{
						dtx.clearRect(0, 0, 1034, 730); 
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
							dtx.drawImage(newimg, 0, 0, 280, 280, X, Y, 5, 5);
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
