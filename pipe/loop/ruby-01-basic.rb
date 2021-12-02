#!/usr/bin/ruby

timeformat = '%a %b %d %H:%M:%S'

while true do
  localtime = Time.now
  datestr = localtime.strftime(timeformat)
  puts datestr

  sleep(1)
end
