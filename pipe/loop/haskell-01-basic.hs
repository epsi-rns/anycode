import Data.Time.LocalTime
import Data.Time.Format

import Control.Concurrent
import Control.Monad

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- wrap Funktion

myTimeFormat = "%a %b %d %H:%M:%S"

wFormatTime :: FormatTime t => t -> String
wFormatTime myUtcTime = formatTime 
    Data.Time.Format.defaultTimeLocale myTimeFormat myUtcTime

wSleep :: Int -> IO ()
wSleep mySecond = threadDelay (1000000 * mySecond)

printDate = do
    now <- getZonedTime
    let nowFmt = wFormatTime now
    putStrLn nowFmt
    wSleep 1

-- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ---
-- main

main = forever $ printDate


