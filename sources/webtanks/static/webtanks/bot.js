function bot(num)
{
	var type = 0;
	var Xb = 0;
	var Yb = 0;
	var t = 0;
	var fX = 0;
	var fY = 0;
	var numb = 0;
	if(dbot[num] == 1)
	{
		botx[num].clearRect(0, 0, 1034, 730);
		alert('bot died!');
	}
	else
	{
	$.ajax({
		type: 'POST',
		url: "bot/",
		data: {'name': 6,
			'num': num,},
		dataType: 'json',
		success: function(arr){
			type = arr[0];
			Xb = arr[1];
			Yb = arr[2];
			Xs[num + 1] = Xb;
			Ys[num + 1] = Yb;
			kind = arr[3];
			numbot = arr[4];
			if(type == 4)
			{
				botx[num].clearRect(0, 0, 1034, 730); 
				if(bnum == kind)
				{
					bnum = bnum + 4;
					kind = bnum;
				}					
				botchange(kind, Xs[num + 1], Ys[num + 1], num);
				bnum = kind;	
				$.ajax({
	  			type: 'POST',
	  			url: "bot/",
	  			data: {'name': 5,
					'num': num,},
				dataType: 'json',
	  			success: function(arr){
					type = arr[0];
					fX = arr[1];
					fY = arr[2];
					numb = arr[3];
					if(type==2)
					{
	   					//newimg.src = '/static/webtanks/images/bullet.png';
      						//newimg.onload = function(){
						//	btx.drawImage(newimg, 0, 0, 280, 280, fX, fY, 5, 5);
						//}
						
						//window.preventDefault();
						//alert("OK");						
						t = timeid;
						time[t] = setInterval(function() {flight(numb, t, num + 1)}, 20);
						timeid++;
					}
					else
					{
						//alert('game over');
					}
	  			},
				error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
					}	
					
			});
				bot(num);
			}
			else
			{
				alert('bot died!')
			}
	  	},
		error: function(xhr, errmsg, err){
				alert(xhr.status + ": " + xhr.responseText);
			}	
					
	});
	}	
}
