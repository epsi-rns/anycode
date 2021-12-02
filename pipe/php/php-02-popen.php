#!/usr/bin/php
<?php # using PHP7

# http://php.net/manual/en/function.popen.php

$path    = __dir__."/../assets";
$cmdin   = 'conky -c '.$path.'/conky.lua';
$cmdout  = 'less'; # or 'dzen2'

# handle
$pipein  = popen($cmdin,  "r");
$pipeout = popen($cmdout, "w");

while(!feof($pipein)) {
    $buffer = fgets($pipein);
    fwrite($pipeout, $buffer);
    flush();
}

pclose($pipein);
pclose($pipeout);
