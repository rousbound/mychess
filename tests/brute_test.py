import sys
sys.path.insert(0,'..')
from mychess.chess import Chess as Chess
from mychess.board import Board as Board
import copy



def move_generation_test(depth, chess=Chess(Board()), played_moves = ""):
    """
    Brute force all possible games within a certain ply depth (ply = half-move) to check
    program correctness against the Shannon number table

    """
    if depth == 0:
        # print(played_moves)
        return 1
    chess.legal_moves = chess.get_legal_moves()
    counter = 0
    for move in chess.legal_moves:
        # Make move
        board = copy.deepcopy(chess.board)
        algebric_move = chess.play_move(move)

        counter += move_generation_test(depth-1, chess, played_moves + " " + algebric_move)

        # Undo move

        chess.turn = not chess.turn
        chess.board = board
    return counter


import time
import datetime
import sys
import logging

if len(sys.argv) == 1:
    depth = 5
else:
    depth = int(sys.argv[2])

logging.basicConfig(filename='log/testBrute.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info(f"Initiating move generation test on depth: {depth}")
l = []
test_start = time.time()
ply_depth_start = time.time()
expected_results = [20,400,8902,197_281,4_865_609]
for i,j in zip(range(1,depth+1), expected_results):
    result = move_generation_test(i)
    l.append(result)
    logging.info(f"Result of possible games with {i} ply: {result}/{j} - {'OK' if result == j else 'ERROR'}")
    ply_elapsed_time = (time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - ply_depth_start)))
    logging.info(f"Elapsed time in {i} ply: {ply_elapsed_time} seconds")
    ply_depth_start = time.time()

all_elapsed_time = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - test_start))

logging.info(f"Total Elapsed time: ({all_elapsed_time})")