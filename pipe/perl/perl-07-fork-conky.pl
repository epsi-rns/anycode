#!/usr/bin/perl

use warnings;
use strict;
use File::Basename;
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
    my $pipein  = IO::Pipe->new();
     
    my $dirname = dirname(__FILE__);
    my $path    = "$dirname/../assets";       
    my $cmd     = "conky -c $path/conky.lua";
    my $handle  = $pipein->reader($cmd);

    while(<$pipein>) {
        print $pipeout $_;
        flush $pipeout;
    }
    
    $pipein->close();
}

sub run_dzen2 { 

    my $pipeout = IO::Pipe->new();
    
    my $cmd = "dzen2 " . get_dzen2_parameters();
    my $handle = $pipeout->writer($cmd);
    
    generated_output($pipeout);
    $pipeout->close();
}

sub detach_dzen2 { 
    my $pid = fork;
    return if $pid;     # in the parent process
    
    run_dzen2();
    exit; 
}

sub detach_transset { 
    my $pid = fork;
    return if $pid;     # in the parent process
    
    sleep 1;
    system('transset .8 -n dzentop >/dev/null');
    
    exit; 
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
system('pkill dzen2');

# run process in the background
detach_dzen2();

# optional transparency
# detach_transset();
