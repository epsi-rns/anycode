#!/usr/bin/ruby

# http://ruby-doc.org/core-1.8.7/IO.html#method-c-popen

def generated_output(stdin)
  timeformat = '%a %b %d %H:%M:%S'

  while true do
    localtime = Time.now
    datestr = localtime.strftime(timeformat)
    stdin.puts datestr

    sleep(1)
  end
end

cmdout  = 'less' # or 'dzen2'

IO.popen(cmdout, "w") { |f| generated_output(f) }

