input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

defmodule Day04 do
  def part1(parsed) do
    parsed
    |> Enum.with_index()
    |> Enum.map(fn {line, x} ->
      line
      |> Enum.with_index()
      |> Enum.map(fn {character, y} -> count_xmas(parsed, character, x, y, "XMAS") end)
      |> Enum.sum()
    end)
    |> Enum.sum()
  end

  def count_xmas(grid, character, x, y, to_find) when is_integer(x) and is_integer(y) do
    if character != String.at(to_find, 0) do
      0
    else
      to_find = String.slice(to_find, 1, String.length(to_find))

      [
        {0, 1},
        {0, -1},
        {-1, 1},
        {-1, 0},
        {-1, -1},
        {1, 0},
        {1, 1},
        {1, -1}
      ]
      |> Enum.count(&is_xmas(grid, x, y, &1, to_find))
    end
  end

  def is_xmas(_grid, _x, _y, _direction, ""), do: true

  def is_xmas(grid, x, y, {diff_x, diff_y}, to_find) do
    target = String.at(to_find, 0)
    to_find = String.slice(to_find, 1, String.length(to_find))

    at(grid, x + diff_x, y + diff_y) == target and
      is_xmas(grid, x + diff_x, y + diff_y, {diff_x, diff_y}, to_find)
  end

  def at(grid, x, y) when x >= 0 and x < 140 and y >= 0 and y < 140 do
    Enum.at(grid, x) |> Enum.at(y)
  end

  def at(_grid, _x, _y), do: "."

  def parse(input) do
    input
    |> String.split("\n")
    |> Enum.reject(&(&1 == ""))
    |> Enum.map(fn line -> line |> String.split("") |> Enum.reject(&(&1 == "")) end)
  end
end

File.read!("day4.txt")
|> Day04.parse()
|> Day04.part1()
|> IO.inspect()
