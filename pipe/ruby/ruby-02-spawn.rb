#!/usr/bin/ruby

# https://ruby-doc.org/core-2.2.0/Process.html#method-c-spawn

path    = __dir__+ "/../assets"
cmdin   = 'conky -c ' + path + '/conky.lua'
cmdout  = 'dzen2' 

read, write = IO.pipe

spawn(cmdin, out: write)
spawn(cmdout, in: read )

write.close

