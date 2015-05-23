function isbot(X, Y)
{
	//alert(numbots);
	for(var i = 0; i < numbots+1; i++)
	{
		if((X - 20 <= botX[i] && X + 20 >= botX[i] && Y - 20 <= botY[i] && Y + 20 >= botY[i]))
		{
			dbot[i] = 1;
		}
	}
}
function flight(num, t, numtank, Xc, Yc)
	{
		var X = 0;
		var Y = 0;
		var kind = 0;
		X = Xs[numtank];
		Y = Ys[numtank];
		kind = nums;
		if(numtank == 0)
		{
			change(kind, X, Y);
		}			
		/*else
		{
			kind = numz[numtank - 1];
			botchange(kind, X, Y, numtank - 1);
		}*/	
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
				data: {'name': num,
					'who': numtank,
					'X': Xc,
					'y': Yc},
				dataType: 'json',
	  			success: function(arr){
					kind = arr[0];
					X = arr[1];
					Y = arr[2];
					isbot(X, Y);					
					//num = arr[3];
					if(kind==3)
					{
						dtx.clearRect(0, 0, 1034, 730); 
							if(bulnum == 0)
							{	   					
								newimg.src = bul1;
								bulnum = 1;
							}      			
							else
							{
								newimg.src = bul2;
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
						if(kind == 6)
						{
							if(Y == 0)
							{
								//alert("lose");
								//document.location.href = '/static/webtanks/LOSE.html'
								/*$.ajax({
									type: 'POST',
									url: "lose/",
									error: function(xhr, errmsg, err){
										alert(xhr.status + ": " + xhr.responseText);
									}	
								});*/
								//document.location.href = '/static/webtanks/LOSE.html';
							}
							else
							{
								dbot[X] = 1;
								numbots--;
								if(numbots < 0)
								{
									alert("win");
									/*$.ajax({
										type: 'POST',
										url: "win/",
										error: function(xhr, errmsg, err){
											alert(xhr.status + ": " + xhr.responseText);
										}	
									});*/
									//document.location.href = '/static/webtanks/WIN.html';
								}
							}
						
						}
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
						//window.addEventListener('keydown', whatKey, true);
					}	
					
			});
	}
