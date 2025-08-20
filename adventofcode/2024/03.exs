input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

defmodule Day03 do
  def part1(input) do
    Regex.scan(~r/mul\((\d+),(\d+)\)/, input)
    |> Enum.map(fn [_, a, b] ->
      String.to_integer(a) * String.to_integer(b)
    end)
    |> Enum.sum()
  end

  def part2(input) do
    Regex.scan(~r/mul\((\d+),(\d+)\)|do\(\)|don't\(\)/, input)
    |> Enum.reduce({true, 0}, fn match, {enabled, acc} ->
      case match do
        ["don't()"] ->
          {false, acc}

        ["do()"] ->
          {true, acc}

        [_, a, b] when enabled ->
          {enabled, acc + String.to_integer(a) * String.to_integer(b)}

        _ ->
          {enabled, acc}
      end
    end)
  end
end

File.read!("day3.txt")
|> Day03.part1()
|> IO.inspect()

File.read!("day3.txt")
|> Day03.part2()
|> IO.inspect()
