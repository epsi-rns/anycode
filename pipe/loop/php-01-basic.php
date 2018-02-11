#!/usr/bin/php 
<?php # using PHP7

$timeformat = '%a %b %d %H:%M:%S';

do {
    print strftime($timeformat)."\n";
    sleep(1);
} while (true);
