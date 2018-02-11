#!/usr/bin/php
<?php # using PHP7

function get_dzen2_parameters() 
{ 
    $xpos    = 0;
    $ypos    = 0;
    $width   = 640;
    $height  = 24;
    $fgcolor = "#000000";
    $bgcolor = "#ffffff";
    $font    = "-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*";

    $parameters  = "  -x $xpos -y $ypos -w $width -h $height";
    $parameters .= " -fn '$font'";
    $parameters .= " -ta c -bg '$bgcolor' -fg '$fgcolor'";
#   $parameters .= " -title-name dzentop";

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

function run_dzen2() 
{ 
    $cmdout  = 'dzen2 '.get_dzen2_parameters();
    $pipeout = popen($cmdout, "w");

    generated_output($pipeout);

    pclose($pipeout);
}

function detach_dzen2() 
{ 
    $pid = pcntl_fork();
    
    switch($pid) {         
         case -1 : die('could not fork'); // fork errror         
         case 0  : run_dzen2(); break;    // we are the child
         default : return $pid;           // we are the parent             
    }    
}

function detach_transset() { 
    $pid = pcntl_fork();
    if ($pid == 0) { 
        sleep(1);
        system('transset .8 -n dzentop >/dev/null');
    }
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
system('pkill dzen2');

# run process in the background
detach_dzen2();

# optional transparency
# detach_transset();
