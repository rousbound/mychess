"""
This script tests draw conditions.

"""
import logging
import os

from mychess import Chess
import datetime 


# Configure logging


now = datetime.datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
logging.basicConfig(filename=f'log/test_draws_{dt_string}.log',
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%H:%M:%S',
        )

movedraw50 = ["d2d4 g8f6 c2c4 g7g6 b1c3 f8g7 e2e4 d7d6 g1f3 e8g8 f1e2 e7e5 e1g1 b8c6 d4d5 c6e7 f3d2 a7a5 a1b1 f6d7 a2a3 f7f5 b2b4 g8h8 f2f3 e7g8 d1c2 g8f6 c3b5 a5b4 a3b4 f6h5 g2g3 d7f6 c4c5 c8d7 b1b3 h5g3 h2g3 f6h5 f3f4 e5f4 c5c6 b7c6 d5c6 h5g3 b3g3 f4g3 c6d7 g3g2 f1f3 d8d7 c1b2 f5e4 f3f8 a8f8 b2g7 d7g7 c2e4 g7f6 d2f3 f6f4 e4e7 f8f7 e7e6 f7f6 e6e8 f6f8 e8e7 f8f7 e7e6 f7f6 e6b3 g6g5 b5c7 g5g4 c7d5 f4c1 b3d1 c1d1 e2d1 f6f5 d5e3 f5f4 f3e1 f4b4 d1g4 h7h5 g4f3 d6d5 e3g2 h5h4 e1d3 b4a4 g2f4 h8g7 g1g2 g7f6 f3d5 a4a5 d5c6 a5a6 c6b7 a6a3 b7e4 a3a4 e4d5 a4a5 d5c6 a5a6 c6f3 f6g5 f3b7 a6a1 b7c8 a1a4 g2f3 a4c4 c8d7 g5f6 f3g4 c4d4 d7c6 d4d8 g4h4 d8g8 c6e4 g8g1 f4h5 f6e6 h5g3 e6f6 h4g4 g1a1 e4d5 a1a5 d5f3 a5a1 g4f4 f6e6 d3c5 e6d6 g3e4 d6e7 f4e5 a1f1 f3g4 f1g1 g4e6 g1e1 e6c8 e1c1 e5d4 c1d1 c5d3 e7f7 d4e3 d1a1 e3f4 f7e7 d3b4 a1c1 b4d5 e7f7 c8d7 c1f1 f4e5 f1a1 e4g5 f7g6 g5f3 g6g7 d7g4 g7g6 d5f4 g6g7 f3d4 a1e1 e5f5 e1c1 g4e2 c1e1 e2h5 e1a1 f4e6 g7h6 h5e8 a1a8 e8c6 a8a1 f5f6 h6h7 e6g5 h7h8 d4e6 a1a6 c6e8 a6a8 e8h5 a8a1 h5g6 a1f1 f6e7 f1a1 g5f7 h8g8 f7h6 g8h8 h6f5 a1a7 e7f6 a7a1 f5e3 a1e1 e3d5 e1g1 g6f5 g1f1 d5f4 f1a1 f4g6 h8g8 g6e7 g8h8 e6g5", "7k/4N3/5K2/5BN1/8/8/8/r7 b - - 100 113"]


draw_three_fold_repetition = ["e2e4 e7e5 e1e2 e8e7 e2e1 e7e8 e1e2 e8e7 e2e1 e7e8 e1e2 e8e7 a2a4", "rnbq1bnr/ppppkppp/8/4p3/4P3/8/PPPPKPPP/RNBQ1BNR w - - 10 7"]

draw_by_stalemate = ["e2e4 e7e5 g1f3 b8c6 f1b5 c6d4 f3d4 e5d4 e1g1 c7c6 b5c4 g8f6 d2d3 d7d5 e4d5 f6d5 f1e1 f8e7 d1e2 c8e6 c2c3 d4c3 b1c3 e8g8 c4d5 c6d5 b2b3 e7f6 c1b2 a8c8 a1c1 d8a5 c3a4 d5d4 h2h3 a5g5 e2f3 b7b5 h3h4 g5d2 e1d1 c8c1 b2c1 d2a2 a4c5 f6h4 g2g3 h4e7 c5e6 f7e6 c1f4 a2b3 d1c1 e6e5 f3b7 e5f4 b7e7 f4g3 f2g3 b3d3 e7e6 g8h8 c1c8 d3g3 g1h1 g3f3 h1h2 h7h6 c8f8 f3f8 e6e4 f8d8 e4d3 b5b4 h2g2 a7a5 g2f2 a5a4 f2e2 a4a3 d3b3 d4d3 e2d2 d8d4 d2d1 d4c3 b3g8 h8g8", "6k1/6p1/7p/8/1p6/p1qp4/8/3K4 w - - 0 45"]


