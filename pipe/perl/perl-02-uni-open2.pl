#!/usr/bin/perl
# Unidirectional Pipe Example
# A pipe has a read end and a write end.

use warnings;
use strict;

use File::Basename;
use IPC::Open2;

my $dirname = dirname(__FILE__);
my $path    = "$dirname/../assets";
my $cmdin   = "conky -c $path/conky.lua";
my $cmdout  = "dzen2";

my ($rhin, $whin);
my $pidin  = open2 ($rhin,  $whin,  $cmdin)  
    or die "can't pipein: $!";

my ($rhout, $whout);
my $pidout = open2 ($rhout, $whout, $cmdout) 
    or die "can't pipeout: $!";

my $line = '';
while ($line = <$rhin>) {
    print $whout $line;
}

waitpid( $pidin,  0 );
waitpid( $pidout, 0 );
