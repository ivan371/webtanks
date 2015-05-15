function image(number, X, Y) {
	img.src = '/static/webtanks/images/tank' + number.toString() + '.png';
    img.onload = function() {
		ctx.restore();			
		ctx.drawImage(img, 100, 100, 800, 800, X, Y, 20, 20);
	}
}

function change(type, X, Y) {
		switch (type) {	//1 - up, 2 - down, 3 - right, 4 - left
		case 1:
			image(2, X, Y)
		break;
		case 2:
			image(3, X, Y)
		break;
		case 3:
			image(1, X, Y)
		break;
		case 4:
			image(4, X, Y)
		break;
		case 5:
			image(6, X, Y)
		break;
		case 6:
			image(7, X, Y)
		break;
		case 7:
			image(5, X, Y)
		break;
		case 8:
			image(8, X, Y)
		break;
		}
	}
