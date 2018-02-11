import System.Process
import System.IO
import System.Posix.Process

import Data.Time.LocalTime
import Data.Time.Format

import Control.Concurrent
import Control.Monad

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- wrap Funktion

cmdout = "dzen2"

getDzen2Parameters = [
      "-x", xpos,  "-y", ypos,
      "-w", width, "-h", height,
      "-fn", font,
      "-ta", "c",
      "-bg", bgcolor,
      "-fg", fgcolor       --,
--    "-title-name", "dzentop"
    ]
  where    
    xpos    = "0"
    ypos    = "0"
    width   = "640"
    height  = "24"
    fgcolor = "#000000"
    bgcolor = "#ffffff"
    font    = "-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*"


wFormatTime :: FormatTime t => t -> String
wFormatTime myUtcTime = formatTime 
    Data.Time.Format.defaultTimeLocale myTimeFormat myUtcTime
  where myTimeFormat = "%a %b %d %H:%M:%S"


wSleep :: Int -> IO ()
wSleep mySecond = threadDelay (1000000 * mySecond)

generatedOutput pipein = do
     now <- getZonedTime
     let nowFmt = wFormatTime now
     
     hPutStrLn pipein nowFmt
     hFlush pipein

     wSleep 1

runDzen2 = do
    (Just pipein, _, _, ph)  <- 
        createProcess (proc cmdout getDzen2Parameters) 
        { std_in = CreatePipe }
    
    forever $ generatedOutput pipein
    
    hClose pipein

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

main = do
    -- remove all dzen2 instance
    system "pkill dzen2"

    -- run process in the background
    -- forkProcess is required since we use forever control
    forkProcess $ runDzen2
    
    putStr ""
