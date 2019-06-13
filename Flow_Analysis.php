<?php

error_reporting(0); 
define('LOG_FILEDIR','./logs'); 

if(is_dir(LOG_FILEDIR))
#echo "has "
;
else
{
mkdir(LOG_FILEDIR,0777,true);
# echo "Mkdir";
}
function waf() 
{ 
if (!function_exists('getallheaders')) { 
function getallheaders() { 
foreach ($_SERVER as $name => $value) { 
if (substr($name, 0, 5) == 'HTTP_') 
$headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value; 
} 
return $headers; 
} 
} 
$get = $_GET; 
$post = $_POST; 
$cookie = $_COOKIE; 
$header = getallheaders(); 
$files = $_FILES; 
$ip = $_SERVER["REMOTE_ADDR"]; 
$method = $_SERVER['REQUEST_METHOD']; 
$filepath = $_SERVER["SCRIPT_NAME"]; 
foreach ($_FILES as $key => $value) { 
$files[$key]['content'] = file_get_contents($_FILES[$key]['tmp_name']); 
file_put_contents($_FILES[$key]['tmp_name'], "virink"); 
}
unset($header['Accept']);
$input = array("Get"=>$get, "Post"=>$post, "Cookie"=>$cookie, "File"=>$files, "Header"=>$header);
logging($input);
}
function logging($var){ 
$filename = $_SERVER['REMOTE_ADDR'];
$LOG_FILENAME = LOG_FILEDIR."/".$filename.".txt";
$LOG_FILENAME_JustParam = LOG_FILEDIR."/".$filename."Just_param".".txt";
#echo $LOG_FILENAME;
$time = date("Y-m-d G:i:s");
#echo "\n";
#echo $filename;
#echo "\n";


file_put_contents($LOG_FILENAME, "\r\n".$time."\r\n".print_r($var, true), FILE_APPEND); 
file_put_contents($LOG_FILENAME,"\r\n".'http://'.$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF'].'?'.$_SERVER['QUERY_STRING'], FILE_APPEND);
file_put_contents($LOG_FILENAME,"\r\n***************************************************************",FILE_APPEND);

file_put_contents($LOG_FILENAME_JustParam, "\r\n".$time,FILE_APPEND); 
file_put_contents($LOG_FILENAME_JustParam,"  ".'http://'.$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF'].'?'.$_SERVER['QUERY_STRING'], FILE_APPEND);
}

waf(); 
?>