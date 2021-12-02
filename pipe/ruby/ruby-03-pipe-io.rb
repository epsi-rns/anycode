#!/usr/bin/ruby

# https://ruby-doc.org/core-2.2.0/Process.html#method-c-spawn

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

rd, wr = IO.pipe

if fork
  wr.close
  spawn(cmdout, in: rd )
  rd.close
  Process.wait
else
  rd.close
  generated_output(wr)
  wr.close
end
