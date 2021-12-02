#!/usr/bin/perl

use warnings;
use strict;
use Time::Piece;
use IO::Pipe;

sub get_dzen2_parameters { 
    my $xpos    = 0;
    my $ypos    = 0;
    my $width   = 640;
    my $height  = 24;
    my $fgcolor = "#000000";
    my $bgcolor = "#ffffff";
    my $font    = "-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*";

    my $parameters = "  -x $xpos -y $ypos -w $width -h $height";
    $parameters   .= " -fn '$font'";
    $parameters   .= " -ta c -bg '$bgcolor' -fg '$fgcolor'";
#   $parameters   .= " -title-name dzentop";
    
    return $parameters;
}

sub generated_output {
    my $pipeout = shift;

    my $datestr;
    my $timeformat = '%a %b %d %H:%M:%S';
    
    while(1) {
        $datestr = localtime->strftime($timeformat);
        print $pipeout "$datestr \n";

        flush $pipeout;
        sleep 1;
    }
}

sub run_dzen2 { 

    my $parameters = get_dzen2_parameters();

    my $pipeout = IO::Pipe->new();
    my $childhandle = $pipeout->writer("dzen2 $parameters");

    generated_output($pipeout);
    $pipeout->close();
}

sub detach_dzen2 { 
    my $pid = fork;
    return if $pid;     # in the parent process
    
    run_dzen2();
    exit; 
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
system('pkill dzen2');

# run process in the background
detach_dzen2();
