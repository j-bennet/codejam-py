import Control.Monad
import Data.List

data ScoreType = NonSurprising
               | Surprising
               | TooLow
               deriving (Eq, Show)
                 
isHigh :: Int -> Int -> ScoreType
isHigh p total = let (q, r) = quotRem total 3
                 in if q >= p then NonSurprising
                    else if q == p - 1 then if r >= 1
                                            then NonSurprising
                                            else if total > 0 then Surprising
                                                 else TooLow
                         else if q == p - 2 && r == 2
                              then Surprising
                              else TooLow

countHigh :: Int -> Int -> [Int] -> Int
countHigh sn p totals = snd $ countHigh' (sn, 0) 
  where
    countHigh' (s, c) = foldl' isHigh' (s, c) totals
    isHigh' (s, c) total = let scoreType = isHigh p total
                           in case scoreType of
                             NonSurprising -> (s, c + 1)
                             Surprising -> if s > 0 then (s - 1, c + 1)
                                           else (s, c)
                             TooLow -> (s, c)

main :: IO ()
main = do
  nCases <- readLn :: IO Int
  forM_ [1..nCases] $ \nCase -> do
    line <- getLine
    let (_:s:p:total) = map read $ words line
    let result = countHigh s p total
    putStrLn $ "Case #" ++ show nCase ++ ": " ++ show result
