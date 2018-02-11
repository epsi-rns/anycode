#!/usr/bin/ruby

# http://ruby-doc.org/stdlib-2.4.1/libdoc/open3/rdoc/Open3.html#method-c-pipeline_w

require 'open3'

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

Open3.pipeline_w(cmdout) {|i, ts| generated_output(i) }

