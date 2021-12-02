#!/usr/bin/php
<?php # using PHP7

$timeformat = '%a %b %d %H:%M:%S';

$cmdout  = 'less'; # or 'dzen2'
$pipeout = popen($cmdout, "w");

do {
    $datestr = strftime($timeformat)."\n";
    fwrite($pipeout, $datestr);
    flush();
    sleep(1);
} while (true);

pclose($pipeout);