only_knight_left = ["d2d4 h7h5 c1g5 g8f6 c2c4 c7c6 b2b4 f6g8 e2e4 d8c7 d1h5 g8h6 g5e7 f8e7 c4c5 e7h4 h5g5 e8g8 h2h3 b7b5 e1d2 f8e8 g5e7 g7g5 d2c3 b8a6 e7e8 g8h7 c3b2 f7f5 e8h5 h7g7 h1h2 f5e4 d4d5 c7f4 g1e2 f4f5 h5f7 f5f7 b1d2 f7e8 a1b1 e8f7 d5d6 f7f6 b2c1 f6f4 c1d1 f4f7 e2c1 a6b8 a2a3 g5g4 b1a1 f7e6 f1e2 e6f6 c1b3 c8a6 e2c4 f6e7 d2f1 e7e8 h2h1 g7h7 d1d2 e8h5 c4e6 h4g5 f1e3 g5e3 d2c3 h7g6 f2f3 g6h7 h1c1 g4f3 c1e1 a6c8 e1e2 h7g6 e2b2 h6g4 h3h4 e3d2 c3d2 h5h4 a1f1 g4h6 e6g8 h4g3 d2e3 c8a6 b2d2 h6f7 d2d1 g3h3 a3a4 h3h7 b3a5 a6c8 e3f2 f7h8 d1d4 b8a6 f1a1 h7h4 g2g3 h4e7 d4e4 g6f5 e4e1 e7g7 g8c4 g7h6 e1e5 f5f6 f2f3 h6g6 e5e7 g6c2 e7e6 d7e6 a5b3 b5a4 a1d1 c2e2 f3f4 e2d3 c4e6 a6c7 g3g4 d3c3 d1d5 a4b3 e6f5 c3b4 f4g3 c7e6 f5g6 b4c3 g3h4 c3b2 d5f5 f6g6 f5f6 g6g7 f6f8 b2c3 f8f3 e6g5 h4h5 c3c4 f3f7 g7f7 h5g5 c4c3 g5h5 c3c1 d6d7 c1b2 h5h4 b2d4 d7c8q d4a4 c8f5 f7e8 f5d7 e8f8 h4h3 a4f4 d7f5 f8g7 h3g2 h8f7 f5f7 f4f7 g4g5 a8c8 g5g6 c8c7 g6f7 g7f6 g2g1 f6g5 g1f1 g5h4 f1g1 c7d7 g1h2 d7d2 h2g1 d2d6 g1f1 d6e6 f7f8r h4h3 f8f7 e6e5 f7b7 e5c5 f1f2 h3g4 b7e7 c5b5 e7h7 b5h5 h7f7 h5h2 f2e3 h2b2 f7f2 g4h4 f2f5 h4g3 f5b5 b2a2 b5b6 a2f2 e3d3 f2a2 b6b7 g3f4 b7d7 f4g5 d7e7 a7a6 d3c3 a2h2 e7e8 g5h5 c3d3 h2f2 e8g8 c6c5 g8f8 h5g4 f8f4 g4g5 f4f3 g5h6 d3e3 c5c4 f3f2 h6g7 e3f3 g7g8 f3e2 g8h8 f2f6 c4c3 e2f2 c3c2 f2g2 a6a5 g2g1 h8g7 f6h6 c2c1r g1g2 c1d1 h6e6 b3b2 e6h6 b2b1n h6f6 d1h1 f6f4 h1h4 f4c4 g7h8 c4c1 h4h7 c1g1 h7d7 g2h2 d7c7 g1g5 c7c4 g5g1 c4c6 g1g5 c6c1 g5g8 h8g8 h2g3 g8f8 g3f4 c1d1 f4f3 d1d7 f3g2 d7d6 g2h1 d6g6 h1h2 b1c3 h2h3 f8f7 h3h2 g6g7 h2h3 f7e7 h3h4 g7g2 h4h3 e7e6 h3g2 e6f7 g2h3 f7g8 h3h4 c3d1 h4g4 g8g7 g4h4 g7h6 h4g4 h6h7 g4f3 d1c3 f3g2 c3d5 g2h1 d5b6 h1g2 a5a4 g2h2 a4a3 h2g3 b6d5 g3h2 d5e3 h2g1 e3f1 g1f1 a3a2 f1e1 h7h6 e1f1 a2a1n", "8/8/7k/8/8/8/8/n4K2 w - - 0 172"]

