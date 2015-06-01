function win(X, Y, kind)
{
	if (kind == 0)
	{
		if(X - 15 <= XT && X + 15 >= XT && Y - 15 <= YT && Y + 15 >= YT)
		{
			document.forms["lose"].submit();
		}
	}
	else
	{
		if(X - 15 <= XO && X + 15 >= XO && Y - 15 <= YO && Y + 15 >= YO)
		{
			document.forms["win"].submit();
		}
	}
}

