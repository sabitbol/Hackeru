<html>
<head>



	<title>Wellcome To My Website!</title>
	<h1 style="color:blue;">THIS IS MY WEBSITE!</h1>
	<div class="content"></div>
		<p class="ext">
		This is the content text
		</p>

<form method="GET" action="<?php echo $_SERVER ['PHP_SELF'];>">
<input type="text" name="yourname" value="Enter your name">
<input type="submit" name="Submit" value="Click to submit">

</form>
<?php
	if(isset($_GET['submit']))
{
	$name = $_GET['yourname'];
	echo  "(Unsecure) Wellcome <b>$name</b>";
}
else {
echo "Please enter a name";
}
?>


<style>
	div.content {
		height: 10px;
		width: 100%;
	}


	body {
                height: 10px;
                width: 100%;
                font-family: courier;
                font-size: 160%;
        }


	p.ext {
		color: red
</style>
</head>


</html>
