<html>
	<head>
    <script>
	var tankX = 10;
	var tankY = 710;
	var tank = new Image();
	var newtankctx;
	var back = new Image();
	var oldBack = new Image();
	function game() {
	   	if (canvas.getContext)
	   	{
            		var example = document.getElementById('example'),
            		ctx     = example.getContext('2d');
	    		ctx.fillStyle = 'orange';
    	    		ctx.fillRect(100, 100, example.width, example.height);
			back = ctx.getImageData(0, 0, 720, 1024);
	    		line_1     = example.getContext('2d');
	    		line_1.fillStyle = 'gray';
	    		line_1.fillRect(100, 100, 924, 6);
            		line_1.fillRect(100, 100, 6, 620);
	    		line_1.fillRect(100, 714, 924, 6);
	    		line_1.fillRect(1018, 100, 6, 620);
	    		line_1.fillRect(100, 200, 724, 6);
            		line_1.fillRect(300, 620, 724, 6);
            		line_1.fillRect(400, 300, 6, 250);
            		line_1.fillRect(700, 300, 6, 250);
	    		line_2     = example.getContext('2d');
	    		line_2.fillStyle = 'red';
            		line_2.fillRect(824, 200, 194, 6);
            		line_2.fillRect(106, 620, 200, 6);
            		line_2.fillRect(550, 206, 6, 414);
	    		line_2.fillRect(106, 420, 294, 6);
                	line_2.fillRect(706, 420, 312, 6);
			makeTank();
		}	
		gameLoop = setInterval(doGameLoop, 16);
		window.addEventListener('keydown', whatKey, true);
		
	}
	function makeTank()
	{
		ctx.fillStyle = "black";
       		ctx.rect(9, 708, 10, 712);
        	ctx.fill();
		ship = ctx.getImageData(0, 0, 720, 1024);
		ctx.putImageData(oldBack, 0, 0);
	}
	
	function doGameLoop() {
	        ctx.putImageData(oldBack, oldShipX, oldShipY);
	        ctx.putImageData(ship, shipX, shipY);
        }

        </script>
	</head>
	<body onload="game()">
		<h1>
      		Tanks
    		</h1>
    		<canvas id="myCanvas" width='1024' height='720'> </canvas>
    	</body>
</html>
