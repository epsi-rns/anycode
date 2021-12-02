#!/usr/bin/perl

use warnings;
use strict;
use File::Basename;
use IO::Pipe;

sub get_lemon_parameters { 
    # geometry: -g widthxheight+x+y
    my $xpos       = 0;
    my $ypos       = 0;
    my $width      = 640;
    my $height     = 24;

    my $geom_res   = "${width}x${height}+${xpos}+${ypos}";

    # color, with transparency
    my $fgcolor    = "#000000";
    my $bgcolor    = "#aaffffff";

    # XFT: require lemonbar_xft_git 
    my $font       = "monospace-9";

    # finally
    my $parameters = "  -g $geom_res -u 2"
                   . " -B $bgcolor -F $fgcolor"
                   . " -f $font";

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

sub run_lemon { 

    my $pipeout = IO::Pipe->new();
    
    my $cmd = "lemonbar " . get_lemon_parameters();
    my $handle = $pipeout->writer($cmd);
    
    generated_output($pipeout);
    $pipeout->close();
}

sub detach_lemon { 
    my $pid = fork;
    return if $pid;     # in the parent process
    
    run_lemon();
    exit; 
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all lemon instance
system('pkill lemonbar');

# run process in the background
detach_lemon();
