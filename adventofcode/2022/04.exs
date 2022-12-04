input =
  "data/04.txt"
  |> File.read!()
  |> String.split("\n")
  |> Enum.reject(&(&1 == ""))
  |> IO.inspect()

ranges =
  input
  |> Enum.map(fn ranges ->
    ranges
    |> String.split(",")
    |> Enum.map(fn range ->
      [start, finish] = String.split(range, "-")
      Range.new(String.to_integer(start), String.to_integer(finish))
    end)
  end)

ranges
|> Enum.count(fn records ->
  [first, second] = records |> Enum.map(&MapSet.new/1)
  MapSet.subset?(first, second) or MapSet.subset?(second, first)
end)
|> IO.inspect()

ranges
|> Enum.count(fn [first, second] -> not Range.disjoint?(first, second) end)
|> IO.inspect()
