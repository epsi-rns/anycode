#!/usr/bin/perl
# Unidirectional Pipe Example
# A pipe has a read end and a write end.

use warnings;
use strict;
use File::Basename;
use IO::Pipe;

my $dirname = dirname(__FILE__);
my $path    = "$dirname/../assets";
my $cmdin   = "conky -c $path/conky.lua";
my $cmdout  = "less"; # or dzen2

my $pipein  = IO::Pipe->new();
my $hnd_in  = $pipein->reader($cmdin);

my $pipeout = IO::Pipe->new();
my $hnd_ou  = $pipeout->writer($cmdout);

while(<$pipein>) {
    print $pipeout $_;
    flush $pipeout;
}
    
$pipein->close();
$pipeout->close();
