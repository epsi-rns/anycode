#!/usr/bin/ruby

# http://ruby-doc.org/core-1.8.7/IO.html#method-c-popen

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

cmdout  = 'less' # or 'dzen2'

IO.popen(cmdout, "w") do |f| 
  generated_output(f) 
        
  f.close()    
end
