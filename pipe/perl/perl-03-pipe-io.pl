#!/usr/bin/perl

use warnings;
use strict;
use Time::Piece;
use IO::Pipe;

my $cmdout  = "lemonbar"; # or dzen2

my $pipeout = IO::Pipe->new();
my $handle = $pipeout->writer($cmdout);

my $datestr;
my $timeformat = '%a %b %d %H:%M:%S';

while(1) {
    $datestr = localtime->strftime($timeformat);
    print $pipeout "$datestr \n";
    
    flush $pipeout;    
    sleep 1;
}

$pipeout->close();

