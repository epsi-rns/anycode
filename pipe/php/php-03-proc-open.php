#!/usr/bin/php
<?php # using PHP7

$timeformat = '%a %b %d %H:%M:%S';
$cmdout  = 'dzen2';

$descriptorspec = array(
   0 => array('pipe', 'r'),  // stdin
   1 => array('pipe', 'w'),  // stdout
   2 => array('pipe', 'w',)  // stderr
);

$procout = proc_open($cmdout, $descriptorspec, $pipeout);

if (is_resource($procout)) {
    do {
        $datestr = strftime($timeformat)."\n";
        fwrite($pipeout[0], $datestr);

        sleep(1);
    } while (true);

    proc_close($procout);
}
