#!/usr/bin/ruby

# http://ruby-doc.org/stdlib-2.0.0/libdoc/shell/rdoc/Shell.html

require 'shell'

path    = __dir__+ "/../assets"
cmdin   = 'conky -c ' + path + '/conky.lua'
cmdout  = 'dzen2'

sh = Shell.new

sh.transact { system(cmdin) | system(cmdout) }

