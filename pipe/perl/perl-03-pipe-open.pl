#!/usr/bin/perl
# https://docstore.mik.ua/orelly/perl3/prog/ch16_03.htm

use warnings;
use strict;
use Time::Piece;

my $cmdout  = "less"; # or dzen2

open my $pipeout, "|-", $cmdout
    or die "Could not open filehandle: $!";
    
my $datestr;
my $timeformat = '%a %b %d %H:%M:%S';

while(1) {
    $datestr = localtime->strftime($timeformat);
    print $pipeout "$datestr \n";
    
    flush $pipeout;
    sleep 1;
}

close $pipeout


