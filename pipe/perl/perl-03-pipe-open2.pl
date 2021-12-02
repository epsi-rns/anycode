#!/usr/bin/perl

use warnings;
use strict;

use Time::Piece;
use IPC::Open2;

my $cmdout  = "dzen2";

my ($rhout, $whout);
my $pidout = open2 ($rhout, $whout, $cmdout) 
    or die "can't pipeout: $!";
    
my $datestr;
my $timeformat = '%a %b %d %H:%M:%S';

while(1) {
    $datestr = localtime->strftime($timeformat);
    print $whout "$datestr \n";
    
    sleep 1;
}

waitpid( $pidout, 0 );


