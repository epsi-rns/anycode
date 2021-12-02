#!/usr/bin/ruby

def get_dzen2_parameters()
  xpos    = '0'
  ypos    = '0'
  width   = '640'
  height  = '24'
  fgcolor = '#000000'
  bgcolor = '#ffffff'
  font    = '-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*'

  parameters  = "  -x #{xpos} -y #{ypos} -w #{width} -h #{height}"
  parameters << " -fn '#{font}'"
  parameters << " -ta c -bg '#{bgcolor}' -fg '#{fgcolor}'"
# parameters << " -title-name dzentop"
end

def generated_output(stdin)
  timeformat = '%a %b %d %H:%M:%S'

  while true do
    localtime = Time.now
    datestr = localtime.strftime(timeformat)
    stdin.puts datestr

    sleep(1)
  end
end

def run_dzen2()
  cmdout  = 'dzen2 ' + get_dzen2_parameters()
  IO.popen(cmdout, "w") do |f| 
    generated_output(f) 
        
    f.close()    
  end
end

def detach_dzen2()
  # warning: Signal.trap is application wide
  Signal.trap("PIPE", "EXIT")
    
  pid = fork { run_dzen2() }
  Process.detach(pid)
end

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
system('pkill dzen2')

# run process in the background
detach_dzen2()
