input =
  "data/03.txt"
  |> File.read!()
  |> String.split("\n")
  |> Enum.reject(&(&1 == ""))

to_int = fn letter ->
  if String.upcase(letter) == letter do
    :binary.first(letter) - 38
  else
    :binary.first(letter) - 96
  end
end

input
|> Enum.map(&String.split_at(&1, round(String.length(&1) / 2)))
|> Enum.map(fn {a, b} ->
  MapSet.intersection(
    MapSet.new(a |> String.split("", trim: true)),
    MapSet.new(b |> String.split("", trim: true))
  )
end)
|> Enum.map(&(&1 |> Enum.at(0) |> to_int.()))
|> Enum.sum()
|> IO.inspect()

input
|> Enum.chunk_every(3)
|> Enum.reduce(0, fn records, sum ->
  records
  |> Enum.reduce(records |> hd() |> String.split("", trim: true) |> MapSet.new(), fn el, acc ->
    MapSet.intersection(acc, el |> String.split("", trim: true) |> MapSet.new())
  end)
  |> Enum.at(0)
  |> to_int.()
  |> Kernel.+(sum)
end)
|> IO.inspect()