only_bishop_left = [" a2a4 b8c6 a4a5 g8h6 c2c4 c6d4 e2e3 d7d6 h2h4 e7e5 b2b4 c8g4 d1a4 e8e7 a4c2 g4f3 c2a2 d8b8 a2a3 e5e4 g1f3 f7f5 g2g3 d4c6 f3d4 g7g5 d4b5 b8d8 f2f3 e7e8 f1d3 h8g8 h4g5 g8g6 a3b3 f8e7 b5a3 c6d4 f3e4 h6f7 e1f2 d8d7 b4b5 g6h6 h1h3 d4c6 f2f1 f7h8 b3d1 e7d8 h3h2 d8e7 a3c2 h6h3 c2a3 d7d8 d1g4 d6d5 c4c5 f5f4 g4f5 e7f8 d3c2 f8e7 f5e5 h7h5 e5c7 h8f7 c7e5 c6b4 g3g4 f4e3 e5e6 h3h2 e6c8 b4c6 f1e1 h2f2 c8f5 e8f8 f5e6 d8b6 c2d3 e7c5 e6h6 f7h6 g5h6 c5a3 e4e5 a8d8 d3e2 b6c5 b5b6 f8g8 e2d3 c5d6 d2e3 d8f8 e5d6 a3b4 e1d1 c6e5 a1a4 b4e1 d3c4 f8b8 e3e4 e5d3 a5a6 f2g2 e4d5 g2d2 c1d2 d3e5 b6a7 e5c4 a7a8b e1d2 a6a7 d2h6 a4b4 g8f7 b1c3 h6f8 a7b8b h5g4 c3b5 f7g8 b5c7 c4a3 b4b3 f8h6 b3b1 a3c4 b1b6 h6f8 b6b4 f8h6 d1e1 h6f4 e1e2 g4g3 c7a6 b7a6 b8c7 f4d6 a8c6 g3g2 c7d6 c4a5 b4b1 a5b7 d6a3 g2g1r b1d1 g8h7 a3f8 h7h8 c6d7 g1g7 d7a4 b7a5 d1g1 g7f7 a4c6 f7b7 e2f1 b7b4 f1e2 b4b3 e2f1 b3b2 f1e1 b2f2 c6b7 f2g2 d5d6 a5c4 g1f1 h8h7 f1h1 h7g6 h1h8 c4b6 b7c8 b6d7 h8h5 d7f6 h5h8 f6e4 c8b7 e4g3 h8h2 g2d2 e1d2 g3e4 b7e4 g6f7 f8h6 f7e6 d2e3 e6f6 e3f2 f6e5 e4g2 e5f5 f2g3 f5e6 g2h3 e6f7 g3g4 f7e6 g4f3 e6f6 h3f5 f6e5 h6d2 e5f5 h2h6 f5e5 f3g4 e5e4 g4h5 e4d5 d2g5 d5e5 d6d7 a6a5 d7d8n e5d4 h5h4 a5a4 h6a6 d4e4 g5f4 e4d5 f4e3 a4a3 a6a3 d5e4 h4h5 e4e5 e3d2 e5f5 d8f7 f5f6 d2c3 f6f7 c3d4 f7e6 h5g5 e6d6 d4g1 d6d7 g5f4 d7c7 a3c3 c7d8 g1e3 d8e7 c3c5 e7d6 e3g1 d6e6 f4g5 e6f7 g5f4 f7f8 c5c3 f8e8 g1e3 e8e7 c3c2 e7d7 e3a7 d7e8 f4f3 e8d7 f3g3 d7e8 g3g4 e8f7 c2a2 f7g6 g4f3 g6h7 a7c5 h7g8 f3f2 g8h8 f2f1 h8g8 a2a7 g8h8 c5b4 h8g8 a7a5 g8g7 a5a8 g7f7 b4a5 f7g6 a5d8 g6h6 a8a1 h6h5 d8b6 h5h4 f1e2 h4g3 a1a6 g3g2 a6a1 g2h2 b6e3 h2g2 e3g5 g2h3 a1a4 h3g3 a4g4 g3g4", "8/8/8/6B1/6k1/8/4K3/8 w - - 0 162"]

