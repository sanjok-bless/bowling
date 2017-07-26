# bowling

python 3.5.2

Task:
1. See scoring rules for 10 pin bowling below
2. Create function to calculate game score
3. Provide testcases to ensure your code is correct
4. Put resulting code and testcases into github and send me a link
5. Do not worry about data input/output, you can hardcode list of
integers to provide input data and print output to console
6. RULES (FYI you can find Russian version here :
http://bowling.sin.ru/score.shtml)
The scoring rules of 10-pin bowling are as follows:

1) A game consists of 10 frames. In each frame, the bowler has two
chances to knock down as many pins as possible.
2) For each pin knocked down, the bowler scores 1 point.
3) If the bowler knocks off all pins with the first ball in a frame,
it is called a "strike". In this case, the number of pins knocked off
in the next two balls bowled is also added to the player's score for
this frame.
4) Instead, if the bowler knocks off all remaining pins with the
second ball in a frame, it is called a "spare". In this case, the
number of pins knocked off in the next ball bowled is also added to
the player's score for this frame.
5) If the player bowls a strike in the last frame, he is awarded two
extra balls so as to allow the awarding of bonus points. If both these
balls also result in strikes, a total of 30 points (10 + 10 + 10) is
awarded for the frame. Similarly, if the player bowls a spare in the
last frame, he is awarded one extra ball and the score for that ball
is added to the score of the last frame.

Let's calculate points for this game (I split frames with | symbols)
Frames: 1     2       3     4     5     6      7     8       9           10
             10 | 3,7 | 6,1 | 10 | 10 | 10 | 2,8 | 9,0 | 7,3 | 10, 10, 10|

frame   -  points
1 -   strike 10 + 3 + 7 = 20
2 -   spare  (3+7) + 6 = 36
3 -   7                           = 43
4 -   strike 10+10+10 = 73
5 -   strike 10+10+2   = 95
6 -   strike 10+2+8     = 115
7 -   spare (2+8)+9     = 134
8 -   9                           = 143
9     spare (7+3)+10   = 163
10  strike 10+10+10  = 193 (two additional balls given)

So function will take a list
[10,3,7,6,1,10,10,10,2,8,9,0,
7,3,10,10,10] and return 193
