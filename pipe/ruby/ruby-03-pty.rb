#!/usr/bin/ruby

# https://ruby-doc.org/stdlib-2.2.3/libdoc/pty/rdoc/PTY.html

require 'pty'

def generated_output(stdin)
  timeformat = '%a %b %d %H:%M:%S'

  while true do
    localtime = Time.now
    datestr = localtime.strftime(timeformat)
    stdin.puts datestr

    sleep(1)
  end
end

cmdout  = 'dzen2' 

PTY.spawn(cmdout) { |output, input, pid| generated_output(input) }


