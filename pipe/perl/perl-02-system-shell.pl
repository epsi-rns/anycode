#!/usr/bin/perl
# Using system shell

use warnings;
use strict;
use File::Basename;

# reset the terminal, for use with less
system('reset');

my $dirname = dirname(__FILE__);
my $path    = "$dirname/../assets";
my $cmdin   = "conky -c $path/conky.lua";
my $cmdout  = "less"; # or dzen2
my $cmd     = "$cmdin | $cmdout";

# execute pipe
system($cmd);
