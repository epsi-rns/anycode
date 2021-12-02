#!/usr/bin/perl
# Unidirectional Pipe Example
# A pipe has a read end and a write end.

use warnings;
use strict;
use File::Basename;

my $dirname = dirname(__FILE__);
my $path    = "$dirname/../assets";
my $cmdin   = "conky -c $path/conky.lua";
my $cmdout  = "dzen2 -ta l"; # or dzen2

open my $pipein, "-|", $cmdin
    or die "Could not open filehandle: $!";

open my $pipeout, "|-", $cmdout
    or die "Could not open filehandle: $!";
    
while(<$pipein>) {
    print $pipeout $_;
    flush $pipeout;
}

close $pipein;
close $pipeout;

