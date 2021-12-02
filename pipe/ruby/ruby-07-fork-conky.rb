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
  path    = __dir__+ "/../assets"
  cmdin   = 'conky -c ' + path + '/conky.lua'
    
  IO.popen(cmdin, "r") do |f| 
    while f do
      stdin.puts f.gets
    end
    f.close()    
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

def detach_transset()
  pid = fork do
    sleep(1)
    system('transset .8 -n dzentop >/dev/null')        
  end
    
  Process.detach(pid)
end

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
system('pkill dzen2')

# run process in the background
detach_dzen2()

# optional transparency
# detach_transset()
