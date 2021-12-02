#!/usr/bin/perl

use warnings;
use strict;
use Time::Piece;
use IO::Pipe;

my $timeformat = '%a %b %d %H:%M:%S';

my $datestr;
while(1) {
    $datestr = localtime->strftime($timeformat);
    print "$datestr \n";
      
    sleep 1;
}