opposite_color_bishops = ["g1h3 b7b5 c2c4 a7a5 b2b3 f7f5 d1c2 b8c6 g2g4 a8b8 d2d3 a5a4 d3d4 c6e5 h3g1 g7g5 f2f3 d7d5 c1f4 b8b7 e1f2 a4a3 c2c3 e8f7 f1g2 f7g7 f4d2 e5g6 c4c5 h7h6 g1h3 b7a7 c3c1 c7c6 c1b2 d8c7 d2f4 c8a6 b2c3 g6h4 c3c2 e7e6 h3g1 c7e5 e2e4 e5d6 c2e2 h4g6 e4f5 a7c7 e2d1 d6d7 f4e5 g6e5 d1e1 e5f7 g2f1 d7d6 f1c4 d6d8 e1c3 c7a7 f2g2 d8c8 c3e1 f8d6 c4f1 d6e7 e1c1 a7d7 g1e2 e7c5 c1e1 f7e5 b3b4 e5g4 b1a3 d7b7 e1d1 e6e5 f3g4 g7f8 d1c2 h8h7 h2h3 f8f7 e2g1 c5a7 d4e5 b7c7 a3b1 c8e6 c2c4 c7e7 a2a3 a6c8 c4c5 e6f6 f1c4 f6d6 g2f1 f7f8 c4e2 e7g7 a3a4 c8b7 c5d4 g7f7 d4f4 g8f6 f1e1 b5a4 f4d4 d6d8 d4f2 b7a8 e1d2 a7b8 d2c1 f7g7 e2d3 g7g6 c1d1 d8c7 f2b6 f8e8 d1e1 h7g7 d3e2 c7d7 b1d2 g7g8 g1f3 d7c8 f3h4 b8e5 b6d8 c8d8 f5g6 d8b8 h1h2 e5c3 h2h1 b8h2 e2f3 h2f2 e1f2 e8d8 d2b3 c3e1 f2g2 f6g4 b3a5 g4e5 f3h5 d8c8 a1a2 g8h8 a2b2 c6c5 h5e2 e5d7 e2d1 c8d8 d1h5 h8g8 h5e2 a8b7 g6g7 d7e5 a5b3 e1c3 h1a1 b7a6 h4f5 c5c4 h3h4 d8c7 f5e3 e5g6 g2f3 g5g4 f3f2 g8h8 b3d4 a4a3 a1b1 c3b4 g7h8b g6h8 e2f1 c7d8 b2e2 b4a5 b1c1 a5d2 e3d1 h6h5 e2e7 c4c3 e7e3 d2e3 d1e3 a6e2 d4b5 h8f7 b5c3 e2c4 c1e1 c4a2 f2g3 d8c8 c3e4 f7d6 f1g2 c8b7 e1f1 d6c8 g3h2 b7c7 f1h1 c8e7 e4g5 c7d6 g2d5 a2d5 e3f5 e7f5 g5e6 d5a2 h1e1 f5g7 e1a1 d6e6 a1g1 e6e5 g1a1 e5e4 a1d1 a2g8 h2g3 g7f5 g3g2 f5d4 g2g1 d4c6 d1d2 c6d4 g1h2 e4e5 h2g2 g8h7 g2g1 h7f5 d2g2 f5e6 g2g4 h5g4 h4h5 e6d7 g1g2 e5d5 g2g3 d7e6 g3f4 d4f3 h5h6 e6f7 f4g4 d5d4 h6h7 a3a2 g4f5 d4c5 h7h8b a2a1n f5f6 c5b4 f6e7 b4a3 h8d4 f7h5 d4c3 f3h4 e7f6 a1b3 f6e5 a3a4 c3b2 b3c1 e5e6 h4g6 e6d5 a4b4 b2a3 b4c3 a3d6 c1a2 d6b8 a2c1 b8c7 g6e7 d5c5 e7f5 c7a5 c3b2 c5c6 f5d6 c6d6 b2b3 d6d7 c1a2 a5c7 b3c2 c7d8 h5e8 d7c7 c2c1 c7b7 e8b5 b7b8 b5d3 d8b6 a2b4 b8b7 c1b1 b6d4 b4d5 d4a7 d5b6 a7b6", "8/1K6/1B6/8/8/3b4/8/1k6 b - - 0 166"]

