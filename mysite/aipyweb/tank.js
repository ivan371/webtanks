function handler(event) {
	var KEY_CODE = {
		LEFT: 37,
		UP: 38,
		RIGHT: 39,
		DOWN: 40
	}
	var xhr = new XMLHttpRequest();
	switch(event.keyCode) {
		case KEY_CODE.LEFT:
			xhr.send(1);
		break;
		case KEY_CODE.UP:
			xhr.send(2);
		break;
		case KEY_CODE.RIGHT:
			xhr.send(3);
		break;
		case KEY_CODE.DOWN:
			xhr.send(4);
		break;
		default:

	}
}
window.addEventListener('keydown', handler, false);
window.addEventListener('keypress', handler, false);
window.addEventListener('keyup', handler, false);
