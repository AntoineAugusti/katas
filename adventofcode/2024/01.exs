input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

defmodule Day1 do
  def part1(parsed) do
    {first, second} = parsed |> Enum.unzip()

    Enum.zip(Enum.sort(first), Enum.sort(second))
    |> Enum.map(fn {a, b} -> abs(a - b) end)
    |> Enum.sum()
  end

  def part2(parsed) do
    {first, second} = Enum.unzip(parsed)
    frequencies = Enum.frequencies(second)

    first
    |> Enum.map(fn n ->
      n * Map.get(frequencies, n, 0)
    end)
    |> Enum.sum()
  end

  def parse(input) do
    input
    |> String.split("\n")
    |> Enum.reject(&(&1 == ""))
    |> Enum.map(fn line ->
      {first, line} = Integer.parse(line)
      line = String.trim(line)
      {second, ""} = Integer.parse(line)
      {first, second}
    end)
  end
end

input = File.read!("day1.txt") |> Day1.parse()
Day1.part1(input) |> IO.inspect()
Day1.part2(input) |> IO.inspect()
