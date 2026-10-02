"""Run with: python -m unittest test_moves -v"""
import random
import unittest
import moves


def board(white=(), black=()):
    cells = ["x"] * 23
    for i in white:
        cells[i] = "W"
    for i in black:
        cells[i] = "B"
    return "".join(cells)


class MoveTests(unittest.TestCase):
    def test_board_geometry(self):
        # Independently list connected paths from the diagram.
        paths = [(0,1,2), (3,4,5), (6,7), (8,9,10), (11,12,13),
                 (14,15,16), (17,18,19), (20,21,22), (0,8,20),
                 (3,9,17), (6,10,14), (7,11,16), (5,12,19),
                 (2,13,22), (0,3,6), (2,5,7), (20,17,14),
                 (22,19,16), (1,4), (15,18,21)]
        expected = {frozenset((a,b)) for path in paths for a,b in zip(path,path[1:])}
        actual = {frozenset((i,j)) for i in range(23) for j in moves.neighbors(i)}
        self.assertEqual(actual, expected)
        for i in range(23):
            for j in moves.neighbors(i):
                self.assertIn(i, moves.neighbors(j))
        for path in paths:
            if len(path) == 3:
                for color in ('W','B'):
                    b = board(path) if color == 'W' else board(black=path)
                    for i in path:
                        self.assertTrue(moves.closeMill(i,b))
        self.assertFalse(moves.closeMill(1,board((1,4,15))))

    def test_empty_opening(self):
        b = 'x' * 23
        results = moves.GenerateMovesOpening(b)
        self.assertEqual(results,[board((i,)) for i in range(23)])
        self.assertEqual(b,'x'*23)

    def test_capture_only_isolated(self):
        b = board((0,1), (3,4,5,8,13))
        results = moves.GenerateAdd(b)
        completed = [r for r in results if r[2]=='W']
        self.assertEqual(len(completed),2)
        self.assertEqual({i for r in completed for i in (8,13) if r[i]=='x'}, {8,13})
        self.assertTrue(all(r[3:6]=='BBB' for r in completed))

    def test_no_capture_available(self):
        b = board((0,1,2),(3,4,5))
        out = ['existing']
        moves.GenerateRemove(b,out)
        self.assertEqual(out,['existing',b])
        out=[]
        moves.GenerateRemove(board((0,1,2)),out)
        self.assertEqual(out,[board((0,1,2))])

    def test_hopping_and_movement(self):
        b=board((0,3,8),(1,4,9))
        self.assertEqual(moves.GenerateMovesMidgameEndgame(b),moves.GenerateHopping(b))
        self.assertIn(board((3,8,22),(1,4,9)),moves.GenerateHopping(b))
        self.assertNotIn(board((3,8,22),(1,4,9)),moves.GenerateMove(b))
        b=board((0,3,8,20),(1,4,9))
        self.assertEqual(moves.GenerateMovesMidgameEndgame(b),moves.GenerateMove(b))

    def test_random_move_invariants(self):
        rng=random.Random(4346)
        for _ in range(150):
            points=list(range(23)); rng.shuffle(points)
            nw=rng.randint(3,9); nb=rng.randint(3,9)
            b=board(points[:nw],points[nw:nw+nb])
            self.assertEqual(moves.swap_colors(moves.swap_colors(b)),b)
            for phase in ('opening','game'):
                for player in ('W','B'):
                    results=moves.generate_moves(b,phase,player)
                    opponent='B' if player=='W' else 'W'
                    for r in results:
                        moves.validate_board(r)
                        added=[i for i in range(23) if b[i]=='x' and r[i]==player]
                        removed=[i for i in range(23) if b[i]==player and r[i]=='x']
                        self.assertEqual(len(added),1)
                        self.assertEqual(len(removed),0 if phase=='opening' else 1)
                        if phase=='game' and b.count(player)!=3:
                            self.assertIn(added[0],moves.neighbors(removed[0]))
                        captures=[i for i in range(23) if b[i]==opponent and r[i]=='x']
                        self.assertLessEqual(len(captures),1)
                        if captures:
                            self.assertTrue(moves.closeMill(added[0],r))
                            self.assertFalse(moves.closeMill(captures[0],b))
                        changed=set(added+removed+captures)
                        self.assertTrue(all(b[i]==r[i] for i in range(23) if i not in changed))
                    mirror=[moves.swap_colors(r) for r in moves.generate_moves(moves.swap_colors(b),phase,opponent)]
                    self.assertEqual(results,mirror)

    def test_invalid_input(self):
        for b in ('x'*22,'z'*23,None):
            with self.assertRaises(ValueError):
                moves.GenerateAdd(b)
        for i in (-1,23,True):
            with self.assertRaises(ValueError):
                moves.neighbors(i)


if __name__ == '__main__':
    unittest.main()
