function image(number1, number2, num, Xb, Yb) {
	newimg.src = '/static/webtanks/images/bot'+ number1.toString() + '.png';
    newimg.onload = function() {
		botx[num].drawImage(newimg, 100, 100, 800, 800, Xb, Yb, 20, 20);
	}
	numz[num] = number2;
}

function botchange(kind, Xb, Yb, num) {
		switch (kind) {	//1 - up, 2 - down, 3 - right, 4 - left
		case 1:
			image(2, 1, num, Xb, Yb)
		break;
		case 2:
			image(3, 2, num, Xb, Yb)
		break;
		case 3:
			image(4, 3, num, Xb, Yb)
			break;
		case 4:
			image(1, 4, num, Xb, Yb)
		break;
		case 5:
			image(6, 5, num, Xb, Yb)
			break;
		case 6:
			image(7, 6, num, Xb, Yb)
			break;
		case 7:
			image(8, 7, num, Xb, Yb)
			break;
		case 8:
			image(5, 8, num, Xb, Yb)
			break;
		}
}

