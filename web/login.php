<DOCTYPE html>
<html>
<head>
<title> Hello Everyone!</title>
<style>
		body {
                     	width: 70px;
			margin: 0 auto;
                     }
		.ptitle {
			color: blue;
			text-align: center;
			padding: 30px 0 10px 0
			border-bottom: 3px solid blue;
			}
		.logincon {
			width: 400px;
			height: 200px;
			margin: 0 auto;
			text-align: center;
			border: 1px solid black;
			  }

		form > * {
			margin-bottom: 10px;
			 }
</style>
</head>
<body>
	<?php
		$name = "shimi";
		$password
	?>
	<h1 class="ptitle">Admin Panel</h1>

	<div class="logincon">
		<h2>Login</h2>
		<form method="post">
			<input type="text" name="usr" placeholder="Username" />
			<br />
			<input type="password" name="pass" placeholder="Password" />
			<br />
		<form/>
	<div/>
</body>
</html>
