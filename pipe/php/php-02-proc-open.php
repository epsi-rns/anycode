#!/usr/bin/php
<?php # using PHP7

# http://php.net/manual/en/function.proc-open.php

$path    = __dir__."/../assets";
$cmdin   = 'conky -c '.$path.'/conky.lua';
$cmdout  = 'dzen2';

$descriptorspec = array(
   0 => array('pipe', 'r'),  // stdin
   1 => array('pipe', 'w'),  // stdout
   2 => array('pipe', 'w',)  // stderr
);

$procin  = proc_open($cmdin,  $descriptorspec, $pipein);
$procout = proc_open($cmdout, $descriptorspec, $pipeout);

if (is_resource($procin)) {
    while(!feof($pipein[1])) {
        $buffer = fgets($pipein[1]);
        fwrite($pipeout[0], $buffer);
    }

    proc_close($procin);
    proc_close($procout);
}
