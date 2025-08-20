input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

defmodule Day02 do
  def part1(input) do
    Enum.count(input, &is_safe/1)
  end

  def part2(input) do
    Enum.count(input, &is_safe_with_tolerance/1)
  end

  defp is_safe_with_tolerance(levels) do
    levels
    |> remove_one_item_permutations()
    |> Enum.any?(&is_safe/1)
  end

  defp remove_one_item_permutations(list) do
    list
    |> Enum.with_index()
    |> Enum.map(fn {_, index} ->
      head = Enum.take(list, index)
      tail = Enum.drop(list, index + 1)
      head ++ tail
    end)
  end

  defp is_safe([a, a | _]), do: false

  defp is_safe([a, b | _] = levels) do
    diff = a - b
    is_safe(levels, div(diff, abs(diff)))
  end

  defp is_safe(levels, sign) do
    Enum.chunk_every(levels, 2, 1)
    |> Enum.all?(fn chunks ->
      case chunks do
        [a, b] ->
          (sign * (a - b)) in 1..3

        [_] ->
          true
      end
    end)
  end

  def parse(input) do
    input
    |> String.split("\n")
    |> Enum.reject(&(&1 == ""))
    |> Enum.map(fn line ->
      String.split(line, " ")
      |> Enum.map(&String.to_integer(&1))
    end)
  end
end

input = File.read!("day2.txt") |> Day02.parse()

input
|> Day02.part1()
|> IO.inspect()

input
|> Day02.part2()
|> IO.inspect()
