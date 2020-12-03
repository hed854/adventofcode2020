import pytest
import sys
from day3 import Map, TobogganDrive

def test_map_init():
    t = Map("test_input")
    assert 11 == t.height
    assert 11 == t.width

def test_map_coordinates():
    t = Map("test_input")
    # non wrapped
    assert "." == t.get_tile(0,0)
    assert "#" == t.get_tile(3,0)
    assert "." == t.get_tile(0,3)
    assert "." == t.get_tile(3,3)
    # wrapped coordinates
    assert "." == t.get_tile(12,0)
    assert "#" == t.get_tile(14,0)
    assert "." == t.get_tile(12,3)
    assert "." == t.get_tile(14,3)

def test_map_display(capsys):
    # Basic layer only
    t = Map("test_input")
    t.display()
    capture = capsys.readouterr()
    reference = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#\n"
    assert reference == capture.out
    # With display layer and ANSI coloring
    t.display_layer[0][0] = "X"
    t.display()
    capture = capsys.readouterr()
    reference = "\033[0;31mX\033[0m.##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#\n"
    assert reference == capture.out

def test_drive(capsys):
    t = TobogganDrive(Map("test_input"))
    crashed = t.run()
    assert 7 == crashed
    t.map.display()
    capture = capsys.readouterr()
    reference = "\033[0;31m0\033[0m.##.......\n#..\033[0;31m0\033[0m#...#..\n.#....\033[0;31mX\033[0m..#.\n..#.#...#\033[0;31m0\033[0m#\n.\033[0;31mX\033[0m...##..#.\n..#.\033[0;31mX\033[0m#.....\n.#.#.#.\033[0;31m0\033[0m..#\n.#........\033[0;31mX\033[0m\n#.\033[0;31mX\033[0m#...#...\n#...#\033[0;31mX\033[0m....#\n.#..#...\033[0;31mX\033[0m.#\n"
    assert reference == capture.out
