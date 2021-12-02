#!/usr/bin/php
<?php # using PHP7

function get_lemon_parameters() 
{ 
    # geometry: -g widthxheight+x+y
    $xpos     = 0;
    $ypos     = 0;
    $width    = 640;
    $height   = 24;

    $geom_res = "${width}x${height}+${xpos}+${ypos}";

    # color, with transparency
    $fgcolor  = "'#000000'";
    $bgcolor  = "'#aaffffff'";

    # XFT: require lemonbar_xft_git 
    $font     = 'monospace-9';

    # finally  
    $parameters  =  " -g $geom_res -u 2"
                  . " -B $bgcolor -F $fgcolor"
                  . " -f $font";

    return $parameters;
}

function generated_output($process)
{
    $path    = __dir__."/../assets";
    $cmdin   = 'conky -c '.$path.'/conky.lua';
    $pipein  = popen($cmdin,  "r"); # handle
    
    while(!feof($pipein)) {
        $buffer = fgets($pipein);
        fwrite($process, $buffer);
        flush();
    }
    
    pclose($pipein);
}

function run_lemon() 
{ 
    $cmdout  = 'lemonbar '.get_lemon_parameters();
    $pipeout = popen($cmdout, "w");

    generated_output($pipeout);

    pclose($pipeout);
}

function detach_lemon() 
{ 
    $pid = pcntl_fork();
    
    switch($pid) {         
         case -1 : die('could not fork'); // fork errror         
         case 0  : run_lemon(); break;    // we are the child
         default : return $pid;           // we are the parent             
    }    
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all lemonbar instance
system('pkill lemonbar');

# run process in the background
detach_lemon();