only_kings = ["b2b3 h7h6 c1b2 b7b5 c2c3 g7g5 e2e3 c7c6 a2a4 g5g4 d1f3 d8b6 b3b4 a7a6 h2h4 e7e6 f3e2 b6d8 a1a3 f8e7 e2d1 d7d6 d1e2 e8f8 e2g4 h8h7 g4e6 e7h4 e6a2 f7f5 d2d4 h4g3 f1b5 d8b6 b2c1 a8a7 b5a6 h7h8 a6b5 f8e7 h1h3 c8a6 e3e4 g8f6 a2e6 e7e6 h3g3 e6d7 e1f1 f5e4 a4a5 f6g8 b1d2 b6c7 b5e2 a6b7 g3g5 d7e7 g5e5 e7d8 f2f3 b7c8 e5h5 c8h3 f1f2 d8d7 e2a6 d7e6 d2b3 b8a6 g2g3 c7h7 c1f4 a7e7 b4b5 c6b5 f4g5 e6f7 f2e1 h3c8 c3c4 h7f5 g5c1 f5g4 e1d2 e7c7 d2c3 g4f3 c3b2 c7a7 b3d2 f3f2 a3a1 a7d7 b2b1 d7a7 d2b3 f2g2 g1e2 h8h7 b1b2 c8g4 c1h6 a7d7 a1c1 g2f1 c1c2 f1h3 d4d5 h3h5 b3d2 g8e7 c2c3 h5h2 b2b1 h2g1 e2c1 g1d4 c1a2 e7c8 h6e3 d4b6 e3g5 b6c5 a2b4 c8a7 c3c1 b5c4 c1c3 e4e3 b1c1 f7e8 g5d8 d7e7 b4c2 g4d7 c2a1 c5d4 d8c7 e7g7 d2e4 d7e6 e4g5 d4c3 c1b1 g7g6 g5e6 c3b4 b1c1 g6g5 c1d1 g5f5 c7d8 b4b6 e6c7 e8f8 d1e2 b6b8 a1c2 f5f1 d8f6 h7e7 c7a6 b8b6 f6d4 e7g7 d4e5 b6b8 e5g7 f8g7 e2f1 g7g6 c2e3 b8d8 e3c4 g6f5 c4b6 d8f8 b6a8 a7c6 f1g1 c6a5 a6c7 f8e7 c7e8 a5c4 g1f2 e7h7 e8f6 f5g6 f6g8 g6h5 a8b6 h7g6 g3g4 h5g5 f2e2 c4e3 b6a4 e3g4 e2d1 g6e6 d1c1 g4f6 d5e6 f6g4 a4b2 g4e3 b2a4 e3c4 g8e7 g5h6 e7g8 h6g7 g8e7 g7h6 c1d1 h6g5 e7g6 g5f5 g6f8 c4e5 a4c3 e5d7 d1e1 d7e5 e1e2 e5d3 e6e7 d6d5 f8g6 d3e5 c3b5 e5d3 e2d2 f5g4 g6f4 d3f4 b5c7 g4h5 c7a6 h5h4 a6b4 h4h3 e7e8q h3g4 e8e2 g4h3 e2e4 f4g2 e4e6 h3g3 e6h3 g3f4 h3b3 f4e5 b4d3 e5d4 b3b8 d4e4 b8b7 e4f5 d2d1 f5g6 b7a8 g6g7 d3e1 g2e1 a8d8 e1g2 d8h4 g7f7 h4h2 f7f6 h2g2 d5d4 g2c2 f6g7 d1e2 g7g8 e2f2 g8f8 c2c8 f8e7 c8a6 e7d7 a6a7 d7e6 a7h7 e6d6 h7h5 d6c7 h5b5 c7d8 b5b2 d8e7 b2b7 e7f6 b7b6 f6g7 b6d4 g7h7 d4b4 h7g8 b4d2 g8f8 d2g5 f8f7 g5g2 f7f6 f2f3 f6f5 g2g5 f5g5", "8/8/8/6k1/8/5K2/8/8 w - - 0 158"]

tests = [movedraw50, draw_three_fold_repetition, draw_by_stalemate, only_knight_left, only_kings]

def test_all_draw_cases():
    logging.info("----------------------------------------")
    for test in tests:

        # Create Chess() instance with initial position
        chess = Chess()

        # Play all moves and get resulting board state as FEN
        fen = chess.test_input_moves(test[0].split(" "))

        # Compare result with expected FEN 
        r = fen == test[1]

        # Log results
        result = "OK" if r else "ERROR"
        logging.info(f"Test with fen {test[1]} resulted in: {result}")
        assert r

    print("DRAW TEST SUCCESSFUL")
    logging.info(f"DRAW TEST SUCCESSFUL")

